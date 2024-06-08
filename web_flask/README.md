# 0x04. AirBnB clone - Web framework

Python, Back-end, Webserver, Flask

### Concepts

_For this project, we expect you to look at this concept:_

-   [AirBnB clone](https://intranet.alxswe.com/concepts/74)

# AirBnB clone

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7dce92a57c185b8467fad66d43743199545ad97b085ba0bbf4aba339c5e19297)

  

I know you were waiting for it: it’s here!

  

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/  "AirBnB website").

  

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

  

After 4 months, you will have a complete web application composed by:

  

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

- A website (the front-end) that shows the final product to everybody: static and dynamic

- A database or files that store data (data = objects)

- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

  


## Final product

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=318fd7fb6d680a6020faf37896c72c8546c6d69dc046e0c6b98679620b5586d0)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/da2584da58f1d99a72f0a4d8d22c1e485468f941.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=73b690321c1fa22832733e12de818ce872f374ee5ebdc9692333d1edb4cdf9c1)
  

## Concepts to learn

  

--  [Unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest  "Unittest") - and please work all together on tests cases

--  **Python packages** concept page

# Python packages

  

Read: [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages  "Packages")

  

A Python file can be a **module** but when this file is in a folder, we call this folder a **package**.

  

File organization is really important in a big project. This means for Python: packages everywhere.

  

### Compare with C

  

(file organization, not prototype vs code etc.)

  

In C: `#include "abs.h"`

  

In Python:

  

```

import abs

abs.my_abs(89)

  

```

  

or

  

```

from abs import my_abs

my_abs(89)

  

```

  

In C: `#include "my_math/abs.h"`

  

In Python:

  

```

from my_math.abs import my_abs

my_abs(89)

  

```

  

or

  

```

import my_math.abs

my_math.abs.my_abs(89)

  

```

  

### Dotted module names == Path

  

Let’s take this example of file organization:

  

```

my_script.py

my_math/

abs.py

  

```

  

How can I use my function `my_abs(a)` from the file `abs.py` in `my_script.py`?

  

-  `import my_math/abs.py` => NO

-  `import my_math/abs` => NO

-  `import my_math.abs.py` => NO

-  `import my_math.abs` => YES but you will use your function like that: `my_math.abs.my_abs(89)` => not friendly

-  `from my_math.abs import my_abs` => YES YES YES! now you can use your function like that: `my_abs(89)`

  

Wait, does this really work?

  

NO! something is missing: the magic file `__init__.py`

  

Indeed, each folder **must** contain this file to be considered a package.

  

This file should be empty except if you want to import all the content of modules by using `*`.

  

More complicated?

  

```

my_script.py

my_math/

__init__.py

abs.py

functions/

__init__.py

add.py

  

```

  

How can I use my function `my_add(a, b)` from the file `add.py` in `my_script.py`?

  

`from my_math.functions.add import my_add`

  

Easy right?

  

###  `import *` is dangerous

  

Using `import *` is still considered bad practice in production code. In that case, `__init__.py` shouldn’t be empty but must contain the list of modules to load:

  

```

my_script.py

my_math/

__init__.py

abs.py

functions/

__init__.py

add.py

sub.py

mul.py

div.py

  

```

  

```

$ cat my_script.py

from my_math.functions import *

print(add.my_add(1, 3))

print(mul.my_mul(4, 2))

print(div.my_div(10, 2))

  

$ cat my_math/__init__.py # empty file

$ cat my_math/functions/__init__.py

__all__ = ["add", "mul"]

  

$ python3 my_script.py

3

8

Traceback (most recent call last):

File "my_script.py", line 4, in <module>

print(div.my_div(10, 2))

NameError: name 'div' is not defined

$

  

```

  

### Relative versus Absolute import

  

In this example:

  

```

my_script.py

my_math/

__init__.py

abs.py

positive.py

  

```

  

`positive.py` contains one function `def is_positive(n)` and this function uses `my_abs(n)`. How it’s possible?

  

By importing: `from my_math.abs import my_abs` or `from abs import my_abs`

  

What the difference?

  

-  `from abs import my_abs` is using a relative path between your file who imports and the module to import

