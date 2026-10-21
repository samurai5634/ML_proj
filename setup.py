from setuptools import find_packages,setup
from typing import List
EXCLUDE = '-e .'

def get_req(path:str) -> List[str]:
    """ 
    This function is used for getting requirements of the project dynamically
    and building dependencies 
    """
    
    with open(path,'r') as file_obj:
        req = [line.rstrip("\n") for line in file_obj]
        if EXCLUDE in req:
            req.remove(EXCLUDE)

    return req

setup(name="ML_project",
      author="Sarthak",
      author_email="sarthaksahu235@gmail.com",
      version='0.0.1',
      packages=find_packages(),
      install_requires=get_req('req.txt'),
      )