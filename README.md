# Azubi TMP Assignment: API for Product List & Shopping Cart 

This is a backend API that supports a frontend application for a responsive product list with shopping cart functionality.
This project was built as part of a test for the [Azubi Talent Mobility Program(TMP)](https://www.azubiafrica.org/talent-program)

View the requirements here:

- [TMP Software Engineer Test (Assignment 2)](https://www.azubiafrica.org/software-assessment)

## Running the app

To run the app first clone the repository and then follow the steps below:
- cd into the project directory `cd TMP_Backend_Project`

- Setup venv `python -m venv .venv`

- Activate venv `source .venv/bin/activate` [For Linux or any Posix] OR `.venv\Scripts\activate` [For Windows]

- Install required packages `pip install -r requirements.txt`

- Create a .env file and set the enviroment variables as shown in the **.env_example** file. P.S. remove the curly brackets when filling in your personal environment variables

- Run `flask --app app run --debug` to start the application in debug mode


If successfully run, the API should be accessible locally via [http://localhost:5000/apidocs](http://localhost:5000/apidocs)


## Running the tests
- Activate venv `source .venv/bin/activate` [For Linux or any Posix] OR `.venv\Scripts\activate` [For Windows]

- Install required packages `pip install -r requirements.txt`

- Run `pytest` to run all the tests

- Or run all the tests in a single file. E.g. `pytest tests/test_products.py`

- Or run a single test. E.g. `pytest tests/test_products.py::test_get_products`

## Viewing the deployed app

The API is not yet deployed.


Last README.md Update: `08.12.2024`