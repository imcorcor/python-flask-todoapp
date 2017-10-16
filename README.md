# Before you judge the code

This was my very first web app created in March 2017, after 4 months of learning Python programming language from scratch.
As one wise man once said: "Everybody has to start somewhere. You have your whole future ahead of you. Perfection doesn't happen right away."


## ToDo App on WEB!

Simple web TODO app to manage your tasks.

## Getting Started

This app is written in Python3 programming language, with the support of Flask microframework.
It consists one main directory and three subdirectories.
In main directory you can find a script named main.py which is used to run the application. You can also find a file named create_database.py which when run in terminal, creates a database file named database.db using sqlite3 commands. This database is necessary for app to work.
Other directories are:
* models - you can find there a file named todo.py which is the engine of this app. It connects with database and all operations on database are held there.
* templates - consisting of three files: index.html, add.html and edit.html, which describe the way this web application behaves. Those files are connected with Python via Flask framework.
* static - you find there a file named style.css which holds all data about the way this app is displayed on web. It changes the look of it.

### Prerequisites

You need to install Flask.0.12.x. Flask is a framework for Python so make sure you have Python v 3+ installed first.

```
$ python
Python 3.5.2+ (default, Sep 22 2016, 12:18:14)
[GCC 6.2.0 20160927] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

### Installing

Install Flask

```
$ sudo pip install flask
```

## Deployment

First clone this repository by running this command in your terminal:

```
$ git clone https://github.com/fulloffish/python-flask-todoapp.git

```


Then, create database by running create_database.py in your terminal.

```
$ python3 create_database.py
    Database created successfully.

```

Now run main.py in your terminal.

```
$ python3 main.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

Go to the url http://127.0.0.1:5000/

That is how you can use this app. For further developing, read next chapter.

## For developers

* more functions
    All operations on database are held in todo.py file in models directory. This app provides simple CRUD operations. You can add your own methods. Structure of database is defined in create_database.py placed in main directory.
* more subpages
    All routes are predefined in main.py file placed in main directory. You can add more by following the structure pattern.
* better look
    File responsible for this app's looks is style.css. You can easly change the layout, colors and style here. Feel free to try.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Python 3.5.2+](https://www.python.org/download/releases/3.0/) - Back end


## Authors

* **Ania Polak** - *Initial work* - [fulloffish](https://github.com/fulloffish)


## Acknowledgments

* Idea for this comes from Codecool SI week assignment.
