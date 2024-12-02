# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import LicenseUplodFile


class SyncLicensesBuilder:
    """
    Builds and executes requests for operations under /smartLicensing/syncLicenses
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def sync_licenses(self):
        class sync_licenses_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[LicenseUplodFile] = None, **kw) -> Any:
                """
                get all licenses for sa/va

                :param payload: Partner
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "syncLicenses")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/smartLicensing/syncLicenses",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> LicenseUplodFile:
                return LicenseUplodFile(*args, **kwargs)

            @property
            def payload_model(self) -> Type[LicenseUplodFile]:
                return LicenseUplodFile

        return sync_licenses_(self._request_adapter)