-  `from my_math.abs import my_abs` is using an absolute path between the file you execute and the module to import

  

```

$ cat my_script.py

from my_math.positive import is_positive

print(is_positive(89))

print(is_positive(-89))

print(is_positive(333))

  

$ python3 my_script.py

True

False

True

$

  

```

  

Now, let’s execute a file in `my_math`:

  

```

$ cd my_math ; cat test_positive.py

from positive import is_positive

print(is_positive(89))

print(is_positive(-89))

print(is_positive(333))

  

$ cat positive.py

from my_math.abs import my_abs

  

def is_positive(n):

return my_abs(n) == n

  

$ python3 test_positive.py

Traceback (most recent call last):

File "test_positive.py", line 1, in <module>

from positive import is_positive

File "/vagrant/my_math/positive.py", line 1, in <module>

from my_math.abs import my_abs

ImportError: No module named 'my_math'

$

  

```

  

Ahh! If you are using an absolute path, you can’t execute this module from another point as the “root” of your project.

  

Let’s change to relative path:

  

```

$ cd my_math ; cat test_positive.py

from positive import is_positive

print(is_positive(89))

print(is_positive(-89))

print(is_positive(333))

  

$ cat positive.py

from abs import my_abs

  

def is_positive(n):

return my_abs(n) == n

  

$ python3 test_positive.py

True

False

True

$

```

-- Serialization/Deserialization

--  `*args, **kwargs`

--  `datetime`

-- More coming soon!

  

## Steps

  

You won’t build this application all at once, but step by step.

  

Each step will link to a concept:

  

### The console

  

- create your data model

- manage (create, update, destroy, etc) objects via a console / command interpreter

- store and persist objects to a file (JSON file)

  

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

  

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

  


The console will be a tool to validate this storage engine

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5a73b5f645141987b929be88ebbdeccc54d1e9fdbbfc07c7bd2c3c3340f205ca)
  


### Web static

-   learn HTML/CSS
-   create the HTML of your application
-   create template of each object

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c665d58c8657346162aa1fb1d9e7bea885680b8fb3e3ad54af4bd3143a681d45)
  


### MySQL storage

-   replace the file storage by a Database storage
-   map your models to a table in database by using an O.R.M.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=097dab69cb23eec1ef0e5f1535a3f2a72a364b08262b18a339cc77e04759eb09)
  


### Web framework - templating

-   create your first web server in Python
-   make your static HTML file dynamic by using objects stored in a file or database

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d2ca79ecd8ee0b8bdec0e4db9abd54071a8db8c481c45b76da1deab08a971d72)
  


### RESTful API

-   expose all your objects stored via a JSON web interface
-   manipulate your objects via a RESTful API

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ee8a54cef1b39a96f0820f7f5f6fba0670049df9ceaf4fce4e1f2c6c3b2589bd)
  


### Web dynamic

-   learn JQuery
-   load objects from the client side by using your own RESTful API

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=196ae88049e7d79c5639bf51a6d5ec4b92be1080cdafca3e218785fd07385597)
  

## Files and Directories

  

-  `models` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

-  `tests` directory will contain all unit tests.

-  `console.py` file is the entry point of our command interpreter.

-  `models/base_model.py` file is the base class of all our models. It contains common elements:

- attributes: `id`, `created_at` and `updated_at`

- methods: `save()` and `to_json()`

-  `models/engine` directory will contain all storage classes (using the same prototype). For the moment you will have only one: `file_storage.py`.

  

## Storage

  

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

  

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

  

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

  

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

  

- Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)

- Provide default value of any attribute

- In the future, provide the same model behavior for file storage or database storage

  

### How can I store my instances?

  

That’s a good question. So let’s take a look at this code:

  

```

class Student():

def __init__(self, name):

self.name = name

  

students = []

s = Student("John")

students.append(s)

  

```

  

Here, I’m creating a student and store it in a list. But after this program execution, my Student instance doesn’t exist anymore.

  

```

class Student():

def __init__(self, name):

self.name = name

  

students = reload() # recreate the list of Student objects from a file

s = Student("John")

students.append(s)

save(students) # save all Student objects to a file

  

```

  

