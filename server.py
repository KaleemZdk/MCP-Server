import asyncio
from fastmcp import Client

async def main():
    async with Client("fastmcp_calc.py") as client:
        tools = await client.list_tools()
        print("Available tools:", [t.name for t in tools])

        result = await client.call_tool("multiply", {"a": 6, "b": 7})
        print("Result:", result)

asyncio.run(main())