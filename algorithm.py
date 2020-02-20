
def run_algo(scores, L, d):
  """
    scores: list of scores, where index is book id
    L: list of dicts, having properties of libraries
    d: int, deadline
  """

  # This is list of (id, score), whereas scores is list of score only
  scores_sorted = sorted(enumerate(scores), key=lambda e: e[1], reverse=True)

  print(f"scores = {scores}")
  print(f"scores_sorted = {scores_sorted}")
  print(f"deadline d = {d}")

  import json
  print(f"libraries L = {json.dumps(L, indent=2)}")
