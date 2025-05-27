import json

def store_feedback(answer_id, thumbs, comment):
    feedback = {"id": answer_id, "thumbs": thumbs, "comment": comment}
    with open("data/user_feedback.json", "a") as f:
        json.dump(feedback, f)
        f.write("\n")
