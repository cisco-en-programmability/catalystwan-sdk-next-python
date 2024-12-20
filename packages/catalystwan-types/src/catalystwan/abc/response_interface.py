import abc
from collections.abc import Mapping
from typing import Protocol


class ResponseInterface(Protocol):
    """
    Interface to response object. Fits "requests.Response"
    but set of methods is minimal to allow easy migration to another client if needed
    """

    @property
    @abc.abstractmethod
    def headers(self) -> Mapping: ...

    @property
    @abc.abstractmethod
    def text(self) -> str: ...

    @property
    @abc.abstractmethod
    def content(self) -> bytes: ...

    @abc.abstractmethod
    def json(self) -> dict: ...
