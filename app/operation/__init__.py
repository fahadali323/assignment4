# operations.py

class Operation:
    """
    Fahad Ali - IS601 - Assignment 4
    Base class for all operations.
    """
    @staticmethod
    def addition(a: float, b: float) -> float:
        return a + b # Adds two numbers and returns results
    
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        return a - b # Subtract second number from first and returns result

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        return a * b # Multiplies two numbers and returns result
    
    @staticmethod
    def division(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.") # Raises an error if division by zero is attempted
        return a / b # Divides a by b and returns result