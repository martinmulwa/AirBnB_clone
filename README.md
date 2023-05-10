# AirBnB Clone

## Description

This is a team project that is part of the ALX Software Engineering Program curriculum.
The goal is to build the full web application: AirBnB Clone.

## 1. AirBnB Clone - The Console

![Console flow](/images/console.png)

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
