import asyncio
import websockets


async def websocket_client():
    uri = "wss://echo.websocket.org"

    async with websockets.connect(uri) as websocket:
        message = "Hello, WebSocket!"
        await websocket.send(message)
        print(f"Wysłano: {message}")

        response = await websocket.recv()
        print(f"Otrzymano: {response}")


asyncio.get_event_loop().run_until_complete(websocket_client())
