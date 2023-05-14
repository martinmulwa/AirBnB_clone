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

#### Commands

| Command                                                       | Description                                                                                   |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| help `[command]`                                              | Displays all available commands and provides documentation                                    |
| quit                                                          | Exits the program                                                                             |
| EOF                                                           | Exits the program                                                                             |
| create `class_name`                                           | Creates a new instance of the class `class_name`                                              |
| show `class_name` `id`                                        | Prints the string representation of an instance based on the `class_name` and `id`            |
| destroy `class_name` `id`                                     | Deletes an instance based on the `class_name` and `id`                                        |
| all `[class_name]`                                            | Prints the string representation of all instances based or not on the `class_name`            |
| update `class_name` `id` `attribute_name` `"attribute_value"` | Updates an instance based on the `class_name` and `id` by adding or updating `attribute_name` |

### Models

The folder [models](./models/) contains all the data models used in this project defined as classes.

| File                                    | Description                               |
| --------------------------------------- | ----------------------------------------- |
| [base_model.py](./models/base_model.py) | BaseModel class for all the other classes |
| [user.py](./models/user.py)             | User class for user data                  |
| [amenity.py](./models/amenity.py)       | Amenity class for amenity data            |
| [city.py](./models/city.py)             | City class for city location data         |
| [state.py](./models/state.py)           | State class for state location data       |
| [place.py](./models/place.py)           | Place class for accommodation data        |
| [review.py](./models/review.py)         | Review class for user/host review data    |

### File storage

The folder [engine](./models/engine/) manages the serialization and deserialization of all the data, following a JSON format.

A FileStorage class is defined in [file_storage.py](./models/engine/file_storage.py) with methods to follow this flow:
`<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>`

The [**init**.py](./models/__init__.py) file contains the instantiation of the FileStorage class called **storage**, followed by a call to the method reload() on that instance.
This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

### Tests

We use the `unittest` module in Python to test the code. The tests are located in the [tests](./tests/) folder.

To run the tests, navigate to the root of the project and run the following command:

```bash
python3 -m unittest discover tests
```

## Contributors

- [**Martin Pius**](https://github.com/martinmulwa)
- [**Alice Kiptui**](https://github.com/JEPTUI)
