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
