# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import AzureVirtualWan, CloudTypeParam, InlineResponse2009


class VwansBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vwans
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_az_virtual_wans(
        self,
        cloud_type: str,
        cloud_account_id: str,
        resource_group: str,
        refresh: Optional[str] = "false",
        vwan_name: Optional[str] = None,
        **kw,
    ) -> InlineResponse2009:
        """
        API to retrieve Azure Virtual Wans.

        :param cloud_type: Cloud Provider Type
        :param cloud_account_id: Cloud account id
        :param resource_group: Azure cloud resource group name
        :param refresh: Refresh
        :param vwan_name: Vwan Name
        :returns: InlineResponse2009
        """
        params = {
            "cloud-type": cloud_type,
            "cloud-account-id": cloud_account_id,
            "resource-group": resource_group,
            "refresh": refresh,
            "vwan-name": vwan_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vwans",
            return_type=InlineResponse2009,
            params=params,
            **kw,
        )

    @property
    def create_az_virtual_wan(self):
        class create_az_virtual_wan_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                cloud_type: str,
                cloud_account_id: str,
                payload: Optional[AzureVirtualWan] = None,
                **kw,
            ) -> InlineResponse2009:
                """
                API to create an Azure Virtual Wan..

                :param cloud_type: Cloud Provider Type
                :param cloud_account_id: Cloud account id
                :param payload: Request Payload for Multicloud Interconnect Azure Vwan
                :returns: InlineResponse2009
                """
                params = {
                    "cloud-type": cloud_type,
                    "cloud-account-id": cloud_account_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vwans",
                    return_type=InlineResponse2009,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> AzureVirtualWan:
                return AzureVirtualWan(*args, **kwargs)

            @property
            def payload_model(self) -> Type[AzureVirtualWan]:
                return AzureVirtualWan

        return create_az_virtual_wan_(self._request_adapter)

    def delete_az_virtual_wan(
        self,
        cloud_type: CloudTypeParam,
        cloud_account_id: str,
        vwan_name: str,
        resource_group: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        API to delete an Azure Virtual Wan.

        :param cloud_type: Cloud Provider Type
        :param cloud_account_id: Cloud account id
        :param vwan_name: Vwan name
        :param resource_group: Azure cloud resource group name
        :returns: Any
        """
        params = {
            "cloud-type": cloud_type,
            "cloud-account-id": cloud_account_id,
            "vwan-name": vwan_name,
            "resource-group": resource_group,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/vwans/{vwan-name}",
            params=params,
            **kw,
        )
