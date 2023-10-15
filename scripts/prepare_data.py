import os
import subprocess
import argparse
from pathlib import Path

from tqdm.auto import tqdm

import image_to_latex.data.utils as utils
from image_to_latex.data.utils import Tokenizer, get_all_formulas, get_split

# opening config file
parser = argparse.ArgumentParser()
parser.add_argument(
    "--images_folder_name",
    help="images folder name in data folder",
    default="images_processed",
)
parser.add_argument(
    "--equations_file_name",
    help="equations file name in the data folder",
    default="im2latex.lst",
)
parser.add_argument(
    "--data_path",
    help="path where all the data is stored",
    default="/home/gauravs/data/resnet_xfmer",
)

args = parser.parse_args()

DATA_DIRNAME = args.data_path
PROCESSED_IMAGES_DIRNAME = f"{DATA_DIRNAME}/{args.images_folder_name}"
VOCAB_FILE = f"{DATA_DIRNAME}/vocab.json"
CLEANED_FILE = f"{args.equations_file_name}"


def main():

    os.chdir(DATA_DIRNAME)

    # Build vocabulary
    print("Building vocabulary...")
    all_formulas = get_all_formulas(CLEANED_FILE)
    _, train_formulas = get_split(all_formulas, f"{DATA_DIRNAME}/train.lst")
    tokenizer = Tokenizer()
    tokenizer.train(train_formulas)
    tokenizer.save(VOCAB_FILE)
    print("Done!")


if __name__ == "__main__":
    main()
