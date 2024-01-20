from setuptools import setup,find_packages
from typing import List




PROJECT_NAME = "Housing-Predictor"
VERSION = "0.0.2"
AUTHOR = "Mujahid Jamadar"
DESCRIPTION = "This is Housing-Predictor project"

REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return a list of requirements mentioned
    in the requirements.txt file.

    return: This function returns a List which contains the names of libraries
    mentioned in the requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        # Use list comprehension to strip each line and create a list of requirements
        return [line.strip() for line in requirement_file.readlines()].remove("-e .")

# Setup function
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),       #["housing"] folder in which __init__.py file
    install_requires=get_requirements_list()
)


