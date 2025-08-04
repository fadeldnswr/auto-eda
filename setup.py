'''
This file is used for packaging and distributing
Python projects. It's used by setuptools to define
configuration of this project.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
  '''
  This function will return a
  list of requirements
  '''
  requirement_list: List[str] = []
  try:
    with open("requirements.txt", "r") as file:
      # Read lines from the file
      lines = file.readlines()
      
      # Process each line
      for line in lines:
        requirements = line.strip()
        # Ignore the empty line and -e .
        if requirements and requirements != "-e .":
          requirement_list.append(requirements)
  except FileNotFoundError:
    print("The requirements.txt file not found!")
  return requirement_list

# Define the setup for this project
setup(
  name="Auto-EDA",
  version="0.0.1",
  author=["Fadel Achmad Daniswara"],
  author_email=["daniswarafadel@gmail.com"],
  packages=find_packages(),
  install_requirements=get_requirements()
)