# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class AuthenticateBuilder:
    """
    Builds and executes requests for operations under /template/cor/cloud/authenticate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def authenticate_cred_and_update(self):
        class authenticate_cred_and_update_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Authenticate and update cloud account credentials

                :param payload: Cloud account credential
                :returns: Any
                """
                logging.warning(
                    "Operation: %s is deprecated", "authenticateCredAndUpdate"
                )
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/cor/cloud/authenticate",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return authenticate_cred_and_update_(self._request_adapter)

    @property
    def authenticate_cloud_on_ramp_cred_and_add(self):
        class authenticate_cloud_on_ramp_cred_and_add_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Authenticate cloud account credentials

                :param payload: Cloud account credential
                :returns: Any
                """
                logging.warning(
                    "Operation: %s is deprecated", "authenticateCloudOnRampCredAndAdd"
                )
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cor/cloud/authenticate",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return authenticate_cloud_on_ramp_cred_and_add_(self._request_adapter)
