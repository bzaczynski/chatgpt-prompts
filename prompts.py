from chatgpt import chat, load_templates


def apply_review_feedback(fragment: str, feedback: str,temperature: float) -> str:
    template = load_templates()["review"]
    prompt = template.format(fragment=fragment, feedback=feedback)
    return chat(prompt, temperature)
