#!/usr/bin/env python3
from setuptools import find_packages, setup
# Import package metadata from the package's __init__.py file
from src.{{cookiecutter.project_slug_code}} import (_author_, _description_,
                                                    _email_, _version_)

# Read dependencies from requirements.txt
with open("requirements.txt", "r") as requirements_file:
    install_requires = [line.strip() for line in requirements_file if line.strip()]

# Read README.md contents and append to the description
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme_contents = readme_file.read()
_description_ += "\n\n" + readme_contents

_name_ = "{{ cookiecutter.project_slug_code }}"
setup(
    name=_name_,
    version=_version_,
    author=_author_,
    author_email=_email_,
    description=_description_,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            f"{_name_}= src.{{ cookiecutter.project_slug_code }}.scripts:run",
        ],
    },
)
