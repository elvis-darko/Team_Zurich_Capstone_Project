## PROJECT DESCRIPTION
This project is for an African telecommunications company that provides customers with airtime and mobile data bundles. The objective of this project is to develop a machine learning model to predict the likelihood of each customer “churning,” i.e. becoming inactive and not making any transactions for 90 days.

This solution will help this telecom company to better serve their customers by understanding which customers are at risk of leaving

## SUMMARY
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------|:------|
|CP         | CUSTOMER CHURN PREDICTION  |           | STREAMLIT<br />FAST API|





## SETUP
It is recommended to have Virtual Studio Code or any other standard code editor on your local machine.<br />Install the required packages locally to your computer.

It is recommended that you run a python version above 3.0. 
You can download the required python version from [here](https://www.python.org/downloads/).

Use these recommended steps to set up your local machine for this project:

1. **Create the Python's virtual environment :** <br />This will isolate the required libraries of the project to avoid conflicts.<br />Choose any of the line of code that will work on your local machine.

            python3 -m venv venv
            python -m venv venv


2. **Activate the Python's virtual environment :**<br />This will ensure that the Python kernel & libraries will be those of the created isolated environment.

            - for windows : 
                         venv\Scripts\activate

            - for Linux & MacOS :
                         source venv/bin/activate


3. **Upgrade Pip :**<br />Pip is the installed libraries/packages manager. Upgrading Pip will give an to up-to-date version that will work correctly.

            python -m pip install --upgrade pip


4. **Install the required libraries/packages :**<br />There are libraries and packages that are required for this project. These libraries and packages are listed in the `requirements.txt` file.<br />The text file will allow you to import these libraries and packages into the python's scripts and notebooks without any issue.

            python -m pip install -r requirements.txt 



## EVALUATION
The evaluation metric for this challenge is Area Under the Curve (AUC).

The values can be between 0 and 1, inclusive. Where 1 indicates the customer churned and 0 indicates the customer stayed with Expresso.

Your submission should look like:

            user_id                                      CHURN
            00001dbe00e56fc4b1c1b65dda63de2a5ece55f9      0.98
            000055d41c8a62052dd426592e8a4a3342bf565d      0.12
            000081dd3245e6869a4a9c574c7050e7bb84c2c8      0.37


## CONTRIBUTORS
| NAME  |   COUNTRY |   E-MAIL  |
|:------|:----------|:----------|
|ELVIS DARKO|GHANA|elvis_darko@outlook.com|
|FAITH BERIDA|NIGERIA|  |
|RICHMOND E.Y. ABAKE|GHANA|  |
|RICHMOND TETTEH| GHANA|    |
|JOSEPH GIKUBU|     |   |
|MARIE GRACE KAGAJU |   |   |