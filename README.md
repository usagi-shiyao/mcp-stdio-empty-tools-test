# MCP Stdio Empty Tools Test

一个用于测试 MCP Stdio 协议连接和工具发现机制的最小化 MCP Server。

本项目基于官方 MCP Python SDK（FastMCP）实现，**故意不注册任何 Tool**，用于验证 MCP 客户端能否正确处理以下场景：

- Stdio 进程正常启动。
- MCP 初始化握手成功。
- 服务端正常响应 `tools/list` 请求。
- 工具发现结果为空（0 个工具）。
- 客户端能够区分连接失败与连接成功但没有可用工具。

## 1. 项目说明

| 项目 | 内容 |
|---|---|
| 项目名称 | mcp-stdio-empty-tools-test |
| MCP Server 名称 | Empty Tools Test Server |
| MCP 协议 | Stdio |
| 开发语言 | Python |
| SDK | MCP Python SDK |
| 工具数量 | 0 |
| 项目用途 | MCP 连接与空工具发现测试 |

## 2. 项目结构

```text
mcp-stdio-empty-tools-test/
├── server.py
├── requirements.txt
└── README.md
```

## 3. 环境要求

- Python 3.10+
- pip
- 能够安装 Python 第三方依赖的环境

## 4. 安装依赖

执行以下命令安装 MCP Python SDK：

```bash
pip install -r requirements.txt
```

也可以直接执行：

```bash
pip install "mcp>=1.0,<2"
```

## 5. 启动服务

在项目根目录执行：

```bash
python server.py
```

服务启动后不会主动输出工具列表，也不会启动 HTTP 端口。

这是正常行为。Stdio MCP Server 会等待 MCP 客户端通过标准输入发送协议请求，并通过标准输出返回协议响应。

## 6. MCP 服务实现

服务端代码位于 `server.py`。

```python
from mcp.server.fastmcp import FastMCP

# 创建 MCP Server
mcp = FastMCP("Empty Tools Test Server")

# 本项目故意不注册任何 Tool

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

注意：

- 不注册任何 `@mcp.tool()`。
- 使用 `stdio` 作为通信传输方式。
- 不启动 HTTP 服务。
- 不需要 API Key 或其他环境变量。

## 7. MCP 客户端启动配置

如果 MCP 客户端支持 Stdio 启动配置，可以使用以下参数：

**启动命令：**

```text
python
```

**启动参数：**

```json
[
  "server.py"
]
```

**环境变量：**

无需配置。

注意：客户端需要在仓库代码所在目录启动进程，并确保已经安装项目依赖。

## 8. 预期测试结果

当 MCP 客户端成功启动服务并完成初始化后，预期结果如下：

| 验证项目 | 预期结果 |
|---|---|
| 进程启动 | 成功 |
| MCP 初始化 | 成功 |
| Stdio 通信 | 正常 |
| 工具列表请求 | 正常响应 |
| 工具发现数量 | 0 |
| 工具列表 | 空列表 |
| 连接状态 | 成功 |

本项目的核心测试结果是：

```json
{
  "connection_status": "success",
  "transport": "stdio",
  "server_name": "Empty Tools Test Server",
  "tool_count": 0,
  "tools": []
}
```

以上 JSON 仅用于说明预期测试结果，并非服务端直接输出的原始 MCP 协议报文。

## 9. 测试目的

本项目主要用于验证 MCP 客户端的异常处理和边界场景：

1. 是否允许成功连接但发现 0 个工具。
2. 是否能够正确展示空工具列表。
3. 是否会错误地将 0 个工具判定为连接失败。
4. 是否能够区分服务启动失败、协议握手失败和工具列表为空。
5. 是否能够正确展示服务端名称和连接状态。

## 10. 重要说明

本项目是一个用于开发和测试的最小化 MCP Server，不提供任何实际业务工具。

工具数量为 0 是项目的预期设计，不代表 MCP 服务异常。

项目仅用于测试 MCP Stdio 连接与工具发现能力，不建议用于生产环境。
