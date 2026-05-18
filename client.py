import asyncio


async def receive_messages(reader):
    while True:
        data = await reader.read(100)

        if not data:
            break

        print(data.decode().strip())


async def send_messages(writer):
    while True:
        message = await asyncio.to_thread(input, "")

        writer.write(message.encode())
        await writer.drain()


async def main():
    reader, writer = await asyncio.open_connection(
        "127.0.0.1",
        8888
    )

    await asyncio.gather(
        receive_messages(reader),
        send_messages(writer)
    )


asyncio.run(main())