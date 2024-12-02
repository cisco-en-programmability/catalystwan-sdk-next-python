# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Type

from catalystwan.abc import RequestAdapterInterface

from .models import NvaRulesListRequest, NvaRulesResponse, Taskid


class NvaSecurityRulesBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgateway/nvaSecurityRules
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_nva_security_rules(self, cloud_gateway_name: str, **kw) -> NvaRulesResponse:
        """
        Get NVA Security Rules

        :param cloud_gateway_name: Multicloud cloud gateway name
        :returns: NvaRulesResponse
        """
        params = {
            "cloudGatewayName": cloud_gateway_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/cloudgateway/nvaSecurityRules/{cloudGatewayName}",
            return_type=NvaRulesResponse,
            params=params,
            **kw,
        )

    @property
    def update_nva_security_rules(self):
        class update_nva_security_rules_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, cloud_gateway_name: str, payload: NvaRulesListRequest, **kw
            ) -> Taskid:
                """
                Update NVA Security Rules

                :param cloud_gateway_name: Cloud gateway name
                :param payload: Update NVA security Rules
                :returns: Taskid
                """
                params = {
                    "cloudGatewayName": cloud_gateway_name,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/cloudgateway/nvaSecurityRules/{cloudGatewayName}",
                    return_type=Taskid,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> NvaRulesListRequest:
                return NvaRulesListRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[NvaRulesListRequest]:
                return NvaRulesListRequest

        return update_nva_security_rules_(self._request_adapter)
