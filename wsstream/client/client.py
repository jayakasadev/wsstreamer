import asyncio
import sys
import socketio

# asyncio
sio = socketio.AsyncClient(logger=True, engineio_logger=True)


@sio.event
async def hello(data):
    print("I received a message!", data)


@sio.event
async def stream(data):
    print(data)

@sio.event
async def connect():
    print("I'm connected:", sio.get_sid())


@sio.event
async def connect_error():
    print("The connection failed!")


@sio.event
async def disconnect():
    print("I'm disconnected!")


async def bg_task():
    print("bg_task")


async def main():

    await sio.connect("http://localhost:5000")
    sio.start_background_task(bg_task)
    while sio.get_sid() is None:
        await sio.sleep(0.1)
    await sio.emit("hello", {"response": "hello"})
    await sio.sleep(1.0)
    await sio.emit("stream", None)
    await sio.sleep(2.0)
    await sio.disconnect()

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
