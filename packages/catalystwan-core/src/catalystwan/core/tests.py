import importlib
import logging
import os

import pytest
from catalystwan.core.request_adapter import RequestAdapter
from catalystwan.core.session import create_manager_session

logger = logging.getLogger(__name__)


@pytest.fixture(scope="package")
def catalystwan_requests():
    host = os.environ["SDWAN_HOST"]
    port = int(os.environ["SDWAN_PORT"])
    username = os.environ["SDWAN_USERNAME"]
    password = os.environ["SDWAN_PASSWORD"]
    logger.info(f"Connecting to {host}:{port}...")
    with create_manager_session(host, username, password, port) as session:
        session.request_timeout = 60
        yield RequestAdapter(session=session)


@pytest.fixture(scope="package")
def catalystwan_client_factory(catalystwan_requests):
    def wrapper(version: str):
        ver = version.replace(".", "_")
        name = f"catalystwan.versions.v{ver}.api_client"
        logger.info(f"Create {name}.ApiClient")
        module = importlib.import_module(name)
        ApiClient = getattr(module, "ApiClient")
        return ApiClient(catalystwan_requests)

    return wrapper


@pytest.fixture(scope="package")
def catalystwan_client(catalystwan_client_factory):
    version = os.environ["SDWAN_VERSION"]
    return catalystwan_client_factory(version)
