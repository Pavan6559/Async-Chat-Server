import asyncio

clients = set()


async def broadcast(message, sender_writer):
    for client in clients:
        if client != sender_writer:
            client.write(message.encode())
            await client.drain()


async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"{addr} connected")

    clients.add(writer)

    try:
        while True:
            data = await reader.read(100)

            if not data:
                break

            message = data.decode().strip()

            print(f"{addr}: {message}")

            await broadcast(f"{addr}: {message}\n", writer)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print(f"{addr} disconnected")

        clients.remove(writer)

        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        8888
    )

    addr = server.sockets[0].getsockname()
    print(f"Server running on {addr}")

    async with server:
        await server.serve_forever()


asyncio.run(main())