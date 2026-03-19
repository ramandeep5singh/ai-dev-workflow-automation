import requests

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/ai-dev-workflow"


def send_tool_request(tool: str, input: dict):
    payload = {
        "tool": tool,
        "input": input
    }
    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=payload,
            timeout=600
        )

        return response.json()
    
    except requests.exceptions.Timeout:
        return {"error": "Request to n8n timed out"}
    
    except Exception as e:
        return {"error": str(e)}


# def generate_tasks(feature_description: str):

#     payload = {
#         "tool": "generate_feature_tasks",
#         "input": {
#             "feature": feature_description
#         }
#     }

#     response = requests.post(
#         N8N_WEBHOOK_URL,
#         json=payload,
#         timeout=600
#     )

#     return response.json()

# def generate_unit_tests_n8n_client(code: str):

#     payload = {
#         "tool": "generate_unit_tests",
#         "input": {
#             "code": code
#         }
#     }

#     response = requests.post(
#         N8N_WEBHOOK_URL,
#         json=payload,
#         timeout=600
#     )

#     return response.json()