#!/usr/bin/env python
import argparse

import uvicorn


def run(app_module: str = "{{cookiecutter.project_slug_code}}.main:app"):
    parser = argparse.ArgumentParser(description="Run FastAPI application.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to run the server on")
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to run the server on"
    )
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    parser.add_argument(
        "--log-level",
        default="info",
        choices=["critical", "error", "warning", "info", "debug", "trace"],
        help="Log level for uvicorn",
    )

    # Allow additional arguments to be passed and forwarded to uvicorn
    # parser.add_argument(
    #     "extra_args", nargs=argparse.REMAINDER, help="Extra arguments for uvicorn"
    # )

    args = parser.parse_args()

    uvicorn.run(
        app_module,
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level=args.log_level,
    )


if __name__ == "__main__":
    run()
