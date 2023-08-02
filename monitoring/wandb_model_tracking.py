# Use weights and biases to track model performance. This exmaple uses a simple classification model. 
import math 
from pathlib import Path 
from types import SimpleNamespace
from tqdm.auto import tqdm
import torch 
import torch.nn as nn 
import torch.nn.functional as F
from torch.optim import Adam 
from utilities import get_dataloaders 

import wandb 

INPUT_SIZE = 3 * 16 * 16
OUTPUT_SIZE = 5
HIDDEN_SIZE = 256
NUM_WORKERS = 2
CLASSES =["hero", "non-hero", "food"]
DATA_DIR = Path("./data/")
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_model(dropout):
    "Simple MLP with Dropouit"
    return nn.Sequential(
        nn.Flatten(),
        nn.Linear(784, 128),
        nn.ReLU(),
        nn.Dropout(dropout),
        nn.Linear(128, 10)
    ).to(DEVICE)

config = SimpleNamespace(
    epochs = 2, 
    batch_size = 128,
    lr = 1e-5,
    dropout = 0.5,
    slice_size = 1000,
    valid_pct = 0.2,
)


def _train_moidel(config):
    "Train a model with a given config"

    wand.init(
        project = "monitor_training",
        config = config,
    )

    