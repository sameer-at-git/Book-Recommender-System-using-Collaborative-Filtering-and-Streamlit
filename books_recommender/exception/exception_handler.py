import os
import sys

class AppException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = AppException.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
        detailed_error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {error_message}"
        return detailed_error_message

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return AppException.__name__.str()