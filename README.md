0x00. AirBnB clone - The console

AirBNB project: The console, web static, MySQL storage, web framework-templating, RESTful API, web dynamic. 

FILES & DIRECTORIES:
- models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- tests directory will contain all unit tests.
- console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
	> attributes: id, created_at and updated_at
	> methods: save() and to_json()
- models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py

After 4 months, you will have a complete web application composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
