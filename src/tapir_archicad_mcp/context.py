from contextvars import ContextVar
from mcp.server.mcpserver import MCPServer
from multiconn_archicad.multi_conn import MultiConn

mcp_instance: ContextVar[MCPServer] = ContextVar("mcp_instance")
multi_conn_instance: ContextVar[MultiConn] = ContextVar("multi_conn_instance")