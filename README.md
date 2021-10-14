# treasure_hunt
A web application for conducting online treasurehunts.

## Setup for local environment
Clone the repository using the command 
```
   git clone https://github.com/navaneeth-krishna/treasure_hunt.git
```

### Creating a python virtual environment
Create a virtual environment "test" using the following commands
```
   pip install virtualenvwrapper-win
   mkvirtualenv test
```
This should take you to the virtual environment directly after creating it. If you need to run the virtual environment in the future, run the following command:
```
   workon test
```

### Installing Django in the virtual environment
To install django in the virtual environment, first make sure you are in the virtual enviroment. Then, run the command:
```
   pip install django
```
To check whether Django has been correctly installed, run the following command. If it does return an output, you are all set!
```
   django-admin --version
```
Now install all the dependencies/requirements for the application to run from the requirements.txt file. Run the command
```
   pip install -r requirements.txt
```
Run the following command to setup the database.
```
   python manage.py migrate
```
Run the command to create a admin user for the application and give a username and password to create it.
```
   python manage.py createsuperuser
```
Take a look at the `.env` file in the root directory and adjust the time and date to suit your conditions.
  
- **CHECK_DATE** is the date and time after which the clues will be displayed to the users before which a countdown is displayed to the users till the date and time is reached.
- **DEADLINE_DATE** is the date and time after which the treasure hunt ends. 

### Running the application
Run the command to start the application on the local server.
```
   python manage.py runserver
```
### Onboarding to the admin panel of the application
Do these for proper running of the application at the first time run. As well as get a feel of the admin panel
* login using the super user username and password.
* Append "/admin" to the root url and viola! You are at the admin panel.
* Go to clues link and add one clue so that the user sees atleast a clue as well as for proper running of the application.
* You can manage users, usersprofile at the admin panel. Add more clues. Add descriptive questions. See the users who won the treasure hunt.
