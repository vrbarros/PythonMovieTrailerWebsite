PythonMoviewTrailerWebsite
==========================

Hi, welcome to my first Python project! I changed a little the scope of the project in a away to use API integration, Bootstrap and Flask.

This project was developed using Python 3.6.1.

As I'm using TMDB database API to download your favorite movies, I left my credentials in the my_setup = TMDB_Setup() in tmdb.py file in order to make the evaluation easy.

The project was tested in local server. I'm trying to learn how to upload to heroku.

Follow the steps to test the app:

1) Setup Python 3.6.1 enviroment (https://docs.python.org/3/using/)
2) Remember to run: pip install -r requirements.txt
3) Check the files:
    movies.py -> Build the favorite movie array to be used in our HTML page
    tmdb.py -> Connect with TMDB API, authenticate and retrieve data
    test.py -> Make a test making all HTML pages
    app.py -> Start the localserver and make the HTML output
4) Go to app.py and Build (Ctrl + B)