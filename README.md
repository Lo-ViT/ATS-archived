# Set up project

For setup on your local computer, see [README.LOCAL.md](README.LOCAL.md).

For setup on university's cluster, see [README.CLUSTER.md](README.CLUSTER.md).

Click [here](README.md) for the original README.md.

# Set up wandb

On the terminal, login once with your API key

```
wandb login
```

### Turn of wandb

Sometimes, you don't want to run WandB's logging. To disable wandb, add `--nowandb` when run `tools.run_net`.

# Start new experiment

Open new branch if you want to edit code and start new experiment.

A good practice is change only one parameter at once and study how this one change effects the performance. An exception is, you know what you are doing, and you want to change multiple parameters at once to get a new method run.

If you want to try multiple values for a same parameter, it's okay to stay in the same branch.

### Create a new branch

If you want to start a new experiment:

- from scratch, start from the `main` branch

```bash
git switch main
```

- from another parent experiment, switch to the parent experiment

```bash
git switch experiment<parent-nr>
```

Either way, go after that to the Google Sheet, get yourself a number for the new experiment and create a new branch for the child experiment

```bash
git branch experiment<nr>
git switch experiment<nr>
```

### Create new/Edit current configuration file

If you want to:
- create a new experiment from scratch, create in `libs.config` your new configuration, name it `experiment<nr>.py`. 
- change some parameters with respect to some existing parent experiment, just edit `experiment<parent-nr>.py` in the child branch.

Following this routine strictly we can make the experiments more reproducible.

### Start the training

The training can be started as 

```bash
python3 -m tools.run_net --do train --custom_config libs.config.experiment<nr>
```

### Evaluate the model's accuracy

```bash
python3 -m tools.run_net --do test --custom_config libs.config.experiment<nr>
```
### Evaluate the model's FLOPs

TODO

# Contribute useful code to `main`

We can follow the basic workflow: 
- create a GitHub Issue.
- create a new branch from main.
- create a PR for the change and get approval from another teammate.

Keep the PR minimal and readable. Try to change the original paper's repository as little as possible.