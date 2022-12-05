<p align="center">
  <img src="img/todone-logo.png" />
</p>
<h2 align="center">The Only Todo List You Need</h2>

[![Build Status](https://img.shields.io/github/workflow/status/shahleon/smart-todo/Django%20CI/main)](https://github.com/shahleon/smart-todo/actions/workflows/django.yml)
[![Coverage Status](https://coveralls.io/repos/github/shahleon/smart-todo/badge.svg?branch=main)](https://coveralls.io/github/shahleon/smart-todo?branch=main)
[![license badge](https://img.shields.io/github/license/shahleon/cs510-homework-1)](https://github.com/shahleon/smart-todo/blob/main/LICENSE)
[![issues badge](https://img.shields.io/github/issues/shahleon/smart-todo)](https://github.com/shahleon/smart-todo/issues)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Django 4.1](https://img.shields.io/badge/django-4.1-blue.svg)](https://docs.djangoproject.com/en/4.1/releases/4.1/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7155415.svg)](https://doi.org/10.5281/zenodo.7155415)

# TO-DONE

`to-done` lets you manage your todo list effectively with minimal effort. With a minimalistic web interface, 
you can access your todolist on the go. Use our rich library of templates to create a new todo list very fast or create your own.

![To-Done](img/todone-create-list.gif)

Contents
========

 * [Why?](#why)
 * [Features](#key-features)
 * [Upcoming Features](#upcoming-features)
 * [Quick Start](#quick-start)
 * [Documentation](#Documentation)
 * [Want to contribute?](#want-to-contribute)
 * [License](#license)
 * [Developer](#developers)

### Why?

We wanted to work on something that is:

+ Useful, serves some real purpose
+ Easy to start with a basic working version and lends itself to adding new features incrementally to it
+ Easily divisible in modules/features/tasks that can be parallely done by five developers 
+ Diverse enough so that a lot of Software Engineering practices is required/involved 

`to-done` is a todo list app that is actually useful, very easy to create a basic working version with where a ton of new features can be added, touches upon all the aspects of web programming, database, working in a team etc.

### Key Features (Last Version)
 * [Register](#register)
 * [Login](#login-forget-password)
 * [Create, Update, Delete Todo Lists](#manage-todo-list)
 * [Quickly Create Todo Lists From Existing Templates](#templates)
 * [Create Your Own Templates](#templates)

### New Features
* [Shared List]
* [Add Due Date To Tasks]
* [Due Date Alerting Mechanism]
* [Add Reminder Message to completed]
* [Customized Color Tag]
* [Add Tags To Todo Lists For Customizable Grouping]

### Upcoming Features
 * Social login
 * Export and import to-do lists
 * Gamification - earn points by finishing your tasks, show-off your productivity in social media
 * [List of All Planned Features for Second Phase](https://github.com/users/shahleon/projects/2/views/6)

### Quick Start

 * [Download](https://www.python.org/downloads/release/python-380/) and install Python 3.8.0 or higher
 * [Install](https://docs.djangoproject.com/en/4.1/topics/install/) Django 4.1
 * Clone the repository
    ```bash
    $ git clone git@github.com:shahleon/smart-todo.git
    ```
 * Run migrations
    ```bash
    $ cd smarttodo
    $ python manage.py migrate
    ```
 * Start the app
    ```bash
    $ python manage.py runserver 8080
    ```
 * Point your browser at http://127.0.0.1:8080 and explore the app

### Documentation
[See this page](https://shahleon.github.io/smart-todo/)

### Features

#### Register
<p float="middle">
    <img src="img/todone-register.gif" width="500" height="250" />
</p>

#### Login, Forget Password
<p float="middle">
    <img src="img/todone-login.gif" width="500" height="250" /> 
</p>

#### Manage Todo List
<p float="middle">
    <img src="img/todone-create-list.gif" width="500" height="250" />
    <br>
    <br>
    <img src="img/todone-update-list.gif" width="500" height="250" />
</p>

#### Templates
<p float="middle">
    <img src="img/todone-templates.gif" width="500" height="250" />
</p>

### Want to Contribute?

Want to contribute to this project? Learn about [Contributing](CONTRIBUTING.md). Not sure where to start? Have a look at 
the [good first issue](https://github.com/shahleon/smart-todo/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22). Found a bug or have a new feature idea? Create an [Issue](https://github.com/shahleon/smart-todo/issues/new) or shoot a mail to [us](#developers)

### License

Distributed under the MIT License. See [LICENSE](License) for more information.

### Developers (New Version)

<table>
  <tr>
    <td align="center"><a href="https://github.com/juliachiu1"><img src="https://avatars.githubusercontent.com/u/112150278?v=4" width="100px;" alt=""/><br /><sub><b>Chiu, Ching-Lun</b></sub></a></td>
    <td align="center"><a href="https://github.com/Hsueh-YANG"><img src="https://avatars.githubusercontent.com/u/23623764?v=4" width="100px;" alt=""/><br /><sub><b>Yu, Hsueh-Yang</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/123standup"><img src="https://avatars.githubusercontent.com/u/59056739?v=4" width="100px;" alt=""/><br /><sub><b>Lin, Po-Hsun</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Chloe-Ku"><img src="https://avatars.githubusercontent.com/u/60029373?v=4" width="100px;" alt=""/><br /><sub><b>Ku, Li-Ling</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/jackson910210"><img src="https://avatars.githubusercontent.com/u/32348727?v=4" width="100px;" alt=""/><br /><sub><b>Chiang, Chen-Hsuan</b></sub></a><br /></td>
  </tr>
</table>

### Developers (Last Version)

* Shahnewaz Leon (sleon3@ncsu.edu)
* Dong Li (dli35@ncsu.edu)
* Cheng-Yun Kuo (ckuo3@ncsu.edu)
* Drew Commings (docummin@ncsu.edu)
* Janet Brock (jdbrock@ncsu.edu)
