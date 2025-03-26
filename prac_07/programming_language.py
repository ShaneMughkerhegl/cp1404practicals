class ProgrammingLanguage:
    # Represent a programming language object.

    # Initialise the ProgrammingLanguage instance with provided attributes
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    # Return a readable string representation of the language
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, " \
               f"Year={self.year}, Pointer Arithmetic={self.pointer_arithmetic}"

    # Return True if the language is dynamically typed
    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

