from preprocess import load_data
from algorithm import run_algo
from write_output import write_to_output_file

INPUT_FILE = './data/f.txt'
OUTPUT_FILE = 'output_f'

if __name__ == "__main__":
  scores, L, d = load_data(INPUT_FILE)
  # print(L)
  write_to_output_file(run_algo(scores, L, d), OUTPUT_FILE)
