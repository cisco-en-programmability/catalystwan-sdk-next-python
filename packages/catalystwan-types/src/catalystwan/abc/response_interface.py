from typing import Protocol
from collections.abc import Mapping


class ResponseInterface(Protocol):
    """
    Interface to response object. Fits "requests.Response"
    but set of methods is minimal to allow easy migration to another client if needed
    """

    @property
    def headers(self) -> Mapping: ...

    @property
    def text(self) -> str: ...

    @property
    def content(self) -> bytes: ...

    def json(self) -> dict: ...
