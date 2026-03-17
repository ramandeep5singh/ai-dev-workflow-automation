import requests

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/ai-dev-workflow"


def generate_tasks(feature_description: str):

    payload = {
        "action": "generate_feature_tasks",
        "data": {
            "feature": feature_description
        }
    }

    response = requests.post(
        N8N_WEBHOOK_URL,
        json=payload,
        timeout=600
    )

    return response.json()

def generate_unit_tests_n8n_client(code: str):

    payload = {
        "action": "generate_unit_tests",
        "data": {
            "code": code
        }
    }

    response = requests.post(
        N8N_WEBHOOK_URL,
        json=payload,
        timeout=600
    )

    return response.json()