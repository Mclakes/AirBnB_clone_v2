
# 0x02. AirBnB clone - MySQL

Group project: Python, OOP, Back-end, SQL, MySQL, ORM, SQLAlchemy.

## Background Context

Environment variables will be your best friend for this project!

-   `HBNB_ENV`: running environment. It can be “dev” or “test” for the moment (“production” soon!)
-   `HBNB_MYSQL_USER`: the username of your MySQL
-   `HBNB_MYSQL_PWD`: the password of your MySQL
-   `HBNB_MYSQL_HOST`: the hostname of your MySQL
-   `HBNB_MYSQL_DB`: the database name of your MySQL
-   `HBNB_TYPE_STORAGE`: the type of storage used. It can be “file” (using  `FileStorage`) or  `db`  (using  `DBStorage`)

## Resources

**Read or watch**:

-   [cmd module](https://docs.python.org/3/library/cmd.html "cmd module")
-   **packages**  concept page
# Python packages

Read:  [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages "Packages")

A Python file can be a  **module**  but when this file is in a folder, we call this folder a  **package**.

File organization is really important in a big project. This means for Python: packages everywhere.

### Compare with C

(file organization, not prototype vs code etc.)

In C:  `#include "abs.h"`

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

In C:  `#include "my_math/abs.h"`

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

How can I use my function  `my_abs(a)`  from the file  `abs.py`  in  `my_script.py`?

-   `import my_math/abs.py`  => NO
-   `import my_math/abs`  => NO
-   `import my_math.abs.py`  => NO
-   `import my_math.abs`  => YES but you will use your function like that:  `my_math.abs.my_abs(89)`  => not friendly
-   `from my_math.abs import my_abs`  => YES YES YES! now you can use your function like that:  `my_abs(89)`

Wait, does this really work?

NO! something is missing: the magic file  `__init__.py`

Indeed, each folder  **must**  contain this file to be considered a package.

This file should be empty except if you want to import all the content of modules by using  `*`.

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

How can I use my function  `my_add(a, b)`  from the file  `add.py`  in  `my_script.py`?

`from my_math.functions.add import my_add`

Easy right?

### `import *`  is dangerous

Using  `import *`  is still considered bad practice in production code. In that case,  `__init__.py`  shouldn’t be empty but must contain the list of modules to load:

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

$ cat my_math/__init__.py  # empty file
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

`positive.py`  contains one function  `def is_positive(n)`  and this function uses  `my_abs(n)`. How it’s possible?

By importing:  `from my_math.abs import my_abs`  or  `from abs import my_abs`

What the difference?

-   `from abs import my_abs`  is using a relative path between your file who imports and the module to import
-   `from my_math.abs import my_abs`  is using an absolute path between the file you execute and the module to import

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

Now, let’s execute a file in  `my_math`:

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
-   [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest "unittest module")
-   [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/ "args/kwargs")
-   [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html "SQLAlchemy tutorial")
-   [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql "How To Create a New User and Grant Permissions in MySQL")
-   [Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv "Python3 and environment variables")
-   [SQLAlchemy](https://docs.sqlalchemy.org/en/13/ "SQLAlchemy")
-   [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html "MySQL 8.0 SQL Statement Syntax")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"),  **without the help of Google**:

### General

-   What is Unit testing and how to implement it in a large project
-   What is  `*args`  and how to use it
-   What is  `**kwargs`  and how to use it
-   How to handle named arguments in a function
-   How to create a MySQL database
-   How to create a MySQL user and grant it privileges
-   What ORM means
-   How to map a Python Class to a MySQL table
-   How to handle 2 different storage engines with the same codebase
-   How to use environment variables

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version  `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder  `tests`
-   You have to use the  [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest "unittest module")
-   All your test files should be python files (extension:  `.py`)
-   All your test files and folders should start by  `test_`
-   Your file organization in the tests folder should be the same as your project: ex: for  `models/base_model.py`, unit tests must be in:  `tests/test_models/test_base_model.py`
-   All your tests should be executed by using this command:  `python3 -m unittest discover tests`
-   You can also test file by file by using this command:  `python3 -m unittest tests/test_models/test_base_model.py`
-   All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   We strongly encourage you to work together on test cases, so that you don’t miss any edge cases

### SQL Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be executed on Ubuntu 20.04 LTS using  `MySQL 8.0`
-   Your files will be executed with  `SQLAlchemy`  version  `1.4.x`
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`…)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`

### GitHub

**There should be one project repository.**

## More Info

![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png)

### Comments for your SQL file:

```
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

### Video library(2  total)

HBNB - storage abstraction

AirBnB console



<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>



## Tasks

### 0. Fork me if you can!

mandatory

In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:

-   “Who did this code?”
-   “How it works?”
-   “Where are unittests?”
-   “Where is this?”
-   “Why did they do that like this?”
-   “I don’t understand anything.”
-   “… I will refactor everything…”

But the worst thing you could possibly do is to  **redo everything**. Please don’t do that!  **Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!**

For this project you will fork this  [codebase](https://github.com/justinmajetich/AirBnB_clone.git "codebase"):

-   update the repository name to  `AirBnB_clone_v2`
-   update the  `README.md`  with your information  **but don’t delete the initial authors**

If you are the owner of this repository, please create a new repository named  `AirBnB_clone_v2`  with the same content of  `AirBnB_clone`

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`

Done?  Check your code  Get a sandbox

### 1. Bug free!

mandatory

Do you remember the  `unittest`  module?

This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of the program.

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ 

```

All your unittests  **must**  pass without any errors at anytime in this project,  **with each storage engine!**. Same for PEP8!

```
guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ 

```

Some tests won’t be relevant for some type of storage, please skip them by using the  `skipIf`  feature of  [the Unittest module - 26.3.6. Skipping tests and expected failures](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures "the Unittest module - 26.3.6. Skipping tests and expected failures"). Of course, the number of tests must be higher than the current number of tests, so if you decide to skip a test, you should write a new test!

### How to test with MySQL?

First, you create a specific database for it (next tasks). After, you have to remember what the purpose of an unittest?

**“Assert a current state (objects/data/database), do an action, and validate this action changed (or not) the state of your objects/data/database”**

For example, “you want to validate that the  `create State name="California"`  command in the console will add a new record in your table  `states`  in your database”, here steps for your unittest:

-   get the number of current records in the table  `states`  (my using a  `MySQLdb`  for example - but not SQLAlchemy (remember, you want to test if it works, so it’s better to isolate from the system))
-   execute the console command
-   get (again) the number of current records in the table  `states`  (same method, with  `MySQLdb`)
-   if the difference is  `+1`  => test passed

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`

Done?  Check your code

### 2. Console improvements

mandatory

Update the  `def do_create(self, arg):`  function of your command interpreter (`console.py`) to allow for object creation with given parameters:

-   Command syntax:  `create <Class name> <param 1> <param 2> <param 3>...`
-   Param syntax:  `<key name>=<value>`
-   Value syntax:
    -   String:  `"<value>"`  => starts with a double quote
        -   any double quote inside the value must be escaped with a backslash  `\`
        -   all underscores  `_`  must be replace by spaces  . Example: You want to set the string  `My little house`  to the attribute  `name`, your command line must be  `name="My_little_house"`
    -   Float:  `<unit>.<decimal>`  => contains a dot  `.`
    -   Integer:  `<number>`  => default case
-   If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped

**Don’t forget to add tests for this new feature!**

Also, this new feature will be tested here only with  `FileStorage`  engine.

```
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create
create State name="California"
create State name="Arizona"
all State

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create | ./console.py 
(hbnb) d80e0344-63eb-434a-b1e0-07783522124e
(hbnb) 092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7
(hbnb) [[State] (d80e0344-63eb-434a-b1e0-07783522124e) {'id': 'd80e0344-63eb-434a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name': 'California'}, [State] (092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7) {'id': '092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842779), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842792), 'name': 'Arizona'}]
(hbnb) (hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124
(hbnb) [[Place] (76b65327-9e94-4632-b688-aaa22ab8a124) {'number_bathrooms': 2, 'longitude': -122.431297, 'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, 'price_by_night': 300, 'name': 'My little house', 'id': '76b65327-9e94-4632-b688-aaa22ab8a124', 'max_guest': 10, 'number_rooms': 4, 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843774), 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843747)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `console.py, models/, tests/`

Done?  Check your code  Get a sandbox

### 3. MySQL setup development

mandatory

Write a script that prepares a MySQL server for the project:

-   A database  `hbnb_dev_db`
-   A new user  `hbnb_dev`  (in  `localhost`)
-   The password of  `hbnb_dev`  should be set to  `hbnb_dev_pwd`
-   `hbnb_dev`  should have all privileges on the database  `hbnb_dev_db`  (and  **only this database**)
-   `hbnb_dev`  should have  `SELECT`  privilege on the database  `performance_schema`  (and  **only this database**)
-   If the database  `hbnb_dev_db`  or the user  `hbnb_dev`  already exists, your script should not fail

```
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
Enter password: 
hbnb_dev_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_dev@localhost
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `setup_mysql_dev.sql`

Done?  Check your code  Get a sandbox

### 4. MySQL setup test

mandatory

Write a script that prepares a MySQL server for the project:

-   A database  `hbnb_test_db`
-   A new user  `hbnb_test`  (in  `localhost`)
-   The password of  `hbnb_test`  should be set to  `hbnb_test_pwd`
-   `hbnb_test`  should have all privileges on the database  `hbnb_test_db`  (and  **only this database**)
-   `hbnb_test`  should have  `SELECT`  privilege on the database  `performance_schema`  (and  **only this database**)
-   If the database  `hbnb_test_db`  or the user  `hbnb_test`  already exists, your script should not fail

```
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
Enter password: 
hbnb_test_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_test@localhost
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `setup_mysql_test.sql`

Done?  Check your code  Get a sandbox

### 5. Delete object

mandatory

Update  `FileStorage`: (`models/engine/file_storage.py`)

-   Add a new public instance method:  `def delete(self, obj=None):`  to delete  `obj`  from  `__objects`  if it’s inside - if  `obj`  is equal to  `None`, the method should not do anything
-   Update the prototype of  `def all(self)`  to  `def all(self, cls=None)`  - that returns the list of objects of one type of class. Example below with  `State`  - it’s an optional filtering

```
guillaume@ubuntu:~/AirBnB_v2$ cat main_delete.py
#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

guillaume@ubuntu:~/AirBnB_v2$ ./main_delete.py
All States: 0
New State: [State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
All States: 1
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
Another State: [State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 2
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 1
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `models/engine/file_storage.py`

Done?  Check your code  Get a sandbox

### 6. DBStorage - States and Cities

mandatory

SQLAlchemy will be your best friend!

It’s time to change your storage engine and use  `SQLAlchemy`

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/daaef631636b40e0a279a8f240703e065f9d3481.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240416%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240416T123207Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8490bd82063db31725e88051eb909de05cd561a6f46e7f46275ec8d6ce213d9d)

In the following steps, you will make multiple changes:

-   the biggest one is the transition between  `FileStorage`  and  `DBStorage`: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the  **abstraction**: Make your code running without knowing how it’s stored.
-   add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)

Please follow all these steps:

Update  `BaseModel`: (`models/base_model.py`)

-   Create  `Base = declarative_base()`  before the class definition of  `BaseModel`
-   **Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id,  `created_at`,  `updated_at`), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.**
-   Add or replace in the class  `BaseModel`:
    -   class attribute  `id`
        -   represents a column containing a unique string (60 characters)
        -   can’t be null
        -   primary key
    -   class attribute  `created_at`
        -   represents a column containing a datetime
        -   can’t be null
        -   default value is the current datetime (use  `datetime.utcnow()`)
    -   class attribute  `updated_at`
        -   represents a column containing a datetime
        -   can’t be null
        -   default value is the current datetime (use  `datetime.utcnow()`)
-   Move the  `models.storage.new(self)`  from  `def __init__(self, *args, **kwargs):`  to  `def save(self):`  and call it just before  `models.storage.save()`
-   In  `def __init__(self, *args, **kwargs):`, manage  `kwargs`  to create instance attribute from this dictionary. Ex:  `kwargs={ 'name': "California" }`  =>  `self.name = "California"`  if it’s not already the case
-   Update the  `to_dict()`  method of the class  `BaseModel`:
    -   remove the key  `_sa_instance_state`  from the dictionary returned by this method  **only if this key exists**
-   Add a new public instance method:  `def delete(self):`  to delete the current instance from the storage (`models.storage`) by calling the method  `delete`

Update  `City`: (`models/city.py`)

-   `City`  inherits from  `BaseModel`  and  `Base`  (respect the order)
-   Add or replace in the class  `City`:
    -   class attribute  `__tablename__`  -
        -   represents the table name,  `cities`
    -   class attribute  `name`
        -   represents a column containing a string (128 characters)
        -   can’t be null
    -   class attribute  `state_id`
        -   represents a column containing a string (60 characters)
        -   can’t be null
        -   is a foreign key to  `states.id`

Update  `State`: (`models/state.py`)

-   `State`  inherits from  `BaseModel`  and  `Base`  (respect the order)
-   Add or replace in the class  `State`:
    -   class attribute  `__tablename__`
        -   represents the table name,  `states`
    -   class attribute  `name`
        -   represents a column containing a string (128 characters)
        -   can’t be null
    -   for  `DBStorage`: class attribute  `cities`  must represent a relationship with the class  `City`. If the  `State`  object is deleted, all linked  `City`  objects must be automatically deleted. Also, the reference from a  `City`  object to his  `State`  should be named  `state`
    -   for  `FileStorage`: getter attribute  `cities`  that returns the list of  `City`  instances with  `state_id`  equals to the current  `State.id`  => It will be the  `FileStorage`  relationship between  `State`  and  `City`

New engine  `DBStorage`: (`models/engine/db_storage.py`)

-   Private class attributes:
    -   `__engine`: set to  `None`
    -   `__session`: set to  `None`
-   Public instance methods:
    -   `__init__(self):`
        -   create the engine (`self.__engine`)
        -   the engine must be linked to the MySQL database and user created before (`hbnb_dev`  and  `hbnb_dev_db`):
            -   dialect:  `mysql`
            -   driver:  `mysqldb`
        -   all of the following values must be retrieved via environment variables:
            -   MySQL user:  `HBNB_MYSQL_USER`
            -   MySQL password:  `HBNB_MYSQL_PWD`
            -   MySQL host:  `HBNB_MYSQL_HOST`  (here =  `localhost`)
            -   MySQL database:  `HBNB_MYSQL_DB`
        -   don’t forget the option  `pool_pre_ping=True`  when you call  `create_engine`
        -   drop all tables if the environment variable  `HBNB_ENV`  is equal to  `test`
    -   `all(self, cls=None)`:
        -   query on the current database session (`self.__session`) all objects depending of the class name (argument  `cls`)
        -   if  `cls=None`, query all types of objects (`User`,  `State`,  `City`,  `Amenity`,  `Place`  and  `Review`)
        -   this method must return a dictionary: (like  `FileStorage`)
            -   key =  `<class-name>.<object-id>`
            -   value = object
    -   `new(self, obj)`: add the object to the current database session (`self.__session`)
    -   `save(self)`: commit all changes of the current database session (`self.__session`)
    -   `delete(self, obj=None)`: delete from the current database session  `obj`  if not  `None`
    -   `reload(self)`:
        -   create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from  `Base`  must be imported before calling  `Base.metadata.create_all(engine)`)
        -   create the current database session (`self.__session`) from the engine (`self.__engine`) by using a  [sessionmaker](https://docs.sqlalchemy.org/en/13/orm/session_api.html "sessionmaker")  - the option  `expire_on_commit`  must be set to  `False`  ; and  [scoped_session](https://docs.sqlalchemy.org/en/13/orm/contextual.html "scoped_session")  - to make sure your Session is thread-safe

Update  `__init__.py`: (`models/__init__.py`)

-   Add a conditional depending of the value of the environment variable  `HBNB_TYPE_STORAGE`:
    -   If equal to  `db`:
        -   Import  `DBStorage`  class in this file
        -   Create an instance of  `DBStorage`  and store it in the variable  `storage`  (the line  `storage.reload()`  should be executed after this instantiation)
    -   Else:
        -   Import  `FileStorage`  class in this file
        -   Create an instance of  `FileStorage`  and store it in the variable  `storage`  (the line  `storage.reload()`  should be executed after this instantiation)
-   This “switch” will allow you to change storage type directly by using an environment variable (example below)

State creation:

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
guillaume@ubuntu:~/AirBnB_v2$ 

```

City creation:

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 

```

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) a7db3cdc-30e0-4d80-ad8c-679fe45343ba
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
*************************** 2. row ***************************
        id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
created_at: 2017-11-10 00:53:19
updated_at: 2017-11-10 00:53:19
      name: San Jose
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `models/base_model.py, models/city.py, models/state.py, models/engine/db_storage.py, models/__init__.py`

Done?  Check your code

### 7. DBStorage - User

mandatory

Update  `User`: (`models/user.py`)

-   `User`  inherits from  `BaseModel`  and  `Base`  (respect the order)
-   Add or replace in the class  `User`:
    -   class attribute  `__tablename__`
        -   represents the table name,  `users`
    -   class attribute  `email`
        -   represents a column containing a string (128 characters)
        -   can’t be null
    -   class attribute  `password`
        -   represents a column containing a string (128 characters)
        -   can’t be null
    -   class attribute  `first_name`
        -   represents a column containing a string (128 characters)
        -   can be null
    -   class attribute  `last_name`
        -   represents a column containing a string (128 characters)
        -   can be null

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[User] (4f3f4b42-a4c3-4c20-a492-efff10d00c0b) {'updated_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'last_name': 'Snow', 'first_name': 'Guillaume', 'email': 'gui@hbtn.io', 'created_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'password': 'f4ce007d8e84e0910fbdd7a06fa1692d'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
created_at: 2017-11-10 01:17:26
updated_at: 2017-11-10 01:17:26
     email: gui@hbtn.io
  password: guipwd
first_name: Guillaume
 last_name: Snow
guillaume@ubuntu:~/AirBnB_v2$

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `models/user.py`

Done?  Check your code

### 8. DBStorage - Place

mandatory

Update  `Place`: (`models/place.py`)

-   `Place`  inherits from  `BaseModel`  and  `Base`  (respect the order)
-   Add or replace in the class  `Place`:
    -   class attribute  `__tablename__`
        -   represents the table name,  `places`
    -   class attribute  `city_id`
        -   represents a column containing a string (60 characters)
        -   can’t be null
        -   is a foreign key to  `cities.id`
    -   class attribute  `user_id`
        -   represents a column containing a string (60 characters)
        -   can’t be null
        -   is a foreign key to  `users.id`
    -   class attribute  `name`
        -   represents a column containing a string (128 characters)
        -   can’t be null
    -   class attribute  `description`
        -   represents a column containing a string (1024 characters)
        -   can be null
    -   class attribute  `number_rooms`
        -   represents a column containing an integer
        -   can’t be null
        -   default value:  `0`
    -   class attribute  `number_bathrooms`
        -   represents a column containing an integer
        -   can’t be null
        -   default value:  `0`
    -   class attribute  `max_guest`
        -   represents a column containing an integer
        -   can’t be null
        -   default value:  `0`
    -   class attribute  `price_by_night`
        -   represents a column containing an integer
        -   can’t be null
        -   default value:  `0`
    -   class attribute  `latitude`
        -   represents a column containing a float
        -   can be null
    -   class attribute  `longitude`
        -   represents a column containing a float
        -   can be null

Update  `User`: (`models/user.py`)

-   Add or replace in the class  `User`:
    -   class attribute  `places`  must represent a relationship with the class  `Place`. If the  `User`  object is deleted, all linked  `Place`  objects must be automatically deleted. Also, the reference from a  `Place`  object to his  `User`  should be named  `user`

Update  `City`: (`models/city.py`)

-   Add or replace in the class  `City`:
    -   class attribute  `places`  must represent a relationship with the class  `Place`. If the  `City`  object is deleted, all linked  `Place`  objects must be automatically deleted. Also, the reference from a  `Place`  object to his  `City`  should be named  `cities`

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) ed72aa02-3286-4891-acbc-9d9fc80a1103
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Place' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Place] (ed72aa02-3286-4891-acbc-9d9fc80a1103) {'latitude': 37.774, 'city_id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'price_by_night': 120, 'id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'user_id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'max_guest': 6, 'created_at': datetime.datetime(2017, 11, 10, 1, 22, 30), 'description': None, 'number_rooms': 3, 'longitude': -122.431, 'number_bathrooms': 1, 'name': '"Lovely place', 'updated_at': datetime.datetime(2017, 11, 10, 1, 22, 30)}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: ed72aa02-3286-4891-acbc-9d9fc80a1103
      created_at: 2017-11-10 01:22:30
      updated_at: 2017-11-10 01:22:30
         city_id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
         user_id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
            name: "Lovely place"
     description: NULL
    number_rooms: 3
number_bathrooms: 1
       max_guest: 6
  price_by_night: 120
        latitude: 37.774
       longitude: -122.431
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `models/place.py, models/user.py, models/city.py`

Done?  Check your code

### 9. DBStorage - Review

mandatory

Update  `Review`: (`models/review.py`)

-   `Review`  inherits from  `BaseModel`  and  `Base`  (respect the order)
-   Add or replace in the class  `Review`:
    -   class attribute  `__tablename__`
        -   represents the table name,  `reviews`
    -   class attribute  `text`
        -   represents a column containing a string (1024 characters)
        -   can’t be null
    -   class attribute  `place_id`
        -   represents a column containing a string (60 characters)
        -   can’t be null
        -   is a foreign key to  `places.id`
    -   class attribute  `user_id`
        -   represents a column containing a string (60 characters)
        -   can’t be null
        -   is a foreign key to  `users.id`

Update  `User`: (`models/user.py`)

-   Add or replace in the class  `User`:
    -   class attribute  `reviews`  must represent a relationship with the class  `Review`. If the  `User`  object is deleted, all linked  `Review`  objects must be automatically deleted. Also, the reference from a  `Review`  object to his  `User`  should be named  `user`

Update  `Place`: (`models/place.py`)

-   for  `DBStorage`: class attribute  `reviews`  must represent a relationship with the class  `Review`. If the  `Place`  object is deleted, all linked  `Review`  objects must be automatically deleted. Also, the reference from a  `Review`  object to his  `Place`  should be named  `place`
-   for  `FileStorage`: getter attribute  `reviews`  that returns the list of  `Review`  instances with  `place_id`  equals to the current  `Place.id`  => It will be the  `FileStorage`  relationship between  `Place`  and  `Review`

```
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="bob@hbtn.io" password="bobpwd" first_name="Bob" last_name="Dylan"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) d93638d9-8233-4124-8f4e-17786592908b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Review place_id="ed72aa02-3286-4891-acbc-9d9fc80a1103" user_id="d93638d9-8233-4124-8f4e-17786592908b" text="Amazing_place,_huge_kitchen"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) a2d163d3-1982-48ab-a06b-9dc71e68a791
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Review' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Review] (f2616ff2-f723-4d67-85dc-f050a38e0f2f) {'text': 'Amazing place, huge kitchen', 'place_id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'id': 'f2616ff2-f723-4d67-85dc-f050a38e0f2f', 'updated_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'created_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'user_id': 'd93638d9-8233-4124-8f4e-17786592908b'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM reviews\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: f2616ff2-f723-4d67-85dc-f050a38e0f2f
created_at: 2017-11-10 04:06:25
updated_at: 2017-11-10 04:06:25
      text: Amazing place, huge kitchen
  place_id: ed72aa02-3286-4891-acbc-9d9fc80a1103
   user_id: d93638d9-8233-4124-8f4e-17786592908b
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `models/review.py, models/user.py, models/place.py`

Done?  Check your code

### 10. DBStorage - Amenity... and BOOM!

mandatory

Update  `Amenity`: (`models/amenity.py`)

-   `Amenity`  inherits from  `BaseModel`  and  `Base`  (respect the order)
-   Add or replace in the class  `Amenity`:
    -   class attribute  `__tablename__`
        -   represents the table name,  `amenities`
    -   class attribute  `name`
        -   represents a column containing a string (128 characters)
        -   can’t be null
    -   class attribute  `place_amenities`  must represent a relationship  [Many-To-Many](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html "Many-To-Many")  between the class  `Place`  and  `Amenity`. Please see below more detail:  `place_amenity`  in the  `Place`  update

Update  `Place`: (`models/place.py`)

-   Add an instance of  [SQLAlchemy Table](https://docs.sqlalchemy.org/en/13/core/metadata.html "SQLAlchemy Table")  called  `place_amenity`  for creating the relationship  [Many-To-Many](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html "Many-To-Many")  between  `Place`  and  `Amenity`:
    -   table name  `place_amenity`
    -   `metadata = Base.metadata`
    -   2 columns:
        -   `place_id`, a string of 60 characters foreign key of  `places.id`, primary key in the table and never null
        -   `amenity_id`, a string of 60 characters foreign key of  `amenities.id`, primary key in the table and never null
-   Update  `Place`  class:
    -   for  `DBStorage`: class attribute  `amenities`  must represent a relationship with the class  `Amenity`  but also as  `secondary`  to  `place_amenity`  with option  `viewonly=False`  (`place_amenity`  has been define previously)
    -   for  `FileStorage`:
        -   Getter attribute  `amenities`  that returns the list of  `Amenity`  instances based on the attribute  `amenity_ids`  that contains all  `Amenity.id`  linked to the  `Place`
        -   Setter attribute  `amenities`  that handles  `append`  method for adding an  `Amenity.id`  to the attribute  `amenity_ids`. This method should accept only  `Amenity`  object, otherwise, do nothing.

### What’s a  `Many-to-Many`  relationship?

In our system, we don’t want to duplicate amenities (for example, having 10000 time the amenity  `Wifi`), so they will be unique. But, at least 2 places can have the same amenity (like  `Wifi`  for example). We are in the case of:

-   an amenity can be linked to multiple places
-   a place can have multiple amenities

=  `Many-To-Many`

To make this link working, we will create a third table called  `place_amenity`  that will create these links.

And you are good, you have a new engine!

```
guillaume@ubuntu:~/AirBnB_v2$ cat main_place_amenities.py 
#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py
OK
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM amenities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 47321eb8-152a-46df-969a-440aa67a6d59
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Cable
*************************** 2. row ***************************
        id: 4a307e7f-68f9-438f-81c0-8325898dda2a
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Oven
*************************** 3. row ***************************
        id: b80aec52-d0c9-420a-8471-3254572954b6
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Wifi
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 1
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
*************************** 2. row ***************************
              id: db549ae1-4500-4d0c-9b50-4b4978ed229e
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 2
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM place_amenity\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 2. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 3. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 4a307e7f-68f9-438f-81c0-8325898dda2a
*************************** 4. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
*************************** 5. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
guillaume@ubuntu:~/AirBnB_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `models/amenity.py, models/place.py`

Done?  Check your code



# 0x03. AirBnB clone - Deploy static

### Concepts

_For this project, we expect you to look at these concepts:_

-   [CI/CD](https://intranet.alxswe.com/concepts/43)
# CI/CD

The lean/agile methodology (See:  [Twelve Principles of Agile Software](https://agilemanifesto.org/principles.html "Twelve Principles of Agile Software")) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

-   code
-   ship your code
-   measure the impact
-   learn from it
-   fix or improve it
-   start over

As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/75dbe73200b7537f462b0dd81ad010b7840436d8.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120426Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c9d906d5ff9372fdd6ca66620f663b18803759cf989dc40580f0800cb24188d8)

Applied to software engineering,  [CI/CD](https://digital.ai/catalyst-blog/walk-before-you-run-understanding-ci-in-cd/ "CI/CD")  (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

-   Shipping the code:
    -   Capistrano, Fabric
-   Encapsulating the code
    -   Docker, Packer
-   Testing the code
    -   Jenkins, CircleCi, Travis
-   Measuring the code
    -   Datadog, Newrelic, Wavefront
-   [AirBnB clone](https://intranet.alxswe.com/concepts/74)
# AirBnB clone

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=516bf6da24f9a2e5a214126edef1800bc05784339154b58e9e50d0f3de50f3c1)

I know you were waiting for it: it’s here!

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the  [AirBnB website](https://www.airbnb.com/ "AirBnB website").

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

-   A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-   A website (the front-end) that shows the final product to everybody: static and dynamic
-   A database or files that store data (data = objects)
-   An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Final product

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8b19ae4f58813a3369b2ef27d7793195cab2bc2b4d29323ba166800231381e65)  ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/da2584da58f1d99a72f0a4d8d22c1e485468f941.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9f168d89f3a52f12315aca0df62becf8a9279f57b672448b4773aecc049e04af)

## Concepts to learn

-   [Unittest](https://docs.python.org/3.4/library/unittest.html#module-unittest "Unittest")  - and please work all together on tests cases
-   **Python packages**  concept page
# Python packages

Read:  [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages "Packages")

A Python file can be a  **module**  but when this file is in a folder, we call this folder a  **package**.

File organization is really important in a big project. This means for Python: packages everywhere.

### Compare with C

(file organization, not prototype vs code etc.)

In C:  `#include "abs.h"`

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

In C:  `#include "my_math/abs.h"`

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

How can I use my function  `my_abs(a)`  from the file  `abs.py`  in  `my_script.py`?

-   `import my_math/abs.py`  => NO
-   `import my_math/abs`  => NO
-   `import my_math.abs.py`  => NO
-   `import my_math.abs`  => YES but you will use your function like that:  `my_math.abs.my_abs(89)`  => not friendly
-   `from my_math.abs import my_abs`  => YES YES YES! now you can use your function like that:  `my_abs(89)`

Wait, does this really work?

NO! something is missing: the magic file  `__init__.py`

Indeed, each folder  **must**  contain this file to be considered a package.

This file should be empty except if you want to import all the content of modules by using  `*`.

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

How can I use my function  `my_add(a, b)`  from the file  `add.py`  in  `my_script.py`?

`from my_math.functions.add import my_add`

Easy right?

### `import *`  is dangerous

Using  `import *`  is still considered bad practice in production code. In that case,  `__init__.py`  shouldn’t be empty but must contain the list of modules to load:

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

$ cat my_math/__init__.py  # empty file
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

`positive.py`  contains one function  `def is_positive(n)`  and this function uses  `my_abs(n)`. How it’s possible?

By importing:  `from my_math.abs import my_abs`  or  `from abs import my_abs`

What the difference?

-   `from abs import my_abs`  is using a relative path between your file who imports and the module to import
-   `from my_math.abs import my_abs`  is using an absolute path between the file you execute and the module to import

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

Now, let’s execute a file in  `my_math`:

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
-   Serialization/Deserialization
-   `*args, **kwargs`
-   `datetime`
-   More coming soon!

## Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The console

-   create your data model
-   manage (create, update, destroy, etc) objects via a console / command interpreter
-   store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f6748d7b7391efc1e4c161c5b068ffd274c672726c7650449ed0d8ec5afb1959)

### Web static

-   learn HTML/CSS
-   create the HTML of your application
-   create template of each object

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b47abd9a97d03865abe242aa1f5d1d8bbd68cd327184827127381b9a6e9a7cfa)

### MySQL storage

-   replace the file storage by a Database storage
-   map your models to a table in database by using an O.R.M.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0130226e0c8d531484eb1f480264ed449b25fa8b4d5443b58bcb0433898e07e0)

### Web framework - templating

-   create your first web server in Python
-   make your static HTML file dynamic by using objects stored in a file or database

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8a405466316a17c873a0a0e5f698e9cc086d9b719ee7efa41790e9ef9024e4ed)

### RESTful API

-   expose all your objects stored via a JSON web interface
-   manipulate your objects via a RESTful API

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=28034b88f93a39d8a9bb9a66b323dfdb248cb2d45d9d7836b15eb3198b9d0ba9)

### Web dynamic

-   learn JQuery
-   load objects from the client side by using your own RESTful API

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6ea04ad7e88048b9227bd6f61b1364c3984a729c7b4c95abd4dc3dc7ad231720)

