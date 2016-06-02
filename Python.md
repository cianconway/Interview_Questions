### Memory management
Memory is managed in Python in a private heap conmtaining all Python objects 
as data structures. The interpreter takes care of Python heap and the 
programmer has no access to it.

### Higher order function
Higher order function takes one or mor eother functions as input and returns
a new function.

### Copy object in Python
Shallow copy and deep copy

### Sending mail from Py script
SMTPlib 

### __init__
The __init__ function is called a constructor, or initializer, and is automatically called when you create a new instance of a class. Within that function, the newly created object is assigned to the parameter self . The notation self.legs is an attribute called legs of the object in the variable self 

### Mutable and Immutable
A mutable object can be changed after it's created, and an immutable object can't
Mutable objects allow you to make changes "in-place," without allocating a new object

### Python Scoping
L, Local — Names assigned in any way within a function (def or lambda)), and not declared global in that function.
E, Enclosing function locals — Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
G, Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError

### Anonymous function
An anonymous function is a function that is defined without a name

### Decorators
Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated. A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods

### Iteration
When you create a list, you can read its items one by one. Reading its items one by one is called iteration. When you use a list comprehension, you create a list, and so an iterable.
`mylist = [x*x for x in range(3)]`

### Generators
Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory, they generate the values on the fly

### Yield
Yield is a keyword that is used like return, except the function will return a generator.