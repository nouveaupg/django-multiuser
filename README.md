# django-multiuser
Basic Python3/Django 2.1 project to take care of user self management

One of the best things about Django is that it includes a lot of thankless programming tasks required by almost every type of app these days. (Even Adobe and AutoDesk want you to log into their desktop app!)

This is an ongoing project to provide basic views on the Django Project layer to allow users to self manage users in the fashion that is done almost automatically by the django.admin model.

## Usage
1. Clone django-multiuser
2. Create virtualenv in the cloned directory with manage.py '''python3 -m venv venv'''
3. '''> . venv/bin/activate'''
4. '''> (venv) pip install django'''
5. '''> (venv) python3 manage.py migrate'''
6. '''> (venv) python3 manage.py createsuperuser'''
7. '''> (venv) python3 manage.py collectstatic'''
8. '''> (venv) python3 manage.py runserver 8000'''
9. Using a web browser, attempt to load http://localhost:8000, you should see a basic interface for an end user to create an account, login, or reset their password. If not something has gone wrong, e-mail me at nouveau.pg@gmail.com or rapidiphonedev@gmail.com.
10. To further test the setup, try creating a test user.
11. Using the information you gave when creating the superuser, login to http://localhost:800/admin and see if the user is in the user table.
12. '''> (venv) python3 manage.py createapplication <yourapp>'''

This application will contain all of your views, etc. All of the end user management functions are handled by the Project layer (the same level as the admin panel -- the code only creates standard Django user objects)

The CSS namespaces are aggressively namespaced to avoid conflict with your own CSS.

A version of jQuery UI is included to help with form validation. It is in /static/jquery. If you have a preferred solution for your project, this can be replaced. Templates are provided with inheritence and comments to help you customize for your specific application.


13. **Get your POC running even quicker than with Django alone**
