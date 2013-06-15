tripping
========

Site uptime monitoring script, heroku deployable.


Instructions for heroku:

Edit tripping.py to match your details. SMSing is not implemented, but I use an SMS email address provided by my provider in the form of 1234567890@text.att.net

Set the environment variables for the email server:

    heroku config:set EMAIL\_SERVER:smtp.gmail.com:587

    heroku config:set EMAIL\_ADDRESS:sejje@sejje.net

    heroku config:set EMAIL\_PASSWORD:correct-horse-battery-staple


Deploy to heroku:

    git push heroku master

Start the process:
    heroku scale:ps worker=1
