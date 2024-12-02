# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class PrefixmappingBuilder:
    """
    Builds and executes requests for operations under /partner/aci/policy/prefixmapping
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_data_prefix_mappings(self, partner_id: str, **kw) -> Any:
        """
        Get prefix mapping

        :param partner_id: Partner Id
        :returns: Any
        """
        params = {
            "partnerId": partner_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/aci/policy/prefixmapping/{partnerId}",
            params=params,
            **kw,
        )

    @property
    def set_data_prefix_mappings(self):
        class set_data_prefix_mappings_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, partner_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Create data prefix mapping

                :param partner_id: Partner Id
                :param payload: Prefix definition
                :returns: Any
                """
                params = {
                    "partnerId": partner_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/partner/aci/policy/prefixmapping/{partnerId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return set_data_prefix_mappings_(self._request_adapter)
