# Mini Project

[![Made With Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Creative Commons](http://ForTheBadge.com/images/badges/cc-0.svg)](https://creativecommons.org/share-your-work/public-domain/cc0/)

[![Website](https://img.shields.io/badge/Open-WebApp-red)](https://gspp-mainproject.herokuapp.com/)

[![Generic badge](https://img.shields.io/badge/Tensorflow-2.4.1-orange.svg)](https://www.tensorflow.org/learn)
[![Generic badge](https://img.shields.io/badge/Joblib-1.0.1-cyan.svg)](https://joblib.readthedocs.io/en/latest/)
[![Generic badge](https://img.shields.io/badge/Pandas-1.2.3-darkblue.svg)](https://pandas.pydata.org/)
[![Generic badge](https://img.shields.io/badge/Matplotlib-3.3.4-yellow.svg)](https://matplotlib.org/)
[![Generic badge](https://img.shields.io/badge/Keras_Tuner-1.0.2-green.svg)](https://keras-team.github.io/keras-tuner/)
[![Generic badge](https://img.shields.io/badge/py_currency_converter-1.0.2-blue.svg)](https://pypi.org/project/py-currency-converter/)
[![Generic badge](https://img.shields.io/badge/yfinance-0.1.55-red.svg)](https://pypi.org/project/yfinance/)
[![Generic badge](https://img.shields.io/badge/numpy-1.19.5-violet.svg)](https://numpy.org/doc/stable/)
[![Generic badge](https://img.shields.io/badge/scikit_learn-0.24.1-maroon.svg)](https://scikit-learn.org/stable/)
[![Generic badge](https://img.shields.io/badge/nltk-3.6.1-darkgreen.svg)](https://pypi.org/project/beautifulsoup4/)
[![Generic badge](https://img.shields.io/badge/beautifulsoup-4.9.3-brown.svg)](https://pypi.org/project/beautifulsoup4)

[![Maintaner](https://img.shields.io/badge/maintainer-GeezFORCE-red)](https://gitlab.com/GeezFORCE)
[![Maintaner](https://img.shields.io/badge/maintainer-cjalvin24-yellow)](https://gitlab.com/cjalvin24)
[![Maintaner](https://img.shields.io/badge/maintainer-vaishnavmenon99-brightgreen)](https://gitlab.com/vaishnavmenon99)
[![Maintaner](https://img.shields.io/badge/maintainer-skifobabu123-9cf)](https://gitlab.com/skifobabu123)

## To Get Started

### Environment Setup

- Install Anaconda Navigator , make sure to setup conda properly(with path).

- Create an new virtual environment
  `conda create -n <nameOfEnvironment> python=<version>`

- To activate an environment
  `activate <nameOfEnvironment>`

- To deactivate an environment
  `conda deactivate`

- To install a package, use pip or conda
  `pip install <packageName>`
  `conda install <packageName>`

- To list packages in environment
  `conda list`

### Install Packages

`pip install -r requirements.txt`

### Setting Up Path for importing Modules (Optional)

- Goto `C:\Users\<your_username>\Anaconda3\Lib\site-packages`
- Create a file `Python<versionNo>.pth` , eg: `Python37.pth` for Python 3.7
- Edit the file to include this line `C:\\Users\\<your_username>\\my_module`
- eg; If the Project is present in a folder named Project in Desktop of user A, the file should be `C:\\Users\\A\\Desktop\\Project`

### Setup for saving models

- In the project directory create a folder named `models`, `savedModelInformation`, `saveScaler`, `savedData`.
- The directory `savedModelInformation` must have sub-directories `modelInformation`, `modelWeights`.

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

### Install NLTK for Finviz Sentimental Analysis

- Open a python console, type `python` or execute python interpreter
- Import the module , `import nltk`
- Download Vader using the command, `nltk.download("vader_lexicon")`

### To run UI

- Navigate to `Streamlit`
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

### Issues

- [ ] 🔴 Values in constant not updating in other modules, probably need to scrap constants
- [ ] 🟡 Warning in new version of tensorflow, maybe bug
      WARNING:absl:Found untraced functions such as lstm_cell_1_layer_call_and_return_conditional_losses, lstm_cell_1_layer_call_fn, lstm_cell_2_layer_call_and_return_conditional_losses, lstm_cell_2_layer_call_fn, lstm_cell_1_layer_call_fn while saving (showing 5 of 10). These functions will not be directly callable after loading.
      WARNING:absl:Found untraced functions such as lstm_cell_1_layer_call_and_return_conditional_losses, lstm_cell_1_layer_call_fn, lstm_cell_2_layer_call_and_return_conditional_losses, lstm_cell_2_layer_call_fn, lstm_cell_1_layer_call_fn while saving (showing 5 of 10). These functions will not be directly callable after loading. -- Only in Giridhar's computer , maybe packages?
- [ ] 🟢 Reduce complexity of the Currency Conversion (Optional)
- [ ] 🟢 Warning - Sets are not currently considered sequences, but this may change in the future, so consider avoiding using them.

### Fixed

- [x] ~~🔴 Scaler produces wrong values in inverse transform operation.~~
- [x] ~~🔴 Downloads of data takes a long time, bulk download is highly complex~~
- [x] ~~🔴 Model fails whenever TSLA is used~~
- [x] ~~🔴 Colab NoneType Error~~
- [x] ~~🔴 Both models cannot take into account the age of the companies~~
- [x] ~~🔴 Alt model produces NaN on certain runs~~
- [x] ~~🔴 Preprocess Output issue in Numpy~~
- [x] ~~🔴 Error with LSTM network (may have caused by preprocess correction)~~
- [x] ~~🔴 Validation set is not scaling~~
- [x] ~~🟡 https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy -- Scaler Warning~~
- [x] ~~🟡 Find Hyperparameters to improve, look into various activation function, now using standard functions~~ -- Solved with keras tuner
- [x] ~~🟡 Implement currency conversion for non-USD Stocks~~
- [x] ~~🟡 Saving trainX, trainY, validationX, validationY (optional)~~
- [x] ~~🟡 Prediction flattens in rare occurences (can be replicated with GOOG and AAPL).~~
- [x] ~~🟡 Increasing the complexity of bidirectional LSTMs~~
- [x] ~~🟡 Preprocessor cannot handle small datasets.~~
- [x] ~~🟡 Preprocessor cannot handle validation set (5 percent resulted in error)~~
- [x] ~~🟢 tensorflow 2.4.1 requires h5py~=2.10.0, but you have h5py 3.2.1 which is incompatible, change version when creating requirements.txt~~
- [x] ~~🟢 Attributes for Plot Wrapper~~ -- Scrapped
- [x] ~~🟢 Complexity of datetime Conversion~~ -- Scrapped
