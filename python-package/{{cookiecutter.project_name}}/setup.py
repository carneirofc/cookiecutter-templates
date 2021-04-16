#!/usr/bin/env python3
from setuptools import setup, find_namespace_packages
from {{cookiecutter.project_name}} import __author__, __version__, __email__
import pkg_resources

def get_abs_path(relative):
  return pkg_resources.resource_filename(__name__, relative)

def main():
    with open(get_abs_path("README.md"), "r") as _f:
        long_description = _f.read().strip()

    with open(get_abs_path("requirements.txt"), "r") as _f:
        _requirements = _f.read().strip().split("\n")

    setup(
        author=__author__,
        author_email=__email__,
        classifiers=[
            "Programming Language :: Python :: 3",
        ],
        description="{{cookiecutter.project_description}}",
        download_url="https://github.com/{{cookiecutter.gh_owner}}/{{cookiecutter.project_name}}",
        license = "GPLv3",
        long_description=long_description,
        long_description_content_type="text/markdown",
        name="{{cookiecutter.project_name}}",
        url="https://github.com/{{cookiecutter.gh_owner}}/{{cookiecutter.project_name}}",
        version=__version__,
        install_requires=_requirements,
        include_package_data=True,
        packages=find_namespace_packages(include=["{{cookiecutter.project_name}}"]),
        python_requires=">=3.6",
        scripts=[],
        zip_safe=False,
    )

if __name__ == "__main__":
    main()

