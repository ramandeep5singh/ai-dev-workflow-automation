from fastmcp import FastMCP
import requests

mcp = FastMCP("dev-workflow-tools")


@mcp.tool()
def generate_feature_tasks(feature_description: str) -> dict:
    """
    Generate development tasks from a feature description
    using the n8n workflow.
    """

    url = "http://localhost:5678/webhook/generate-feature-tasks"

    payload = {
        "input_data": feature_description
    }

    response = requests.post(url, json=payload)

    if response.headers.get("content-type","").startswith("application/json"):
        return response.json()
    else:
        return {
            "status_code": response.status_code,
            "raw_response": response.text
        }


if __name__ == "__main__":
    print(generate_feature_tasks("Build OAuth login system"))