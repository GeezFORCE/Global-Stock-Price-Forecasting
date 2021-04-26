# Mini Project

[![Made With Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Creative Commons](http://ForTheBadge.com/images/badges/cc-0.svg)](https://creativecommons.org/share-your-work/public-domain/cc0/)

[![Deploy Docker to Heroku](https://github.com/GeezFORCE/MainProject/workflows/Build%20Docker%20image%20and%20deploy%20to%20Heroku/badge.svg)](https://github.com/GeezFORCE/MainProject/workflows)


![Heroku Deploy Status](https://pyheroku-badge.herokuapp.com/?app=gsppp&style=flat)
[![Heroku App Status](https://heroku-shields.herokuapp.com/gsppp)](https://gsppp.herokuapp.com)

## To Get Started

### Install Packages

`pip install -r requirements.txt`

### Setting Up Tensorboard

- In a seperate terminal, intialize the conda virtual environment created for the project.
- In the project directory create a new folder named `logs`
- Type the command `tensorboard --logdir=logs\`
- Open a browser window and paste `http://localhost:6006/`

### Changing requirements.txt

- Run `pip install pipreqs`
- Run `pipreqs <path> --force`

### Google Colab Implementation

[![Keras Tuner](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1UqJFzvPrLxoE2AeeuRV-TytVdM0xNLU_?usp=sharing)

### To run UI

- Navigate to Project Folder
- Run the command `streamlit run app.py`
- Open `http://localhost:8501/`

### UI Tree

```
.
├── Ticker Symbol
└── Main Navigation
    ├── Overview
    │   ├── Company Overview
    │   ├── Financials
    │   └── Open, Close Charts
    ├── Train
    │   ├── Ticker Set
    │   ├── Data Parameters
    │   │   ├── Period
    │   │   ├── Training Parameters
    │   │   ├── Epochs
    │   │   ├── Batch Size
    │   │   ├── Validation Set Percentage
    │   │   └── Learning Rate
    │   ├── Model Parameters
    │   │   ├── Number of LSTM Units
    │   │   ├── Number of Dense Units
    │   │   ├── Number of Bidirectional Layers
    │   │   ├── Number of Dense Layers
    │   │   ├── Dropoutrate
    │   │   └── Return Sequences
    │   └── Train Button
    ├── Predict
    │   ├── Interval
    │   └── Predict Button
    ├── Sentimental Analysis
    │   ├── Scores
    │   │   ├── Ticker Set
    │   │   └── Analyze
    │   ├── Finviz
    │   ├── Twitter
    │   ├── !Reddit
    │   └── Stocktwits
    └── About

```
