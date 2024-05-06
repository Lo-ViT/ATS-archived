# Table of content

- [Table of content](#table-of-content)
- [Set up project](#set-up-project)
- [Set up wandb](#set-up-wandb)
    - [Turn off wandb](#turn-off-wandb)
- [Test your setup](#test-your-setup)
- [Start new experiment](#start-new-experiment)
    - [Create a new branch](#create-a-new-branch)
    - [Create new/Edit current configuration file](#create-newedit-current-configuration-file)
    - [Start the training](#start-the-training)
    - [Evaluate the model's test accuracy](#evaluate-the-models-test-accuracy)
    - [Evaluate the model's test GFLOPs](#evaluate-the-models-test-gflops)
- [Contribute useful code to `main`](#contribute-useful-code-to-main)

# Set up project

For setup on your local computer, see [README.LOCAL.md](README.LOCAL.md). It's recommended to have a set up on your local computer for debugging purpose. For fast debug, only use a subset of the data.

For setup on university's cluster, see [README.CLUSTER.md](README.CLUSTER.md).

Click [here](README.md) for the original README.md.

# Set up wandb

On the terminal, login once with your API key

```
wandb login
```

### Turn off wandb

Sometimes, you don't want to run WandB's logging. To disable wandb, add `--nowandb` when run `tools.run_net`.

# Test your setup

If you did everything correctly, the training can be started easily as 

```bash
python3 -m tools.run_net --do train --custom_config libs.config.experiment0004
```

# Start new experiment

Open new branch if you want to edit code and start new experiment. A good practice is change only one parameter at once and study how this one change effects the performance. You don't need to follow this practice at all, however it's recommended.

When experimenting, it's also recommended to write down the results of each experiment. We document the progresses of everything with this sheet:

https://docs.google.com/spreadsheets/d/17NxbCdiB3WSJX_AVapdG8elrmUOYYIMxNQwbM1Xr_tA

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

### Evaluate the model's test accuracy

```bash
python3 -m tools.run_net --do test --custom_config libs.config.experiment<nr>
```
### Evaluate the model's test GFLOPs

TODO

# Contribute useful code to `main`

Code for an individual experiment should not be merged back to main. If you want to contribute an useful code that you think could be beneficial for up-coming experiments, we follow the basic workflow: 
- create a GitHub Issue.
- create a new branch from main.
- create a PR for the change and get approval from another teammate.

Keep the PR minimal and readable. Try to change the original paper's repository as little as possible.