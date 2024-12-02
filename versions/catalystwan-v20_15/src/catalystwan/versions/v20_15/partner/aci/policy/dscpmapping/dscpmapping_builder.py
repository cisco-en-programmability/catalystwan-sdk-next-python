# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class DscpmappingBuilder:
    """
    Builds and executes requests for operations under /partner/aci/policy/dscpmapping
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dscp_mappings(self, partner_id: str, **kw) -> Any:
        """
        Get DSCP policy

        :param partner_id: Partner Id
        :returns: Any
        """
        params = {
            "partnerId": partner_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/aci/policy/dscpmapping/{partnerId}",
            params=params,
            **kw,
        )

    @property
    def create_dscp_mappings(self):
        class create_dscp_mappings_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, partner_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Create an ACI definition entry

                :param partner_id: Partner Id
                :param payload: ACI definition
                :returns: Any
                """
                params = {
                    "partnerId": partner_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/partner/aci/policy/dscpmapping/{partnerId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_dscp_mappings_(self._request_adapter)

    def delete_dscp_mappings(self, partner_id: str, **kw) -> Any:
        """
        Delete DSCP mapping

        :param partner_id: Partner Id
        :returns: Any
        """
        params = {
            "partnerId": partner_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/partner/aci/policy/dscpmapping/{partnerId}",
            params=params,
            **kw,
        )
