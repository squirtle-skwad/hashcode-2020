from preprocess import load_data
from algorithm import run_algo
from write_output import write_to_output_file

INPUT_FILE = './data/e.txt'

if __name__ == "__main__":
  scores, L, d = load_data(INPUT_FILE)
  write_to_output_file(run_algo(scores, L, d))
