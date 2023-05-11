# AirBnB Clone

![hbnb image](/images/hbnb.png)

## Description

This is a team project that is part of the ALX Software Engineering Program curriculum.
The goal is to build a full web application: AirBnB Clone.

## 1. AirBnB Clone - The Console

![Console flow image](/images/console.png)

This is the first step towards building the full web application: AirBnB Clone.

In this first step we:

- Create our data models
- Build a custom command-line interface(console) for data management
- Manage(create, update, destroy, etc) objects via the console
- Store and persist objects to a file (JSON file)

### Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell.

#### Interactive mode example

The shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

#### Non-interactive mode example

The shell should work like this in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Models

The folder [models](./models/) contains all the data models used in this project defined as classes.

| File                                    | Description                               |
| --------------------------------------- | ----------------------------------------- |
| [base_model.py](./models/base_model.py) | BaseModel class for all the other classes |

### Tests

We use the `unittest` module in Python to test the code. The tests are located in the [tests](./tests/) folder.

To run the tests, navigate to the root of the project and run the following command:

```bash
python3 -m unittest discover tests
```

## Contributors

- [**Martin Pius**](https://github.com/martinmulwa)
- [**Alice Kiptui**](https://github.com/JEPTUI)
