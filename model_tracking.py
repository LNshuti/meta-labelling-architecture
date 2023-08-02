import wandb, random
from sklearn import linear_model

def monitor_training_with_wandb():
  # initialize W&B
  wandb.init(
    project="meta-labelling-strategy",
    config={
      "learning_rate": 0.02,
      "architecture": "CNN",
    }
  )

  # Do your training and log the results to W&B
  lm = linear_model.LinearRegression()
  lm.fit([[random.random()], [random.random()]], [random.random(), random.random()])
  wandb.log({"acc": 0.5, "loss": 0.2})
  wandb.finish()
  return lm

# And run the code to make sure it works
monitor_training_with_wandb()