Nice!

  

But how it works?

  

First, let’s look at `save(students)`:

  

- Can I write each `Student` object to a file => _NO_, it will be the memory representation of the object. For another program execution, this memory representation can’t be reloaded.

- Can I write each `Student.name` to a file => _YES_, but imagine you have other attributes to describe `Student`? It would start to be become too complex.

  

The best solution is to convert this list of `Student` objects to a JSON representation.

  

Why JSON? Because it’s a standard representation of object. It allows us to share this data with other developers, be human readable, but mainly to be understood by another language/program.

  

Example:

  

- My Python program creates `Student` objects and saves them to a JSON file

- Another Javascript program can read this JSON file and manipulate its own `Student` class/representation

  

And the `reload()`? now you know the file is a JSON file representing all `Student` objects. So `reload()` has to read the file, parse the JSON string, and re-create `Student` objects based on this data-structure.

  

### File storage == JSON serialization

  

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure:

  

- convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method `my_instance.to_json()` to retrieve a dictionary

- convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a `my_string = JSON.dumps(my_dict)`

- write this string to a file on disk

  

And the process of deserialization?

  

The same but in the other way:

  

- read a string from a file on disk

- convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a `my_dict = JSON.loads(my_string)`

- convert this data structure to instance - for us it will be a `my_instance = MyObject(my_dict)`

  

##  `*args, **kwargs`

  

[How To Use them](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3  "How To Use them")

  

How do you pass arguments to a function?

  

```

def my_fct(param_1, param_2):

...

  

my_fct("Best", "School")

  

```

  

But with this function definition, you must call `my_fct` with 2 parameters, no more, no less.

  

Can it be dynamic? Yes you can:

  

```

def my_fct(*args, **kwargs):

...

  

my_fct("Best", "School")

  

```

  

What? What’s `*args` and `**kwargs`?

  

-  `*args` is a Tuple that contains all arguments

-  `*kwargs` is a dictionary that contains all arguments by key/value

  

A dictionary? But why?

  

So, to make it clear, `*args` is the list of anonymous arguments, no name, just an order. `**kwargs` is the dictionary with all named arguments.

  

Examples:

  

```

def my_fct(*args, **kwargs):

print("{} - {}".format(args, kwargs))

  

my_fct() # () - {}

my_fct("Best") # ('Best',) - {}

my_fct("Best", 89) # ('Best', 89) - {}

my_fct(name="Best") # () - {'name': 'Best'}

my_fct(name="Best", number=89) # () - {'name': 'Best', 'number': 89}

my_fct("School", 12, name="Best", number=89) # ('School', 12) - {'name': 'Best', 'number': 89}

  

```

  

Perfect? Of course you can mix both, but the order should be first all anonymous arguments, and after named arguments.

  

Last example:

  

```

def my_fct(*args, **kwargs):

print("{} - {}".format(args, kwargs))

  

a_dict = { 'name': "Best", 'age': 89 }

  

my_fct(a_dict) # ({'age': 89, 'name': 'Best'},) - {}

my_fct(*a_dict) # ('age', 'name') - {}

my_fct(**a_dict) # () - {'age': 89, 'name': 'Best'}

  

```

  

You can play with these 2 arguments to clearly understand where and how your variables are stored.

  

##  `datetime`

  

`datetime` is a Python module to manipulate date, time etc…

  

In this example, you create an instance of `datetime` with the current date and time:

  

```

from datetime import datetime

  

date_now = datetime.now()

print(type(date_now)) # <class 'datetime.datetime'>

print(date_now) # 2017-06-08 20:42:42.170922

  

```

  

`date_now` is an object, so you can manipulate it:

  

```

from datetime import timedelta

  

date_tomorrow = date_now + timedelta(days=1)

print(date_tomorrow) # 2017-06-09 20:42:42.170922

  

```

  

… you can also store it:

  

```

a_dict = { 'my_date': date_now }

print(type(a_dict['my_date'])) # <class 'datetime.datetime'>

print(a_dict) # {'my_date': datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}

  

```

  

What? What’s this format when a `datetime` instance is in a datastructure??? It’s unreadable.

  

