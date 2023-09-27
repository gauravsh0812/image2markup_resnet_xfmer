# Image to LaTeX

An application that maps an image of a LaTeX math equation to LaTeX code.

This is a fork that works exactly like the original, but updated to work with Python 3.10 since the original repo is no longer maintained and newer GPUs require newer Lightning versions. This also fixes [a longstanding issue on the original repo related to using an older Python version](https://github.com/kingyiusuen/image-to-latex/issues/20). In fact, since I moved everything to Conda and a bash script, the experience should be much smoother than the original repo.

I did, however, get rid of the api, streamlit and docker since I didn't need them.

## Results

- My Best Run: https://wandb.ai/ternary-operators/image-to-latex/runs/0j8ke3m8
- Run Path: `ternary-operators/image-to-latex/0j8ke3m8`

## How To Use

### Prerequisites

Miniconda: https://docs.conda.io/en/latest/miniconda.html

### Setup

Clone the repository to your computer and position your command line inside the repository folder:

```
git clone https://github.com/kingyiusuen/image-to-latex.git
cd image-to-latex
```

Assuming you have Miniconda installed, run the following command to install the required packages:

```
./install
```

The install script will create and install the required packages in a virtual environment named `img2latex-env` that uses Python 3.10.

But, bash scripts create a new shell, so you will need to run the following command to activate the environment again before running of the scripts:

```
conda activate img2latex-env
```

### Using and/or Testing

To use or test the model, you may use either my best run or your own run. Follow the instructions below to use my best run (replace my best run path with your own run path if you want to use your own run):

```bash
# Download the best model checkpoint from W&B
python3 scripts/download_checkpoint.py ternary-operators/image-to-latex/0j8ke3m8

# Run the model on an image
python3 scripts/test.py --image_path data/test/images/abcd.png
```

The results will be printed to the console.

### Training

#### Data Preparation

Run the following command to download and preprocess the data:

```

python3 scripts/prepare_data.py

```

This will:

- Download the data to `data`.
- Apply some preprocessing to normalize the LaTeX (in addition to the normalization applied by the original data owners)
- Apply some preprocessing to normalize the images (in addition to the normalization applied by the original data owners). This involves making them greyscale, padding them and skipping the ones with no text.

#### Actual Training

Run the following command to train the model:

```

python3 scripts/train.py

```

You can update the training configuration by editing `conf/config.yaml`. The default configuration is the one used to train the best model.

#### Experiment Tracking using Weights & Biases

The best model checkpoint will be uploaded to [Weights & Biases (W&B)](https://wandb.ai/) automatically (you will be asked to register or login to W&B before the training starts).

You can download the best model checkpoint from W&B using the following command:

```

python3 scripts/download_checkpoint.py RUN_PATH

```

Replace RUN_PATH with the path of your run (ex `ternary-operators/image-to-latex/0j8ke3m8`).
