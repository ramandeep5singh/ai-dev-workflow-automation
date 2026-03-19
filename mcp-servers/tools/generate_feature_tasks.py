from services.n8n_client import send_tool_request

def generate_feature_tasks(feature_description: str):

    return send_tool_request("generate_feature_tasks", {"feature_description": feature_description})