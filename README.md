Fast_API project

1) Get this project from Github
2) Install PostgreSQL and create your user and database
3) Change EXAMPLE.env to .env file, fill it with your parameters
4) pip install --user pipenv
5) pipenv shell
6) pipenv install --ignore-pipfile # Install the requirements
7) python create_db.py  # create tables in your DB
8) python main.py # Run an app, every time you restart the server the tables in the database are cleared