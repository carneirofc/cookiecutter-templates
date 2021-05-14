#!/usr/bin/env python3
import pkg_resources

from setuptools import setup, find_packages
from src.{{cookiecutter.project_slug}} import __author__, __version__, __email__

def get_abs_path(relative) -> str:
  return pkg_resources.resource_filename(__name__, relative)

def get_long_description() -> str:
    long_description = ""

    with open(get_abs_path("README.md"), "r") as _f:
        long_description += _f.read().strip()

    long_description += "\n\n"

    with open(get_abs_path("CHANGES.md"), "r") as _f:
        long_description += _f.read().strip()

    return long_description

def get_requirements() -> str:
    with open(get_abs_path("requirements.txt"), "r") as _f:
        return _f.read().strip().split("\n")

def main():
    long_description = get_long_description()

    requirements = get_requirements()

    setup(
        author=__author__,
        author_email=__email__,
        classifiers=[
            "Programming Language :: Python :: 3",
        ],
        description="{{cookiecutter.project_description}}",
        download_url="https://github.com/{{cookiecutter.gh_owner}}/{{cookiecutter.project_slug}}",
        license = "{{cookiecutter.open_source_license}}",
        long_description=long_description,
        long_description_content_type="text/markdown",
        name="{{cookiecutter.project_name}}",
        url="https://github.com/{{cookiecutter.gh_owner}}/{{cookiecutter.project_slug}}",
        version=__version__,
        install_requires=requirements,
        include_package_data=True,
        packages=find_packages(
            where="src",
            include=[
                "{{cookiecutter.project_slug}}*",
            ],
        ),
        package_dir={"": "src"},
        python_requires=">=3.6",
        scripts=[],
        zip_safe=False,
    )

if __name__ == "__main__":
    main()

