<img width="1440" height="840" alt="image" src="https://github.com/user-attachments/assets/d8726d67-1412-4cbb-b058-cf4aa702a9f7" />

# Async Chat Server

An asynchronous TCP chat server built with Python's `asyncio` library to understand event-driven programming, coroutines, task scheduling, and concurrent client communication without traditional multithreading.

## Overview

This project demonstrates how modern async systems work internally using:
- `async` / `await`
- event loops
- coroutines
- asynchronous sockets
- concurrent task execution
- non-blocking I/O

The server allows multiple clients to connect and communicate concurrently using a single-threaded asynchronous architecture.

---

## Features

- Multiple concurrent client connections
- Real-time message broadcasting
- Non-blocking asynchronous communication
- Lightweight event-driven architecture
- Concurrent send/receive handling using `asyncio.gather()`
- Simple TCP socket implementation using asyncio streams

---

## Tech Stack

- Python 3.10+
- asyncio
- TCP sockets

---

## Project Structure

```bash
project/
│
├── server.py
└── client.py
