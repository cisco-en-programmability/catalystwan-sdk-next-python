# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Type
from catalystwan.abc import RequestAdapterInterface
from .models import StatusResponse
from .models import MapDevicesRequest


class UnmapBuilder:
    """
    Builds and executes requests for operations under /partner/{partnerType}/unmap
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def delete_device_mapping(self):
        class delete_device_mapping_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, partner_type: str, nms_id: str, payload: MapDevicesRequest, **kw
            ) -> StatusResponse:
                """
                Unmap a set of devices for the partner

                :param partner_type: Partner type
                :param nms_id: Nms id
                :param payload: List of devices
                :returns: StatusResponse
                """
                params = {
                    "partnerType": partner_type,
                    "nmsId": nms_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/partner/{partnerType}/unmap/{nmsId}",
                    return_type=StatusResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> MapDevicesRequest:
                return MapDevicesRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[MapDevicesRequest]:
                return MapDevicesRequest

        return delete_device_mapping_(self._request_adapter)
