# PWP SPRING 2021
# Lines API
# Group information
* Student 1. Sami Harju sami.harju@gmail.com
* Student 2. Teemu Hannnula thannula@gmail.com
* Student 3. Tuukka Veteli tuukkaveteli@gmail.com

__Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint and instructions on how to setup and run the client__

# Initial help stuff

__These instructions were made for Ubuntu 20.04 running Python 3.8.5.__   
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
4. Run tests
    ```bash
    ./test.sh
    ```
5. Start application
    ```bash
    ./run.sh
    ```
