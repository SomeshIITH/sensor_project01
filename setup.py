from setuptools import find_packages,setup
from typing import List

hyphen_e='-e.'
def get_requirements(file_path : str)->List[str]:
    requirements= []
    with open(file_path) as file_obj:
        requirements=[req.replace("/n","") for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements
setup(
    name = 'Fault detection',
    version = '0.0.1',
    author = " Somesh",
    install_requirements = get_requirements("requirements.txt"),
    packages = find_packages()
)