How to make it readable: [strftime](https://strftime.org/  "strftime")

  

```

print(date_now.strftime("%A")) # Thursday

print(date_now.strftime("%A %d %B %Y at %H:%M:%S")) # Thursday 08 June 2017 at 20:42:42

  

```

  


## Data diagram

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T164107Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=385da7ae397a60012b57a797722ac702d53c8e0951159cf6221d92345e752be0)

## Resources

**Read or watch**:

-   [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb "What is a Web Framework?")
-   [A Minimal Application](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application "A Minimal Application")
-   [Routing](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing "Routing")  (_except “HTTP Methods”_)
-   [Rendering Templates](https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates "Rendering Templates")
-   [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis "Synopsis")
-   [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables "Variables")
-   [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments "Comments")
-   [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control "Whitespace Control")
-   [List of Control Structures](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures "List of Control Structures")  (_read up to “Call”_)
-   [Flask](https://palletsprojects.com/p/flask/ "Flask")
-   [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/ "Jinja")

#### Recommended YouTube playlist to get you started
[CoreyMSchafer Flask Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH "Python Flask")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"),  **without the help of Google**:

### General

-   What is a Web Framework
-   How to build a web framework with Flask
-   How to define routes in Flask
-   What is a route
-   How to handle variables in a route
-   What is a template
-   How to create a HTML response in Flask by using a template
-   How to create a dynamic template (loops, conditions…)
-   How to display in HTML data from a MySQL database

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `PEP 8`  style (version 1.7)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### HTML/CSS Files

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   A  `README.md`  file at the root of the folder of the project is mandatory
-   Your code should be W3C compliant and validate with  [W3C-Validator](https://github.com/alx-tools/W3C-Validator "W3C-Validator")  (except for jinja template)
-   All your CSS files should be in the  `styles`  folder
-   All your images should be in the  `images`  folder
-   You are not allowed to use  `!important`  or  `id`  (`#...`  in the CSS file)
-   All tags must be in uppercase
-   Current screenshots have been done on  `Chrome 56.0.2924.87`.
-   No cross browsers

## More Info

### Install Flask

```
$ pip3 install Flask

```

![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png)

### Manual QA Review

**It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.**

### Video library(1  total)

Python: Flask the web framework

## Tasks

### 0. Hello Flask!

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
-   You must use the option  `strict_slashes=False`  in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   Directory:  `web_flask`
-   File:  `0-hello_route.py, __init__.py`

Done?  Get a sandbox

### 1. HBNB

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
-   You must use the option  `strict_slashes=False`  in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   Directory:  `web_flask`
-   File:  `1-hbnb_route.py`

Done?  Get a sandbox

### 2. C is fun!

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ” followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
-   You must use the option  `strict_slashes=False`  in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   Directory:  `web_flask`
-   File:  `2-c_route.py`

Done?  Get a sandbox

### 3. Python is cool!

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/<text>`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
-   You must use the option  `strict_slashes=False`  in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   Directory:  `web_flask`
-   File:  `3-python_route.py`

Done?  Get a sandbox

### 4. Is it a number?

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
    -   `/number/<n>`: display “`n`  is a number”  **only**  if  `n`  is an integer
-   You must use the option  `strict_slashes=False`  in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   Directory:  `web_flask`
-   File:  `4-number_route.py`

Done?  Get a sandbox

### 5. Number template

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
    -   `/number/<n>`: display “`n`  is a number”  **only**  if  `n`  is an integer
    -   `/number_template/<n>`: display a HTML page  **only**  if  `n`  is an integer:
        -   `H1`  tag: “Number:  `n`” inside the tag  `BODY`
-   You must use the option  `strict_slashes=False`  in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   Directory:  `web_flask`
-   File:  `5-number_template.py, templates/5-number.html`

Done?  Get a sandbox

### 6. Odd or even?

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
    -   `/number/<n>`: display “`n`  is a number”  **only**  if  `n`  is an integer
    -   `/number_template/<n>`: display a HTML page  **only**  if  `n`  is an integer:
        -   `H1`  tag: “Number:  `n`” inside the tag  `BODY`
    -   `/number_odd_or_even/<n>`: display a HTML page  **only**  if  `n`  is an integer:
        -   `H1`  tag: “Number:  `n`  is  `even|odd`” inside the tag  `BODY`
-   You must use the option  `strict_slashes=False`  in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   Directory:  `web_flask`
-   File:  `6-number_odd_or_even.py, templates/6-number_odd_or_even.html`

Done?  Get a sandbox

### 7. Improve engines

mandatory

Before using Flask to display our HBNB data, you will need to update some part of our engine:

Update  `FileStorage`: (`models/engine/file_storage.py`)

-   Add a public method  `def close(self):`: call  `reload()`  method for deserializing the JSON file to objects

Update  `DBStorage`: (`models/engine/db_storage.py`)

-   Add a public method  `def close(self):`: call  `remove()`  method on the private session attribute (`self.__session`)  [tips](https://intranet.alxswe.com/rltoken/_lTxhB5UgQ4nFRoS9ooI5g "tips")  or  `close()`  on the class  `Session`  [tips](https://docs.sqlalchemy.org/en/13/orm/session_api.html "tips")

Update  `State`: (`models/state.py`) - If it’s not already present

-   If your storage engine is not  `DBStorage`, add a public getter method  `cities`  to return the list of  `City`  objects from  `storage`  linked to the current  `State`

```
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!

```

At this moment, in another tab:

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545","2017-03-25 19:42:40","2017-03-25 19:42:40","Alabama");' | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 

```

And let’s go back the Python console:

```
>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!

```

And for the getter  `cities`  in the  `State`  model:

```
guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `models/engine/file_storage.py, models/engine/db_storage.py, models/state.py`

Done?

### 8. List of states

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`
-   Routes:
    -   `/states_list`: display a HTML page: (inside the tag  `BODY`)
        -   `H1`  tag: “States”
        -   `UL`  tag: with the list of all  `State`  objects present in  `DBStorage`  **sorted by  `name`**  (A->Z)  [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/ "tip")
            -   `LI`  tag: description of one  `State`:  `<state.id>: <B><state.name></B>`
-   Import this  [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump")  to have some data
-   You must use the option  `strict_slashes=False`  in your route definition

**IMPORTANT**

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://github.com/OluTshegz/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql "Task"))
-   Make sure all tables are created when you run  `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `web_flask/7-states_list.py, web_flask/templates/7-states_list.html`

Done?  Get a sandbox

### 9. Cities by states

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   To load all cities of a  `State`:
    -   If your storage engine is  `DBStorage`, you must use  `cities`  relationship
    -   Otherwise, use the public getter method  `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`
-   Routes:
    -   `/cities_by_states`: display a HTML page: (inside the tag  `BODY`)
        -   `H1`  tag: “States”
        -   `UL`  tag: with the list of all  `State`  objects present in  `DBStorage`  **sorted by  `name`**  (A->Z)  [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/ "tip")
            -   `LI`  tag: description of one  `State`:  `<state.id>: <B><state.name></B>`  +  `UL`  tag: with the list of  `City`  objects linked to the  `State`  **sorted by  `name`**  (A->Z)
                -   `LI`  tag: description of one  `City`:  `<city.id>: <B><city.name></B>`
-   Import this  [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump")  to have some data
-   You must use the option  `strict_slashes=False`  in your route definition

**IMPORTANT**

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://github.com/OluTshegz/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql "Task"))
-   Make sure all tables are created when you run  `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479545: <B>Akron</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479545: <B>Babbie</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479545: <B>Calera</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479545: <B>Fairfield</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479546: <B>Douglas</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479546: <B>Kearny</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479546: <B>Tempe</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B>
                <UL>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479547: <B>Fremont</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479547: <B>Napa</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479547: <B>San Francisco</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479547: <B>San Jose</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479547: <B>Sonoma</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479548: <B>Denver</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479549: <B>Miami</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479549: <B>Orlando</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479551: <B>Honolulu</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479551: <B>Kailua</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479551: <B>Pearl city</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                        <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                        <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B>
                <UL>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479554: <B>Baton rouge</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479554: <B>Lafayette</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479554: <B>New Orleans</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479555: <B>Saint Paul</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B>
                <UL>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479556: <B>Jackson</B></LI>

                        <LI>541a55f4-7d82-47d9-b54c-a76916479556: <B>Meridian</B></LI>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479556: <B>Tupelo</B></LI>

                </UL>
            </LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B>
                <UL>

                        <LI>531a55f4-7d82-47d9-b54c-a76916479557: <B>Eugene</B></LI>

                        <LI>521a55f4-7d82-47d9-b54c-a76916479557: <B>Portland</B></LI>

                </UL>
            </LI>

        </UL>
    </BODY>
</HTML>
guillaume@ubuntu:~$ 

```

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/9a7ae8155274b17881442200437e8793cf08de48.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T154401Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a509e34743bedb8df291521d3a5ca240fcd4eabe1853c30a56e823ebd74f954f)

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html`

Done?  Get a sandbox


### 10. States and State

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   To load all cities of a  `State`:
    -   If your storage engine is  `DBStorage`, you must use  `cities`  relationship
    -   Otherwise, use the public getter method  `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`
-   Routes:
    -   `/states`: display a HTML page: (inside the tag  `BODY`)
        -   `H1`  tag: “States”
        -   `UL`  tag: with the list of all  `State`  objects present in  `DBStorage`  **sorted by  `name`**  (A->Z)  [tip](https://jinja.palletsprojects.com/en/2.9.x/templates/ "tip")
            -   `LI`  tag: description of one  `State`:  `<state.id>: <B><state.name></B>`
    -   `/states/<id>`: display a HTML page: (inside the tag  `BODY`)
        -   If a  `State`  object is found with this  `id`:
            -   `H1`  tag: “State:
            -   `H3`  tag: “Cities:”
            -   `UL`  tag: with the list of  `City`  objects linked to the  `State`  **sorted by  `name`**  (A->Z)
                -   `LI`  tag: description of one  `City`:  `<city.id>: <B><city.name></B>`
        -   Otherwise:
            -   `H1`  tag: “Not found!”
-   You must use the option  `strict_slashes=False`  in your route definition
-   Import this  [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump")  to have some data

**IMPORTANT**
    Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
-   Make sure all tables are created when you run  `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>States</H1>
        <UL>

            <LI>421a55f4-7d82-47d9-b54c-a76916479545: <B>Alabama</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479546: <B>Arizona</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479547: <B>California</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479548: <B>Colorado</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479549: <B>Florida</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479550: <B>Georgia</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479551: <B>Hawaii</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479552: <B>Illinois</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479553: <B>Indiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479554: <B>Louisiana</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479555: <B>Minnesota</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479556: <B>Mississippi</B></LI>

            <LI>421a55f4-7d82-47d9-b54c-a76916479557: <B>Oregon</B></LI>

        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>State: Illinois</H1>
        <H3>Cities:</H3>
        <UL>
                <LI>521a55f4-7d82-47d9-b54c-a76916479552: <B>Chicago</B></LI>

                <LI>561a55f4-7d82-47d9-b54c-a76916479552: <B>Joliet</B></LI>

                <LI>541a55f4-7d82-47d9-b54c-a76916479552: <B>Naperville</B></LI>

                <LI>531a55f4-7d82-47d9-b54c-a76916479552: <B>Peoria</B></LI>

                <LI>551a55f4-7d82-47d9-b54c-a76916479552: <B>Urbana</B></LI>
        </UL>

    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

        <H1>Not found!</H1>

    </BODY>
</HTML>
guillaume@ubuntu:~$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `web_flask/9-states.py, web_flask/templates/9-states.html`

### 11. HBNB filters

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   To load all cities of a  `State`:
    -   If your storage engine is  `DBStorage`, you must use  `cities`  relationship
    -   Otherwise, use the public getter method  `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`
-   Routes:
    -   `/hbnb_filters`: display a HTML page like  `6-index.html`, which was done during the project  [0x01. AirBnB clone - Web static](https://github.com/OluTshegz/AirBnB_clone/tree/master/web_static "0x01. AirBnB clone - Web static")
        -   Copy files  `3-footer.css`,  `3-header.css`,  `4-common.css`  and  `6-filters.css`  from  `web_static/styles/`  to the folder  `web_flask/static/styles`
        -   Copy files  `icon.png`  and  `logo.png`  from  `web_static/images/`  to the folder  `web_flask/static/images`
        -   Update  `.popover`  class in  `6-filters.css`  to allow scrolling in the popover and a max height of 300 pixels.
        -   Use  `6-index.html`  content as source code for the template  `10-hbnb_filters.html`:
            -   Replace the content of the  `H4`  tag under each filter title (`H3`  States and  `H3`  Amenities) by  `&nbsp;`
        -   `State`,  `City`  and  `Amenity`  objects must be loaded from  `DBStorage`  and  **sorted by name**  (A->Z)
-   You must use the option  `strict_slashes=False`  in your route definition
-   Import this  [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql "10-dump")  to have some data

**IMPORTANT**

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://github.com/OluTshegz/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql "Task"))
-   Make sure all tables are created when you run  `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In the browser:

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=075eeca81e915c96d7327f5c60e48931b7b64287694f58fefc348467dc35c19d)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=caa97d703f88edfdb8cae795d77be76775b2ce08ca5eec3fd5bb908664b90b0b)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=64937603c9b879dfee3f9c56ebe9a2635ff393deb25bcba2defb93d7b671c22c)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=767100760fe641caf40ab06b297c56c72652a1fbc1de679e2c2e3d5c8314cbd3)

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/`

### 12. HBNB is alive!

#advanced

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   To load all cities of a  `State`:
    -   If your storage engine is  `DBStorage`, you must use  `cities`  relationship
    -   Otherwise, use the public getter method  `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`
-   Routes:
    -   `/hbnb`: display a HTML page like  `8-index.html`, done during the  [0x01. AirBnB clone - Web static](https://github.com/OluTshegz/AirBnB_clone/tree/master/web_static "0x01. AirBnB clone - Web static")  project
        -   Copy files  `3-footer.css`,  `3-header.css`,  `4-common.css`,  `6-filters.css`  and  `8-places.css`  from  `web_static/styles/`  to the folder  `web_flask/static/styles`
        -   Copy all files from  `web_static/images/`  to the folder  `web_flask/static/images`
        -   Update  `.popover`  class in  `6-filters.css`  to enable scrolling in the popover and set max height to 300 pixels.
        -   Update  `8-places.css`  to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)
        -   Use  `8-index.html`  content as source code for the template  `100-hbnb.html`:
            -   Replace the content of the  `H4`  tag under each filter title (`H3`  States and  `H3`  Amenities) by  `&nbsp;`
            -   Make sure all HTML tags from objects are correctly used (example:  `<BR />`  must generate a new line)
        -   `State`,  `City`,  `Amenity`  and  `Place`  objects must be loaded from  `DBStorage`  and  **sorted by name**  (A->Z)
-   You must use the option  `strict_slashes=False`  in your route definition
-   Import this  [100-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql "100-dump")  to have some data

**IMPORTANT**

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://github.com/OluTshegz/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql "Task"))
-   Make sure all tables are created when you run  `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 100-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 100-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

```

In the browser:

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/396ae10c9f85a6128ae40e1b63f4bce95adf411c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4364e76c81b4fb4a926a912edc5658b95513e035d301f4881b1b748d9eabb553)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/9eb21499b5f3b59751fdbf561174e2f259d97482.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=47bf04bc9f7ba53fd83c3f6d0af9bca1fc1cd36def181ea576d94cdf6785ae51)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bf248a63c15a746ad694acffdd56d80281782c71.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0f90444f3b4b593e2de69db0876a0825d3a28dbd3b08745c45aaf5345b60c01a)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/494317aad058a649a51f416eceee1a609f07c6c0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a5486917bff7068e9e37731cdecf2ada095f44135d75be473297763791503dcd)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/016911388aa92532e06c4d5361188a2622425517.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T172527Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3b2e48d6c8ff470a368cb4c37f745e9cd7e2f1c79a8bb733d0664017f9577d67)

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `web_flask/100-hbnb.py, web_flask/templates/100-hbnb.html, web_flask/static/`
