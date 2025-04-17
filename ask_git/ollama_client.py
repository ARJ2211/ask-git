import requests

def send_to_ollama(prompt: str, model: str = "codellama") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    if response.status_code != 200:
        raise RuntimeError(f"Ollama error: {response.status_code} - {response.text}")

    return response.json().get("response", "").strip()
