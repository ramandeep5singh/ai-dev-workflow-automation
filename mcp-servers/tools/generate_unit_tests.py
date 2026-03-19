from services.n8n_client import send_tool_request

def generate_unit_tests(code: str):
    """
    Generate Python unit tests for the provided code.
    """
    return send_tool_request("generate_unit_tests",{"code": code})