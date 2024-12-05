# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Type

from catalystwan.abc import RequestAdapterInterface

from .models import WcmNetconfConfigRequest, WcmNetconfConfigRes


class NetconfBuilder:
    """
    Builds and executes requests for operations under /partner/wcm/netconf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def push_netconf_configs(self):
        class push_netconf_configs_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, nms_id: str, payload: WcmNetconfConfigRequest, **kw) -> WcmNetconfConfigRes:
                """
                Push device configs

                :param nms_id: Nms id
                :param payload: Netconf configuration
                :returns: WcmNetconfConfigRes
                """
                params = {
                    "nmsId": nms_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/partner/wcm/netconf/{nmsId}",
                    return_type=WcmNetconfConfigRes,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> WcmNetconfConfigRequest:
                return WcmNetconfConfigRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[WcmNetconfConfigRequest]:
                return WcmNetconfConfigRequest

        return push_netconf_configs_(self._request_adapter)
