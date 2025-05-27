# This script adds the optional feature: Retry loop for low scores,
# and sets up placeholders for UI + feedback capture

import json
from evaluation.automatic_metrics import compute_bleu, compute_rouge
from evaluation.llm_judge import judge_with_llm

THRESHOLD_SCORE = 0.5  # Retry if LLM judge score is below this
MAX_RETRIES = 1  # Limit retries to avoid infinite loops

# Simulate retry by adding '[RETRY]' marker for illustration
def improve_answer(question, old_answer):
    # You can replace this with a real call to OpenAI to regenerate
    return f"[RETRY] {old_answer} with more clarity."

def run_evaluation():
    with open("data/answers.json") as f:
        data = json.load(f)

    results = []
    for item in data:
        q = item["question"]
        a = item["answer"]
        ref = item.get("reference", "")
        attempt = 0

        while attempt <= MAX_RETRIES:
            bleu = compute_bleu(ref, a)
            rouge = compute_rouge(ref, a)
            llm_score = judge_with_llm(q, a)

            if llm_score >= THRESHOLD_SCORE or attempt == MAX_RETRIES:
                break

            print(f"Retrying for ID {item['id']} due to low score: {llm_score}")
            a = improve_answer(q, a)
            attempt += 1

        results.append({
            "id": item["id"],
            "bleu": bleu,
            "rouge": rouge,
            "llm_score": llm_score,
            "final_answer": a,
            "retries": attempt
        })

    with open("results/report.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_evaluation()
