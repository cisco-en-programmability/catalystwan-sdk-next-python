import os
import pytest

from catalystwan.core.session import create_manager_session
from catalystwan.core.request_adapter import RequestAdapter

@pytest.fixture(scope="package")
def catalystwan_requests():
    host = os.environ["SDWAN_HOST"]
    port = int(os.environ["SDWAN_PORT"])
    username = os.environ["SDWAN_USERNAME"]
    password = os.environ["SDWAN_PASSWORD"]
    print(f"Connecting to {host}:{port}...")
    with create_manager_session(host, username, password, port) as session:
        session.request_timeout = 60
        yield RequestAdapter(session=session)
