# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import ReleaseLicenses


class ReleaseLicensesBuilder:
    """
    Builds and executes requests for operations under /v1/licensing/release-licenses
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def release_licenses(self):
        class release_licenses_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[ReleaseLicenses] = None, **kw):
                """
                Release licenses assigned to the devices

                :param payload: List of devices for releasing licenses
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/licensing/release-licenses",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ReleaseLicenses:
                return ReleaseLicenses(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ReleaseLicenses]:
                return ReleaseLicenses

        return release_licenses_(self._request_adapter)
