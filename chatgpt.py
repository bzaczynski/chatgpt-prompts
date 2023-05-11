import os
from pathlib import Path
from functools import cache

import dotenv
import openai
import yaml

dotenv.load_dotenv()
openai.organization = os.getenv("ORGANIZATION_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

TEMPLATE_FILE = Path("templates.yml")


@cache
def load_templates(path: Path = TEMPLATE_FILE) -> dict[str, str]:
    with path.open(encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_available_models() -> list[str]:
    return sorted(model.id for model in openai.Model.list().data)


def chat(prompt: str, temperature: float = 0, model: str = "gpt-4") -> str:
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
    )
    return completion.choices[0].message.content
