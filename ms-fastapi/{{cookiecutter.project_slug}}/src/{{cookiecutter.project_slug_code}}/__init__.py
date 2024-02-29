#!/usr/bin/env python
_version_: str = "{{ cookiecutter.project_version }}"
_author_: str = "{{ cookiecutter.author_name }}"
_email_: str = "{{ cookiecutter.author_email }}"
_description_: str = "{{ cookiecutter.project_description }}"

_api_title_: str = "{{ cookiecutter.project_name }} Microservice"
_api_description_: str = _description_
_api_version_: str = _version_
_api_docs_url_: str = "/swagger"
