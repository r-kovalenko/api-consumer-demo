import httpx
import pytest
from pydantic import ValidationError

from app.client import fetch_customer


def client_for(payload, status=200):
    def handle(request):
        assert request.url.path == "/v1/customers/1"
        return httpx.Response(status, json=payload)

    return httpx.Client(
        base_url="https://provider.example/v1/", transport=httpx.MockTransport(handle)
    )


def test_v1_customer_is_parsed():
    with client_for({"id": 1, "name": "Demo Customer"}) as client:
        assert fetch_customer(client, 1).name == "Demo Customer"


def test_v2_rename_is_an_explicit_compatibility_failure():
    with client_for({"id": 1, "full_name": "Demo Customer"}) as client:
        with pytest.raises(ValidationError, match="name"):
            fetch_customer(client, 1)


def test_http_errors_are_not_reported_as_success():
    with client_for({"detail": "Customer not found"}, status=404) as client:
        with pytest.raises(httpx.HTTPStatusError):
            fetch_customer(client, 1)
