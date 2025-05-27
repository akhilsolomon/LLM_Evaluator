# evaluation/llm_judge.py

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def judge_with_llm(question, answer):
    prompt = f"""You are a strict evaluator for an internal assistant.
Question: {question}
Answer: {answer}

Score the answer from 1 (poor) to 5 (excellent) based on clarity, usefulness, and actionability. Reply only with the number.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        score = response['choices'][0]['message']['content'].strip()
        return int(score)
    except Exception as e:
        print("LLM scoring failed:", e)
        return -1
