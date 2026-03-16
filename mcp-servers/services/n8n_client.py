import requests

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/generate-feature-tasks"

def generate_tasks(feature_description: str):

    payload = {
        "input_data": feature_description
    }

    response = requests.post(
        N8N_WEBHOOK_URL,
        json=payload,
        timeout=600
    )

    return response.json()