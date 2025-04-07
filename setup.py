from setuptools import find_packages,setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return list of requirements

    """
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process eah line
            for line in lines:
                requirement = line.strip()
                #  ignore the empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirement.txt not found")

    return requirement_list


print(get_requirements())


setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="Abinash Mishra",
    author_email="starta@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)