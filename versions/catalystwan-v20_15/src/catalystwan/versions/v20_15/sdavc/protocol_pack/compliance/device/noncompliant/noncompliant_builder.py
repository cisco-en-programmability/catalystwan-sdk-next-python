# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import CompliantDeviceRequest


class NoncompliantBuilder:
    """
    Builds and executes requests for operations under /sdavc/protocol-pack/compliance/device/noncompliant
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_non_compliant_devices_for_protocol_pack_1(self):
        class get_non_compliant_devices_for_protocol_pack_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[CompliantDeviceRequest] = None, **kw):
                """
                Get all non compliant devices for given protocol pack and selected device or entire network

                :param payload: Request Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/sdavc/protocol-pack/compliance/device/noncompliant",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> CompliantDeviceRequest:
                return CompliantDeviceRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[CompliantDeviceRequest]:
                return CompliantDeviceRequest

        return get_non_compliant_devices_for_protocol_pack_1_(self._request_adapter)

    def get_non_compliant_devices_for_protocol_pack(
        self, protocol_pack_name: str, **kw
    ):
        """
        Get all non compliant devices for given protocol pack

        :param protocol_pack_name: Protocol pack name
        :returns: None
        """
        params = {
            "protocolPackName": protocol_pack_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/sdavc/protocol-pack/compliance/device/noncompliant/{protocolPackName}",
            params=params,
            **kw,
        )
