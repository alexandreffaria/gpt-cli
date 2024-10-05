#!/usr/bin/env python3
import os
import openai
import argparse


openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()


def get_response(prompt, model="gpt-4o-mini"):
    gptPrompt = [
        {
            "role": "system",
            "content": "Try to answer in a one-liner, or as close to it as possible:",
        },
        {"role": "user", "content": prompt},
    ]
    try:
        response = client.chat.completions.create(
                model=model,
                messages=gptPrompt,
                max_tokens=100,
                temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a prompt to openai")
    parser.add_argument("prompt", type=str, help="The prompt")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="Model to use")

    args = parser.parse_args()

    result = get_response(args.prompt, args.model)
    print(result)
