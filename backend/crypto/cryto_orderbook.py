from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import websockets

app = FastAPI()
# Allow CORS for all origins
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

COINBASE_WS_URL = "wss://ws-feed.exchange.coinbase.com"

@app.websocket("/ws/orderbook")
async def orderbook_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        async with websockets.connect(COINBASE_WS_URL) as ws:
            await ws.send(json.dumps({
                "type": "subscribe",
                "channels": [{"name": "level2", "product_ids": ["BTC-USD"]}]
            }))
            async for message in ws:
                data = json.loads(message)
                if data.get("type") == "snapshot":
                    if data.get("type") in ["l2update", "snapshot"]:
                        update = {
                            "bids": data.get("bids", []),
                            "asks": data.get("asks", []),
                            "type": data.get("type")
                        }
                        await websocket.send_json(update)
    except WebSocketDisconnect:
        pass
    except Exception as e:
        await websocket.close(code=1000, reason=str(e))
        print(f"WebSocket error: {e}")