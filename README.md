# api-consumer-demo

A typed v1 customer API client. Tests demonstrate successful v1 parsing, rejection of the v2 field rename, and HTTP failure handling. The consumer MCP server is planned.

Part of [API Contract Copilot](https://github.com/r-kovalenko/api-contract-copilot). Features and tasks are tracked in the shared GitHub Project and this repository's issues.

## Run and test

Requires Python 3.12.

```sh
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m ruff format --check .
python -m pytest --cov=app
python -m uvicorn app.main:app --reload
```

The health endpoint is `/health`.

The integration entry point is `app/client.py`. Inject an `httpx.Client` configured with the provider base URL. Tests use an in-memory mock transport, so no network or running provider is required.

## CI and delivery

Pull requests run lint, formatting, pytest with coverage, and container build/smoke tests. Successful main-branch builds publish `ghcr.io/r-kovalenko/api-consumer-demo:<commit-sha>`. No server deployment or paid model calls are configured. See [delivery details](https://github.com/r-kovalenko/api-contract-copilot/blob/main/docs/ci-cd.md).

Build locally: `docker build -t api-consumer-demo .`, then `docker run --rm -p 8000:8000 api-consumer-demo`.

Public visibility does not grant an open-source license; owner selection is pending.
