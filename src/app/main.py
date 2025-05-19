from fastmcp import FastMCP

mcp = FastMCP(stateless_http=True, json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integers.
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.
    """
    return a * b

app = mcp.http_app()