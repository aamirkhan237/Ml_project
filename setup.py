from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requriments(file_path:str)->List[str]:
    """
    this fun will return the list of requriments
    """
    requriments=[]

    with open(file_path) as file_obj:
        requriments=file_obj.readlines()
        requriments=[req.replace("\n",'')for req in requriments]
        if HYPEN_E_DOT in requriments:
            requriments.remove(HYPEN_E_DOT)


setup(
    name='mlproject',
    version='0.0.1',
    author='Aamirkhan',
    author_email='pathanaamirkhan237@gmail.com',
    packages=find_packages(),
    install_requires=get_requriments('requriments.txt')
)