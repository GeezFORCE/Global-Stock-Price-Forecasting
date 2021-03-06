<h1 align="center"> 
    Global Stock Price Forecasting📈 
</h1>
<p align="center">
    <a href="https://github.com/GeezFORCE/MainProject/workflows">
        <img src="https://github.com/GeezFORCE/MainProject/workflows/Build%20Docker%20image%20and%20deploy%20to%20Heroku/badge.svg" alt="Deploy Docker to Heroku">
    </a>
    <a href="https://gsppp.herokuapp.com">
        <img src="https://pyheroku-badge.herokuapp.com/?app=gsppp&style=flat" alt="Heroku Deploy Status">
    </a>
</p>

An attempt to predict stock prices of selected tickers using models trained on historical prices
of similar stocks irrespective of market of trade.

![Overview and Train Page](Screenshot.png)

## Web App

- The application is available as a web app at [Global Stock Price Forecasting](https://gsppp.herokuapp.com)
- Please wait and reload if the website is not reachable

## Local Installation

- If you want to run it locally you'll need [Git](https://git-scm.com/) and [Pip](https://pypi.org/project/pip/) installed.
- Run the following commands from the command line

```
# Clone the repository
git clone https://github.com/GeezFORCE/MainProject.git

# Go into the repository
cd MainProject

# Install Dependencies
pip3 install -r requirements.txt

# Run the application
streamlit run app.py
```

- You can also use docker
