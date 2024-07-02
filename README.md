PROJECT NAME:
Django Band Website


PROJECT DESCRIPTION:
This is an unofficial website for the band The Rolling Stones


PROJECT CONTENTS:
1. BandApp - Main app for website
2. myCapstone - settings and app urls
3. docs - Sphinx documentation

INSTALLATION:
1. Clone the repository from Github
   - git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY (in your command line)

2. Install requirements
   - pip install -r requirements.txt
  
3. Apply database migrations
   - cd myCapstone
   - python manage.py migrate
   - python manage.py makemigrations BandApp
   - python manage.py sqlmigrate BandApp 0001
   - python manage.py migrate
  
4. Create superuser and start server
   - python manage.py createsuperuser
   - python manage.py runserver


USE:
- Clicking on the server link will take you to the sign in page where you can sign in with your superuser account or create a new account
- You will then be free to explore the website with the links at the top of the page


CREDIT:
Kai swanepoel
HyperionDev
