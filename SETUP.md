# Setup for local runs

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

### To run UI

- Navigate to Project Folder
- Run the command `streamlit run app.py`
- Open `http://localhost:8501/`