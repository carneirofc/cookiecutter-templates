Description
-----------

![Linting and Static](https://github.com/{{cookiecutter.gh_owner}}/{{cookiecutter.project_slug}}/actions/workflows/lint.yml/badge.svg)
![Latest tag](https://img.shields.io/github/tag/{{cookiecutter.gh_owner}}/{{cookiecutter.project_slug}}.svg?style=flat)
[![Latest release](https://img.shields.io/github/release/{{cookiecutter.gh_owner}}/{{cookiecutter.project_slug}}.svg?style=flat)](https://github.com/{{cookiecutter.gh_owner}}/{{cookiecutter.project_slug}}/releases)
[![PyPI version fury.io](https://badge.fury.io/py/{{cookiecutter.project_slug}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_slug}}/)
[![Read the Docs](https://readthedocs.org/projects/spack/badge/?version=latest)](https://{{cookiecutter.gh_owner}}.github.io/{{cookiecutter.project_slug}}/)

{{cookiecutter.project_description}}

Development packages are listed at [requirements-dev.txt](requirements-dev.txt) and runtime dependencies at [requirements.txt](requirements.txt).

Development
-----------

Create a python virtual environment
```command
python -m venv .venv
source .venv/bin/activate
```

Install package and dev devpendencies
```command
pip install -e ./requirements.txt -e ./requirements-dev.txt
```


Author
------

{{cookiecutter.author_name}} - {{cookiecutter.author_user}} @ {{cookiecutter.author_email}}


Licence
-------

{{cookiecutter.project_slug}} licenced under {{cookiecutter.open_source_license}}
