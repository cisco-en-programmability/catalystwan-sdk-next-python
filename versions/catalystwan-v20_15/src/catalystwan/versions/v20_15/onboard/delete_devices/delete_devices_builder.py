# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import DeleteDetails, DeleteResponseInner


class DeleteDevicesBuilder:
    """
    Builds and executes requests for operations under /onboard/delete-devices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def delete_devices(self):
        class delete_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[DeleteDetails] = None, **kw
            ) -> List[DeleteResponseInner]:
                """
                Delete Manual Onboard Device details

                :param payload: Payload
                :returns: List[DeleteResponseInner]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/onboard/delete-devices",
                    return_type=List[DeleteResponseInner],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> DeleteDetails:
                return DeleteDetails(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DeleteDetails]:
                return DeleteDetails

        return delete_devices_(self._request_adapter)
