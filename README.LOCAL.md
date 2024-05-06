# Set up repository locally

Clone project

```bash
git clone git@github.com:LongHoangNguyen06/Efficient-Transformer.git
```

# Local installation

Create conda environment

```bash
conda env create -f environment.yml --name efficient-transformer
```

Activate Conda environment

```bash
conda activate efficient-transformer
```

# Set up VSCode

Open the directory with VSCode. `Ctrl + Shift + P`, select interpreter, choose `efficient-transformer`. 

To debug the training process, click on `Run &  Debug`, choose `Debug Train`.

Take a look at `.vscode/launch.json` to change the run parameters of your process.

# Set up TinyImageNet

Create a local directory, download and unzip the data

```bash
mkdir ~/efficient-transformer-data
cd ~/efficient-transformer-data
wget http://cs231n.stanford.edu/tiny-imagenet-200.zip
unzip -qq 'tiny-imagenet-200.zip'
```