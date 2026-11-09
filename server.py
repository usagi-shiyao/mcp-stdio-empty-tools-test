```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Empty Tools Test Server")


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
```
