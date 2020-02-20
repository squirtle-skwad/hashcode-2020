from preprocess import load_data
from algorithm import run_algo

INPUT_FILE = './data/a.txt'

if __name__ == "__main__":
  scores, L, d = load_data(INPUT_FILE)
  run_algo(scores, L, d)
