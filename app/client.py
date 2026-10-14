import httpx
from pydantic import BaseModel


class Customer(BaseModel):
    id: int
    name: str


def fetch_customer(client: httpx.Client, customer_id: int) -> Customer:
    """Consume v1; a v2 response should fail validation until migrated."""
    response = client.get(f"customers/{customer_id}")
    response.raise_for_status()
    return Customer.model_validate(response.json())
