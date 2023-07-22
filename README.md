Sample Django Rest Framework with PostgreSQL App Setup Guide
This is a sample Django Rest Framework (DRF) project built with PostgreSQL. To run this server on your machine, follow the steps below:

Install Python:

Make sure you have Python version 3.5 or above installed. If you don't have it, you can download it from the official Python website: https://www.python.org/downloads/
Install Required Packages:

Open a terminal or command prompt and navigate to the project directory.
Run the following command to download all the required packages for the project:

python -m pip install -r requirements.txt
Install PostgreSQL and Create a Database:

Install PostgreSQL on your machine by following the instructions provided in the official PostgreSQL download page: https://www.postgresql.org/download/
Once PostgreSQL is installed, create a new database as explained in this tutorial: https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e
Update Database Configuration:

Navigate to the app/settings.py file in your project.
Replace the database name and password with the ones you created in the PostgreSQL setup.
Migrate the Database:

In the terminal or command prompt, run the following command to apply the database migrations:

python manage.py migrate
Start the Server:

To launch the server, run the following command:

python manage.py runserver

To run all unit test cases written in the YAML file, execute the following command:

pytest --execute-all=true
Postman API Collection:

For a sample request collection, you can use the following Postman collection link:
https://api.postman.com/collections/9401503-cdfb4aca-57e2-46a8-bb78-96bd50c2b79d?access_key=PMAT-01H5Z8C9HAYJ8ZFG35RA93BTYJ
Alternatively, you can import the collection from the collection.json file provided in the project.
Now you should have the Django Rest Framework server up and running, ready to handle your requests!





Regenerate response
