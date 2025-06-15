from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import websockets
import json

app = FastAPI()

origins = [
    "http://localhost:5173",  # for local dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] temporarily
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Coinbase WebSocket URL for BTC-USD level2 updates
COINBASE_WS_URL = "wss://ws-feed.exchange.coinbase.com"

@app.websocket("/ws/ticker")
async def ticker_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        async with websockets.connect(COINBASE_WS_URL) as ws:
            # Subscribe to ticker channel for BTC-USD
            subscribe_msg = {
                "type": "subscribe",
                "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
            }
            await ws.send(json.dumps(subscribe_msg))
            print("✅ Subscribed to Coinbase ticker")

            async for message in ws:
                data = json.loads(message)
                print("📩 Ticker data:", data)
                if data.get("type") == "ticker":
                    update = {
                        "type": data["type"],
                        "price": data.get("price"),
                        "best_bid": data.get("best_bid"),
                        "best_ask": data.get("best_ask"),
                        "time": data.get("time")
                    }
                    await websocket.send_text(json.dumps(update))
    except WebSocketDisconnect:
        print("🔌 WebSocket disconnected")
    except Exception as e:
        await websocket.close()
        print(f"WebSocket error: {e}")

@app.get("/")
def root():
    return {"message": "Real-Time Ticker via Coinbase WebSocket"}
