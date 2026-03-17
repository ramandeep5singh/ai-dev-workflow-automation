from fastmcp import FastMCP
from tools.generate_feature_tasks import generate_feature_tasks
from tools.generate_unit_tests import generate_unit_tests

mcp = FastMCP("dev-workflow-tools")


@mcp.tool()
def generate_feature_tasks_tool(description: str):
    """
    Generate development tasks for implementing a software feature.
    """
    return generate_feature_tasks(description)

@mcp.tool()
def generate_unit_tests_tool(code: str):
    """
    Generate Python unit tests for the provided code.
    """
    return generate_unit_tests(code)

if __name__ == "__main__":
    mcp.run()