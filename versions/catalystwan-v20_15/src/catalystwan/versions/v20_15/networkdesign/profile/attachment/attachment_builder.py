# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class AttachmentBuilder:
    """
    Builds and executes requests for operations under /networkdesign/profile/attachment
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def push_device_profile_template(self):
        class push_device_profile_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, profile_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Attach to device profile

                :param profile_id: Device profile Id
                :param payload: Device template
                :returns: Any
                """
                logging.warning(
                    "Operation: %s is deprecated", "pushDeviceProfileTemplate"
                )
                params = {
                    "profileId": profile_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/networkdesign/profile/attachment/{profileId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return push_device_profile_template_(self._request_adapter)
