# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import DeleteAllListsBody


class DeleteAllListsBuilder:
    """
    Builds and executes requests for operations under /template/policy/ise/identity/deleteAllLists
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def delete_all_lists(self):
        class delete_all_lists_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[DeleteAllListsBody] = None, **kw
            ) -> bool:
                """
                Delete all lists of the specified list type

                :param payload: type of list
                :returns: bool
                """
                return self._request_adapter.request(
                    "DELETE",
                    "/dataservice/template/policy/ise/identity/deleteAllLists",
                    return_type=bool,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> DeleteAllListsBody:
                return DeleteAllListsBody(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DeleteAllListsBody]:
                return DeleteAllListsBody

        return delete_all_lists_(self._request_adapter)
