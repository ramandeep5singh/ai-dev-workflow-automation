from fastmcp import FastMCP
from tools.generate_feature_tasks import generate_feature_tasks

mcp = FastMCP("dev-workflow-tools")


@mcp.tool()
def generate_feature_tasks_tool(description: str):
    """
    Generate development tasks for implementing a software feature.
    """
    return generate_feature_tasks(description)

if __name__ == "__main__":
    mcp.run()