from mcp.server.fastmcp import FastMCP

# 创建 MCP 服务，不注册任何工具
mcp = FastMCP("Empty Tools Test Server")

if __name__ == "__main__":
    mcp.run(transport="stdio")
