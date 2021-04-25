[![codecov](https://codecov.io/gh/samharju/PWP/branch/master/graph/badge.svg?token=6RCP3VWOJJ)](https://codecov.io/gh/samharju/PWP)
[![CI](https://github.com/samharju/PWP/actions/workflows/main.yml/badge.svg)](https://github.com/samharju/PWP/actions/workflows/main.yml)
# PWP SPRING 2021
# Lines API
# Group information
* Student 1. Sami Harju sami.harju@gmail.com
* Student 2. Teemu Hannnula thannula@gmail.com
* Student 3. Tuukka Veteli tuukkaveteli@gmail.com

__Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint and instructions on how to setup and run the client__

# Initial help stuff

__These instructions were made for Ubuntu 20.04 running Python 3.9.__   
1. Create a virtual environment (optional)
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
   
2. Install dependencies.
    ```bash
    ./install.sh
    ```
3. Initialize database or apply new migrations
    ```bash
    ./migrate.sh
    ```
4. Run only database tests
    ```bash
    pytest -v -m models
    ```
5. Run all tests and check code syntax
    ```bash
    ./test.sh
    ```
6. Start application
    ```bash
    ./run.sh
    ```
7. Find api entrypoint with a client of your choice
    
    [http://localhost:8000/api/](http://localhost:8000/api/)
    
