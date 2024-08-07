# Fundamentals of OOP 

We have 4 fundamentals for writing OOP in programming languages.
1., Inheritance: This is when a class A inherits the ppties and method of another class B. we pass the first class as a parameter to the second class, so it have public access to its attributes and method.
1., constructor is a method that we use to initialize the properties or variable that will be used in the class. The constructor is automatically called, anythime we create an object of the class. so we can have a method, and pass it as properties in the constructor as well.

1., The super(write_child_class_name_here).__init__(variable_name) is used in the child class that is inheriting the properties and method of the parent class, so we can have access to the constructor of the parent class. We pass all the parameter in the parent class constructor into the child class constructor, and the variable name into the super(write_varaible_namee). use the print method here. to see how it work, but you must create an object of the class, to get an output in the console. When a class B is inheriting, it just know all the features and propeties of the class A to use them as an additional functionalites for itself.

## Why Use super()
Using super() in the constructor of a subclass has several benefits:

### Code Reusability:

It allows you to reuse the initialization logic defined in the parent class without duplicating code.
If the parent class has complex initialization logic, you can simply call it rather than rewriting it in the subclass.

If you need to change the initialization logic of the parent class, you only need to update it in one place. The subclasses will automatically use the updated logic.
This makes the code easier to maintain and less error-prone.


## Encapsulation

There is possibility to restrict the access to the class methods and attributes. To aviod direct modification of the methods and attributes. When you have sensitive data, that user should not have access it, encapsulation does the job, you need to use a private attributes, then use public getter and setter  methdod to update/ access the value of the private attributes.

note: 
1., A private variables can only be accessed within the same class( another class cant access it directly) However, it is possible to access them if we provide public get and set methods.

1., For every private attributes, there has to be a getter and setter to be able to access it outside of the class.

### Encapsulation of Helper Functions:

If you have a small helper function that is only relevant within the context of a larger function, you can define it as a nested method. This keeps the helper function hidden from the rest of the class or module, reducing potential namespace pollution.

Breaking down a complex function into smaller parts can improve readability. Nested methods can help to logically segment different parts of a function, making it easier to follow and maintain.

When you have complex logic that needs to share some local state, nested methods can be useful. Since nested methods have access to the variables in their enclosing scope, they can naturally share state without the need for additional parameters.

### Static Methods


## Method overloading and overrriding

Method overriding in Python is straightforward and follows the principles of inheritance and polymorphism. When a childclass defines a method with the same name, parameters, and return type as a method in its superclass, it overrides the method in the parentclass. Method overriding is a key aspect of achieving polymorphism.

In statically typed languages like Java, method overloading allows multiple methods with the same name but different parameter lists (different types, numbers, or both). Python does not support method overloading in the same way. Instead, you can achieve similar functionality using default arguments or variable-length arguments (*args).


