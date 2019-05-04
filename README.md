[![Build Status](https://travis-ci.org/Geronimo1992/phot-app-django.svg?branch=master)](https://travis-ci.org/Geronimo1992/phot-app-django)

# Full Stack Django Frameworks Milestone Project
This is a Phototgallery that allows photographers to post their pictures online to download for free by users across the world. 

# UX
The design of the website is simple and it is straight forward how to use it. It is responsive and it has been developed with the end user in mind. The navigation has bg image and the text is white.
The page uses a flexbox grid to align the pictures on the screen, allowing for a clean interface. There is a detail page where a user can donwload the picture and donate a sum to the non profit company if he chooses do to so. On the left upper corner on the detail page, there 
is a little bit of info about the photgrapher. When clicked on it, you get redirected to the profile of that photographer where you can view an intro and his picture. There is a search bar to make navigation easier by searching a certain category of pictures. There is a leader board page where 
visitors can view the most popular photgrpahers ranked in a top thirty listing. 

# Features
* User can add pictures to his personal portfolio on his profile page.
* User can delete pictures he wants to delete.
* User can edit his profile info and reset his password.

Wireframes can be found [here](https://github.com/Geronimo1992/phot-app-django/tree/master/wireframes)

# Techologies Used

* [HTML](https://www.w3schools.com/html/html_intro.asp) has been used for the structure of the page
* [CSS](https://www.w3schools.com/css/) has been used for styling
* [Python](https://www.python.org/) has been used to write the backend code
* [Django](https://www.djangoproject.com/) has been used to facilitate the backend development
* [PostgreSQL](https://www.postgresql.org/) has been used as a database

# Testing

* HTML has been tested on [W3C](https://validator.w3.org/)
* CSS has been tested on [W3C](https://jigsaw.w3.org/css-validator/)
* Python has been tested on [pep8 online check](http://pep8online.com/)
* Testing of every views status code has been done. See  [here](https://github.com/Geronimo1992/phot-app-django)
* Manual tests have been performed as well (checking links, forms, etc)
* Continious integration wiht travis has been added

# deployment
* Code can be found on [Github](https://github.com/Geronimo1992/phot-app-django)
* Website has been deployed and can be found on [Heroku](https://photogallery-milestone-project.herokuapp.com/)

1. Go to Heroku and make an account or sing in if you already have one
2. Click on "new" the right upper corner to create a new app
3. Name your app 
4. Choose Region
5. Go to resources and search for postgresql (if you're using this db)
6. Go to to settings and configurate your environmental variables. These are the variables like your SECRET_KEY in Django that should be kept away from your github. Anything that has to remain secret should be added as an env var, this includes api keys, passwords, database urls and other things
that do not belong on your public repositories.
7. Next go to your Django settings and configure your database.
8. Install Gunicorn by using command sudo pip3 install gunicorn. Go to documentation of gunicorn to learn about it [documentation](https://gunicorn.org/)
9. Install whitenoise (sudo pip3 install whitenoise) which allows you to serve your static files to the server, this is mandatory, see [documentation for more about it](http://whitenoise.evans.io/en/stable/)
10. Install Pillow (sudo pip3 install pillow) which allows you to process media files. [documentation](https://pillow.readthedocs.io/en/stable/)
11. You can use amazon web services if you like to store everything in the cloud. See [documentation](https://docs.aws.amazon.com/s3/?id=docs_gateway) for more about this. [Click here](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html) for a tutorial on how to configurate your settings.py file to host your stqtic files on aws.
12. Once you've installed everything and are ready to go, you can click on deploy in the heroku dashboard and connect your github account. Once everyhting has been loaded you can view your deployed app on heroku.


# Credits

* Many times i refered to the python documentation
* Many times i refered to Django docs
* A big thank you to my mentor for planning and helping with the projects
* A big thanks to tutor support for helping me out with many difficult issues.
* Tutorial for atuhentication has been taken [here](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)
* Password reset tutorial has been taken from a yoututbe video [here](https://www.youtube.com/watch?v=VLOM-mZCfpk)
* Pagination in django tutorial has been taken [here](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
* Sendgrid tutorial has been taken [here](https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html)
* [Pexels.com](https://www.pexels.com/) has been my go to for all the pictures for this project. 
* Many more resources have been consulted online for advice and python syntax (stackoverflow, pyhton pep8, blogs, etc).
