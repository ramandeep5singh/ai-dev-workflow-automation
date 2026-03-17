from services.n8n_client import generate_unit_tests_n8n_client

def generate_unit_tests(code: str):
    """
    Generate Python unit tests for the provided code.
    """
    return generate_unit_tests_n8n_client(code)