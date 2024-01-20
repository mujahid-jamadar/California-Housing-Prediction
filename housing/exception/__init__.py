import os
import sys

class HousingException(Exception):
    """
    Custom exception class for housing-related application errors.

    Attributes:
    - error_message (str): Detailed error message including script name, line number, and original error message.

    Methods:
    - __init__(self, error_message: Exception, error_details: sys): Initializes the exception with error details.
    - get_detailed_error_message(error_message: Exception, error_details: sys) -> str: Generates a detailed error message.
    - __str__(self) -> str: Returns a string representation of the exception with the detailed error message.
    - __repr__(self) -> str: Returns a string representation of the class name.
    """

    def __init__(self, error_message: Exception, error_details: sys):
        """Initializes the exception with the provided error message and system information."""
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message, error_details)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys) -> str:
        """Generates a detailed error message including script name, line number, and original error message."""
        _, _, exec_tb = error_details.exc_info()
        line_number, file_name = exec_tb.tb_frame.f_lineno, exec_tb.tb_frame.f_code.co_filename
        return f"Error in script: [{file_name}] at line: [{line_number}] - {error_message}"

    def __str__(self) -> str:
        """Returns a string representation of the exception with the detailed error message."""
        return self.error_message

    def __repr__(self) -> str:
        """Returns a string representation of the class name."""
        return HousingException.__name__
