from contextlib import AbstractContextManager
from enum import Enum, auto
from typing import Optional, Protocol

from packaging.version import Version
from typing_extensions import Self

from catalystwan.abc import ResponseInterface


class SessionType(Enum):
    SINGLE_TENANT = auto()
    PROVIDER = auto()
    TENANT = auto()
    PROVIDER_AS_TENANT = auto()
    NOT_DEFINED = auto()


class SessionInterface(AbstractContextManager, Protocol):
    """
    Interface to client object.
    We only need a 'request' function and few vmanage session properties obtained from server.
    Matched to fit "requests.Session" but migration to other client is possible.
    At his point not very clean as injection of custom kwargs is possible (and sometimes used)
    """

    def request(self, method: str, url: str, **kwargs) -> ResponseInterface: ...

    @property
    def api_version(self) -> Version: ...

    @property
    def session_type(self) -> Optional[SessionType]: ...

    def login(self) -> Self: ...

    def close(self, *args) -> None: ...

    def __copy__(self) -> Self: ...