## Files and Directories

-   `models`  directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
-   `tests`  directory will contain all unit tests.
-   `console.py`  file is the entry point of our command interpreter.
-   `models/base_model.py`  file is the base class of all our models. It contains common elements:
    -   attributes:  `id`,  `created_at`  and  `updated_at`
    -   methods:  `save()`  and  `to_json()`
-   `models/engine`  directory will contain all storage classes (using the same prototype). For the moment you will have only one:  `file_storage.py`.

## Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

-   Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
-   Provide default value of any attribute
-   In the future, provide the same model behavior for file storage or database storage

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

First, let’s look at  `save(students)`:

-   Can I write each  `Student`  object to a file =>  _NO_, it will be the memory representation of the object. For another program execution, this memory representation can’t be reloaded.
-   Can I write each  `Student.name`  to a file =>  _YES_, but imagine you have other attributes to describe  `Student`? It would start to be become too complex.

The best solution is to convert this list of  `Student`  objects to a JSON representation.

Why JSON? Because it’s a standard representation of object. It allows us to share this data with other developers, be human readable, but mainly to be understood by another language/program.

Example:

-   My Python program creates  `Student`  objects and saves them to a JSON file
-   Another Javascript program can read this JSON file and manipulate its own  `Student`  class/representation

And the  `reload()`? now you know the file is a JSON file representing all  `Student`  objects. So  `reload()`  has to read the file, parse the JSON string, and re-create  `Student`  objects based on this data-structure.

