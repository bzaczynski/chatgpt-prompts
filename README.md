# ChatGPT Prompts

This is an experimental project that leverages [OpenAI API](https://platform.openai.com/docs/api-reference?lang=python) to generate text based on a predefined prompt.

## Setup

Make a `.env` file with the following variables:

```
OPENAI_API_KEY=<your-secret-api-key>
ORGANIZATION_ID=<your-organization-id>
```

You can view and manage your [API keys](https://platform.openai.com/account/api-keys) and check your [organization ID](https://platform.openai.com/account/org-settings) in the account settings.

## Install

```
(venv) $ python -m pip install -r requirements.txt -c constraints.txt
```

## Usage

```
(venv) $ python review.py
```
