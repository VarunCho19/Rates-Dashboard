import asyncio
import websockets

async def test_ws():
    uri = "ws://127.0.0.1:8000/ws/orderbook"
    async with websockets.connect(uri) as websocket:
        print("✅ Connected")
        for _ in range(5):
            msg = await websocket.recv()
            print("📨", msg)



asyncio.run(test_ws())