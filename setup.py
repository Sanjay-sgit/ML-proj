from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' 
#-e -> install packages in editable mode, later if we make any changes in any package that changes will updated in all packages so don't need to install
#again and again. .-> current directory.

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sanjay',
author_email='sanjay@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)