### File storage == JSON serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure:

-   convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method  `my_instance.to_json()`  to retrieve a dictionary
-   convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a  `my_string = JSON.dumps(my_dict)`
-   write this string to a file on disk

And the process of deserialization?

The same but in the other way:

-   read a string from a file on disk
-   convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a  `my_dict = JSON.loads(my_string)`
-   convert this data structure to instance - for us it will be a  `my_instance = MyObject(my_dict)`

## `*args, **kwargs`

[How To Use them](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3 "How To Use them")

How do you pass arguments to a function?

```
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")

```

But with this function definition, you must call  `my_fct`  with 2 parameters, no more, no less.

Can it be dynamic? Yes you can:

```
def my_fct(*args, **kwargs):
    ...

my_fct("Best", "School")

```

What? What’s  `*args`  and  `**kwargs`?

-   `*args`  is a Tuple that contains all arguments
-   `*kwargs`  is a dictionary that contains all arguments by key/value

A dictionary? But why?

So, to make it clear,  `*args`  is the list of anonymous arguments, no name, just an order.  `**kwargs`  is the dictionary with all named arguments.

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

## `datetime`

`datetime`  is a Python module to manipulate date, time etc…

In this example, you create an instance of  `datetime`  with the current date and time:

```
from datetime import datetime

date_now = datetime.now()
print(type(date_now)) # <class 'datetime.datetime'>
print(date_now) # 2017-06-08 20:42:42.170922

```

