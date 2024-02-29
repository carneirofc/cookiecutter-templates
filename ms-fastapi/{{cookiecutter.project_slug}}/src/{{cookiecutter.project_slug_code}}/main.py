# main.py
from fastapi import FastAPI
from {{cookiecutter.project_slug_code}} import (_api_description_,
                                                _api_docs_url_, _api_title_,
                                                _api_version_)
from {{cookiecutter.project_slug_code}}.controllers import healthz

app = FastAPI(
    title=_api_title_,
    description=_api_description_,
    version=_api_version_,
    docs_url=_api_docs_url_,
)

app.include_router(healthz.router, tags=["Health"])
