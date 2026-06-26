import json
import csv

# Load the Reddit JSON file
with open("reddit_comments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

def collect_comments(children):
    for child in children:
        if child.get("kind") != "t1":
            continue

        body = child["data"].get("body", "").strip()

        if body and body not in ["[deleted]", "[removed]"] and len(body) > 10:
            rows.append([body, "", ""])

        replies = child["data"].get("replies")
        if isinstance(replies, dict):
            collect_comments(replies["data"]["children"])

# Reddit thread JSON:
# data[0] = post
# data[1] = comments
comments = data[1]["data"]["children"]
collect_comments(comments)

with open("takemeter_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label", "notes"])
    writer.writerows(rows)

print(f"Done! Saved {len(rows)} comments.")