`date_now`  is an object, so you can manipulate it:

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

What? What’s this format when a  `datetime`  instance is in a datastructure??? It’s unreadable.

How to make it readable:  [strftime](https://strftime.org/ "strftime")

```
print(date_now.strftime("%A")) # Thursday
print(date_now.strftime("%A %d %B %Y at %H:%M:%S")) # Thursday 08 June 2017 at 20:42:42

```

## Data diagram

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120632Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8bd2e5b0acf1fb836245042ceee265727730c1ba77b24beb9ce16dec564bbe94)

## Background Context

Ever since you completed project  [0x0F. Load balancer](https://github.com/OluTshegz/alx-system_engineering-devops/tree/master/0x0F-load_balancer "0x0F. Load balancer")  of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your  `web_static`  work. You will use  `Fabric`  (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via  `sudo`) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

Before starting, please fork the repository  `AirBnB_clone_v2`  from your partner if you don’t have it

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/288/aribnb_diagram_0.jpg?cache=off)

## Resources

**Read or watch**:

--   [How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments "How to use Fabric")
--   [How to use Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python "How to use Fabric in Python")
--   [Fabric and command line options](https://docs.fabfile.org/en/1.13/usage/fab.html "Fabric and command line options")
--   [CI/CD concept page](https://intranet.alxswe.com/rltoken/M_3lKmMAGA2KWujegl-ibA "CI/CD concept page")
# CI/CD

The lean/agile methodology (See:  [Twelve Principles of Agile Software](https://agilemanifesto.org/principles.html "Twelve Principles of Agile Software")) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

-   code
-   ship your code
-   measure the impact
-   learn from it
-   fix or improve it
-   start over

As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/75dbe73200b7537f462b0dd81ad010b7840436d8.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240503%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T120426Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c9d906d5ff9372fdd6ca66620f663b18803759cf989dc40580f0800cb24188d8)

Applied to software engineering,  [CI/CD](https://digital.ai/catalyst-blog/walk-before-you-run-understanding-ci-in-cd/ "CI/CD")  (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

-   Shipping the code:
    -   Capistrano, Fabric
-   Encapsulating the code
    -   Docker, Packer
-   Testing the code
    -   Jenkins, CircleCi, Travis
-   Measuring the code
    -   Datadog, Newrelic, Wavefront

--   [Nginx configuration for beginners](https://nginx.org/en/docs/beginners_guide.html "Nginx configuration for beginners")
--   [Difference between root and alias on NGINX](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/ "Difference between root and alias on NGINX")
In NGINX configuration, both `root` and `alias` directives are used to specify the location of static files served by your web server. However, they differ in how they determine the final path:

**Root:**

-   Defines the **document root**, the base directory from which NGINX serves files.
-   The location block's URL path is **appended** to the `root` directive to create the final path.
-   Use `root` when you want NGINX to follow the directory structure reflected in your URLs.

**Example:**

Nginx

```
root /var/www/html;

location /images/ {
    # Serves files from /var/www/html/images
}

```

Use code [with caution.](/faq#coding)

content_copy

In this example, a request for `/images/logo.png` will translate to the actual file path `/var/www/html/images/logo.png`.

**Alias:**

-   Creates an **alternate path** for a specific location block.
-   **Replaces** the location block's URL path with the `alias` directive.
-   Use `alias` when you want to serve files from a location that doesn't directly correspond to the URL structure.

**Example:**

Nginx

```
location /static/ {
    alias /var/www/assets/;
}

```

Use code [with caution.](/faq#coding)

content_copy

Here, a request for `/static/style.css` will be translated to `/var/www/assets/style.css` because the `/static/` part is replaced by the alias.

**Key Differences:**

-   **Path Construction:** `root` appends, `alias` replaces.
-   **URL Structure:** `root` maintains the URL structure, `alias` can create a different path structure.

**When to Use Which:**

-   Use `root` for your main document root and locations that directly reflect the directory hierarchy.
-   Use `alias` for serving static files from a non-standard location or for creating shortcuts within your URL structure.

--   [Fabric for Python 3](https://github.com/mathiasertl/fabric "Fabric for Python 3")
--   [Fabric Documentation](https://www.fabfile.org/ "Fabric Documentation")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"),  **without the help of Google**:

### General

-   What is Fabric
-   How to deploy code to a server easily
-   What is a  `tgz`  archive
-   How to execute Fabric command locally
-   How to execute Fabric command remotely
-   How to transfer files with Fabric
-   How to manage Nginx configuration
-   What is the difference between  `root`  and  `alias`  in a Nginx configuration

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using  `python3`  (version 3.4.0)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file at the root of the folder of the project is mandatory
-   Your code should use the  `PEP 8`  style (version  `1.7.*`)
-   Your Fabric file must work with  `Fabric 3`  version  `1.14.post1`  (installation instruction below)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Bash Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file at the root of the folder of the project is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass  `Shellcheck`  (version  `0.3.3-1~ubuntu20.04.1`  via  `apt-get`) without any errors
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

## More Info

### Install Fabric for Python 3 - version 1.14.post1

```
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1

```

### Video library(1  total)

Deploy static files with Fabric

### Quiz questions

**Great!**  You've completed the quiz successfully! Keep going!  (Show quiz)

## Tasks

### 0. Prepare your web servers

mandatory

Write a Bash script that sets up your web servers for the deployment of  `web_static`. It must:

-   Install Nginx if it not already installed
-   Create the folder  `/data/`  if it doesn’t already exist
-   Create the folder  `/data/web_static/`  if it doesn’t already exist
-   Create the folder  `/data/web_static/releases/`  if it doesn’t already exist
-   Create the folder  `/data/web_static/shared/`  if it doesn’t already exist
-   Create the folder  `/data/web_static/releases/test/`  if it doesn’t already exist
-   Create a fake HTML file  `/data/web_static/releases/test/index.html`  (with simple content, to test your Nginx configuration)
-   Create a symbolic link  `/data/web_static/current`  linked to the  `/data/web_static/releases/test/`  folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
-   Give ownership of the  `/data/`  folder to the  `ubuntu`  user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
-   Update the Nginx configuration to serve the content of  `/data/web_static/current/`  to  `hbnb_static`  (ex:  `https://mydomainname.tech/hbnb_static`). Don’t forget to restart Nginx after updating the configuration:
    -   Use  `alias`  inside your Nginx configuration
    -   [Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias "Tip")

Your program should always exit successfully.  **Don’t forget to run your script on both of your web servers.**

In optional, you will redo this task but by using Puppet

```
ubuntu@89-web-01:~/$ sudo ./0-setup_web_static.sh
ubuntu@89-web-01:~/$ echo $?
0
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 ubuntu ubuntu   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 ubuntu ubuntu 4096 Mar 7 22:29 releases
drwxr-xr-x 2 ubuntu ubuntu 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `0-setup_web_static.sh`

Done?  Check your code  Get a sandbox

### 1. Compress before sending

mandatory

Write a Fabric script that generates a  [.tgz](https://en.wikipedia.org/wiki/Tar_%28computing%29 ".tgz")  archive from the contents of the  `web_static`  folder of your AirBnB Clone repo, using the function  `do_pack`.

-   Prototype:  `def do_pack():`
-   All files in the folder  `web_static`  must be added to the final archive
-   All archives must be stored in the folder  `versions`  (your function should create this folder if it doesn’t exist)
-   The name of the archive created must be  `web_static_<year><month><day><hour><minute><second>.tgz`
-   The function  `do_pack`  must return the archive path if the archive has been correctly generated. Otherwise, it should return  `None`

```
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 1-pack_web_static.py do_pack 
Packing web_static to versions/web_static_20170314233357.tgz
[localhost] local: tar -cvzf versions/web_static_20170314233357.tgz web_static
web_static/
web_static/.DS_Store
web_static/0-index.html
web_static/1-index.html
web_static/100-index.html
web_static/2-index.html
web_static/3-index.html
web_static/4-index.html
web_static/5-index.html
web_static/6-index.html
web_static/7-index.html
web_static/8-index.html
web_static/images/
web_static/images/icon.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_group.png
web_static/images/icon_pets.png
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/images/logo.png
web_static/index.html
web_static/styles/
web_static/styles/100-places.css
web_static/styles/2-common.css
web_static/styles/2-footer.css
web_static/styles/2-header.css
web_static/styles/3-common.css
web_static/styles/3-footer.css
web_static/styles/3-header.css
web_static/styles/4-common.css
web_static/styles/4-filters.css
web_static/styles/5-filters.css
web_static/styles/6-filters.css
web_static/styles/7-places.css
web_static/styles/8-places.css
web_static/styles/common.css
web_static/styles/filters.css
web_static/styles/footer.css
web_static/styles/header.css
web_static/styles/places.css
web_static packed: versions/web_static_20170314233357.tgz -> 21283Bytes

Done.
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -l versions/web_static_20170314233357.tgz
-rw-rw-r-- 1 guillaume guillaume 21283 Mar 14 23:33 versions/web_static_20170314233357.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `1-pack_web_static.py`

Done?  Check your code  Get a sandbox

### 2. Deploy archive!

mandatory

Write a Fabric script (based on the file  `1-pack_web_static.py`) that distributes an archive to your web servers, using the function  `do_deploy`:

-   Prototype:  `def do_deploy(archive_path):`
-   Returns  `False`  if the file at the path  `archive_path`  doesn’t exist
-   The script should take the following steps:
    -   Upload the archive to the  `/tmp/`  directory of the web server
    -   Uncompress the archive to the folder  `/data/web_static/releases/<archive filename without extension>`  on the web server
    -   Delete the archive from the web server
    -   Delete the symbolic link  `/data/web_static/current`  from the web server
    -   Create a new the symbolic link  `/data/web_static/current`  on the web server, linked to the new version of your code (`/data/web_static/releases/<archive filename without extension>`)
-   All remote commands must be executed on your both web servers (using  `env.hosts = ['<IP web-01>', 'IP web-02']`  variable in your script)
-   Returns  `True`  if all operations have been done correctly, otherwise returns  `False`
-   You must use this script to deploy it on your servers:  `xx-web-01`  and  `xx-web-02`

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex:  `env.user =...`)

**Disclaimer:**  commands execute by Fabric displayed below are linked to the way we implemented the archive function  `do_pack`  - like the  `mv`  command - depending of your implementation of it, you may don’t need it

```
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key -u ubuntu
[52.55.249.213] Executing task 'do_deploy'
[52.55.249.213] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[52.55.249.213] run: rm -rf /data/web_static/current
[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!
[54.157.32.137] Executing task 'deploy'
[54.157.32.137] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[54.157.32.137] run: rm -rf /data/web_static/current
[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!

Done.
Disconnecting from 54.157.32.137... done.
Disconnecting from 52.55.249.213... done.
guillaume@ubuntu:~/AirBnB_clone_v2$ 
guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">Holberton School</p>
        </footer>
    </body>
</html>
guillaume@ubuntu:~/AirBnB_clone_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `2-do_deploy_web_static.py`

Done?  Check your code  Get a sandbox

### 3. Full deployment

mandatory

Write a Fabric script (based on the file  `2-do_deploy_web_static.py`) that creates and distributes an archive to your web servers, using the function  `deploy`:

-   Prototype:  `def deploy():`
-   The script should take the following steps:
    -   Call the  `do_pack()`  function and store the path of the created archive
    -   Return  `False`  if no archive has been created
    -   Call the  `do_deploy(archive_path)`  function, using the new path of the new archive
    -   Return the return value of  `do_deploy`
-   All remote commands must be executed on both of web your servers (using  `env.hosts = ['<IP web-01>', 'IP web-02']`  variable in your script)
-   You must use this script to deploy it on your servers:  `xx-web-01`  and  `xx-web-02`

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

```
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
[52.55.249.213] Executing task 'deploy'
Packing web_static to versions/web_static_20170315015620.tgz
[localhost] local: tar -cvzf versions/web_static_20170315015620.tgz web_static
web_static/
web_static/0-index.html
web_static/1-index.html
web_static/100-index.html
web_static/2-index.html
web_static/3-index.html
web_static/4-index.html
web_static/5-index.html
web_static/6-index.html
web_static/7-index.html
web_static/8-index.html
web_static/images/
web_static/images/icon.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_group.png
web_static/images/icon_pets.png
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/images/logo.png
web_static/index.html
web_static/styles/
web_static/styles/100-places.css
web_static/styles/2-common.css
web_static/styles/2-footer.css
web_static/styles/2-header.css
web_static/styles/3-common.css
web_static/styles/3-footer.css
web_static/styles/3-header.css
web_static/styles/4-common.css
web_static/styles/4-filters.css
web_static/styles/5-filters.css
web_static/styles/6-filters.css
web_static/styles/7-places.css
web_static/styles/8-places.css
web_static/styles/common.css
web_static/styles/filters.css
web_static/styles/footer.css
web_static/styles/header.css
web_static/styles/places.css
web_static packed: versions/web_static_20170315015620.tgz -> 27280335Bytes
[52.55.249.213] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: rm /tmp/web_static_20170315015620.tgz
[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
[52.55.249.213] run: rm -rf /data/web_static/current
[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
New version deployed!
[54.157.32.137] Executing task 'deploy'
[54.157.32.137] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: rm /tmp/web_static_20170315015620.tgz
[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
[54.157.32.137] run: rm -rf /data/web_static/current
[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
New version deployed!

Done.
Disconnecting from 54.157.32.137... done.
Disconnecting from 52.55.249.213... done.
guillaume@ubuntu:~/AirBnB_clone_v2$ 
guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">Holberton School</p>
        </footer>
    </body>
</html>
guillaume@ubuntu:~/AirBnB_clone_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `3-deploy_web_static.py`

Done?  Check your code  Get a sandbox

### 4. Keep it clean!

#advanced

Write a Fabric script (based on the file  `3-deploy_web_static.py`) that deletes out-of-date archives, using the function  `do_clean`:

-   Prototype:  `def do_clean(number=0):`
-   `number`  is the number of the archives, including the most recent, to keep.
    -   If  `number`  is 0 or 1, keep only the most recent version of your archive.
    -   if  `number`  is 2, keep the most recent, and second most recent versions of your archive.
    -   etc.
-   Your script should:
    -   Delete all unnecessary archives (all archives minus the number to keep) in the  `versions`  folder
    -   Delete all unnecessary archives (all archives minus the number to keep) in the  `/data/web_static/releases`  folder of both of your web servers
-   All remote commands must be executed on both of your web servers (using the  `env.hosts = ['<IP web-01>', 'IP web-02']`  variable in your script)

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

```
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015414.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015448.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 100-clean_web_static.py do_clean:number=2 -i my_ssh_private_key -u ubuntu > /dev/null 2>&1
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `100-clean_web_static.py`

Done?  Check your code  Get a sandbox

### 5. Puppet for setup

#advanced

Redo the task #0 but by using Puppet:

```
ubuntu@89-web-01:~/$ puppet apply 101-setup_web_static.pp
....
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 root root   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 root root 4096 Mar 7 22:29 releases
drwxr-xr-x 2 root root 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ 

```

**Repo:**

-   GitHub repository:  `AirBnB_clone_v2`
-   File:  `101-setup_web_static.pp`

Done?  Check your code




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

-   Add a public method  `def close(self):`: call  `remove()`  method on the private session attribute (`self.__session`)  [tips](https://intranet.alxswe.com/rltoken/_lTxhB5UgQ4nFRoS9ooI5g "tips")  or  `close()`  on the class  `Session`  [tips](https://intranet.alxswe.com/rltoken/xlPf9pDUFMb599rkoDElvg "tips")

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
        -   `UL`  tag: with the list of all  `State`  objects present in  `DBStorage`  **sorted by  `name`**  (A->Z)  [tip](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ "tip")
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
    -   `/hbnb_filters`: display a HTML page like  `6-index.html`, which was done during the project  [0x01. AirBnB clone - Web static](https://intranet.alxswe.com/rltoken/EG-iGbr_iPTlHrQQSNho1g "0x01. AirBnB clone - Web static")
        -   Copy files  `3-footer.css`,  `3-header.css`,  `4-common.css`  and  `6-filters.css`  from  `web_static/styles/`  to the folder  `web_flask/static/styles`
        -   Copy files  `icon.png`  and  `logo.png`  from  `web_static/images/`  to the folder  `web_flask/static/images`
        -   Update  `.popover`  class in  `6-filters.css`  to allow scrolling in the popover and a max height of 300 pixels.
        -   Use  `6-index.html`  content as source code for the template  `10-hbnb_filters.html`:
            -   Replace the content of the  `H4`  tag under each filter title (`H3`  States and  `H3`  Amenities) by  `&nbsp;`
        -   `State`,  `City`  and  `Amenity`  objects must be loaded from  `DBStorage`  and  **sorted by name**  (A->Z)
-   You must use the option  `strict_slashes=False`  in your route definition
-   Import this  [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql "10-dump")  to have some data

**IMPORTANT**

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
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
    -   `/hbnb`: display a HTML page like  `8-index.html`, done during the  [0x01. AirBnB clone - Web static](https://intranet.alxswe.com/rltoken/EG-iGbr_iPTlHrQQSNho1g "0x01. AirBnB clone - Web static")  project
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

-   Make sure you have a running and valid  `setup_mysql_dev.sql`  in your  `AirBnB_clone_v2`  repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
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
