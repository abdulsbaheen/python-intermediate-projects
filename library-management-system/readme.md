The parent class Library contains the basic features of a library such as:

Storing a list of books
Displaying available books
Adding new books
Borrowing books
Returning books

These functions are common for all types of libraries.

👨‍💻 Child Classes

Different specialized libraries are created using inheritance, such as:

comp_Library (Computer Library)
Other custom libraries (School, Kids, etc.)

These child classes:

Inherit all basic features from the parent class
Add their own specific book collections or features
Override methods like display_info() to show customized information
🔁 Use of Inheritance

Inheritance allows:

Code reuse (no need to rewrite functions)
Easy maintenance
Extension of features for different library types

For example, a computer library can have its own set of books while still using borrow and return functions from the main library class.

🎯 Project Outcome

This system demonstrates how real-world library systems can be built efficiently using OOP principles, making the code:

Organized
Reusable
Easy to extend
