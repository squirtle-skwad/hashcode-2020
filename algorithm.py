
def run_algo(scores, L, d):
  # id, score
  scores_sorted = sorted(enumerate(scores), key=lambda e: e[1], reverse=True)

  print(f"scores = {scores}")
  print(f"scores_sorted = {scores_sorted}")
  print(f"deadline d = {d}")

  import json
  print(f"libraries L = {json.dumps(L, indent=2)}")
