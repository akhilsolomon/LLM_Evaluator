import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from evaluation.automatic_metrics import compute_bleu, compute_rouge
from evaluation.llm_judge import judge_with_llm

def run_evaluation():
    with open("data/answers.json") as f:
        data = json.load(f)

    results = []
    for item in data:
        q = item["question"]
        a = item["answer"]
        ref = item.get("reference", "")

        bleu = compute_bleu(ref, a)
        rouge = compute_rouge(ref, a)
        llm_score = judge_with_llm(q, a)

        results.append({
            "id": item["id"],
            "bleu": bleu,
            "rouge": rouge,
            "llm_score": llm_score
        })

    with open("results/report.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_evaluation()
