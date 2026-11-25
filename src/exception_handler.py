import sys
from logger import logging

# logger = logging.getLogger(__name__)

def error_message_details(error,error_details:sys):
    _,_,exc_err = error_details.exc_info()
    file_name = exc_err.tb_frame.f_code.co_filename
    err_message = "Error occured in file name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_err.tb_lineno,str(error))
    return err_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details)

    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.exception('Divide by Zero error occured')
        raise CustomException(e,sys)
    
   

    

    
