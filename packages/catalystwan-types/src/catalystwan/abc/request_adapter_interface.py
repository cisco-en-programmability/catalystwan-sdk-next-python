from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Protocol, Type, TypeVar, Union

from typing_extensions import Self

from catalystwan.abc.types import HTTP_METHOD, JSON

if TYPE_CHECKING:
    from catalystwan.abc.session_interface import SessionInterface

ReturnType = TypeVar("ReturnType")
Payload = TypeVar("Payload")


class RequestAdapterInterface(Protocol):
    session: SessionInterface

    def request(
        self,
        method: HTTP_METHOD,
        url: str,
        payload: Union[Payload, JSON] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[ReturnType]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]: ...

    def get(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]: ...

    def put(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]: ...

    def post(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]: ...

    def delete(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]: ...

    def __copy__(self) -> Self: ...
