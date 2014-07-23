djng
====

Kick-start your Django and AngularJS based web applications in minutes.
Your project will be deployed on Heroku so you can focus on building apps and not infrastructure.

The project provides a minimal set of useful libraries to get you started as quickly as possible. Specific topics are covered by [recipes](https://github.com/djng/djng/wiki).

What you get:

 * Django backend providing a [REST API](http://www.django-rest-framework.org/).
 * AngularJS client including [Restangular](https://github.com/mgonto/restangular) and [UI Router](http://angular-ui.github.io/ui-router/site/#/api/ui.router).
 * Architecture following the [the twelve-factor app methodology](http://12factor.net/).
 * Configured Heroku environment including logging and monitoring.

Prerequisites
-------------

 * Installed [Python](http://python.org/) and [Virtualenv](http://pypi.python.org/pypi/virtualenv) in a unix-style environment. See this [guide](http://install.python-guide.org/) for guidance.
 * An installed version of [Postgres](http://www.postgresql.org/) to test locally. Also create a user and database for your project.
 * Installed [Node.js](http://nodejs.org/).
 * Installed [Grunt](http://gruntjs.com/getting-started) and [Bower](http://bower.io/#install-bower).
 * Installed [Heroku Toolbelt](https://toolbelt.heroku.com/).
 * A Heroku user account. [Signup is free and instant](https://signup.heroku.com/signup/dc).

Bootstrap your project
----------------------

	mkdir myproject && cd $_
    wget -qO- https://github.com/djng/djng-init/raw/master/djng.sh | bash
    
_Make sure you like what's inside [djng.sh](https://github.com/djng/djng-init/raw/master/djng.sh)._

Developing
----------
Run the django development server:

    source venv/bin/activate
    cd server
    python manage.py runserver_plus

Watch for changes in your client:

    cd client
    grunt watch

Deploying
---------
Build your client:

    cd client
    grunt build
    
Add files, commit all your changes and push to heroku:
 
    git add .
    git commit -m 'your changes'
    git push heroku master
