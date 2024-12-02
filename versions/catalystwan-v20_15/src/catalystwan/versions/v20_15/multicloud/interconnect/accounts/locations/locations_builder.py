# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import InterconnectLocations


class LocationsBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/locations
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_location_info(
        self,
        interconnect_type: str,
        interconnect_account_id: str,
        region: Optional[str] = None,
        **kw,
    ) -> InterconnectLocations:
        """
        API to retrieve list of available regions for an Interconnect provider and account.

        :param interconnect_type: Interconnect provider type
        :param interconnect_account_id: Interconnect account id
        :param region: Interconnect provider location
        :returns: InterconnectLocations
        """
        params = {
            "interconnect-type": interconnect_type,
            "interconnect-account-id": interconnect_account_id,
            "region": region,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/locations",
            return_type=InterconnectLocations,
            params=params,
            **kw,
        )

    def update_interconnect_location_info(
        self, interconnect_type: str, interconnect_account_id: str, **kw
    ) -> InterconnectLocations:
        """
        API to retrieve and update the available regions for an Interconnect provider and account.

        :param interconnect_type: Interconnect provider type
        :param interconnect_account_id: Interconnect account id
        :returns: InterconnectLocations
        """
        params = {
            "interconnect-type": interconnect_type,
            "interconnect-account-id": interconnect_account_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/locations",
            return_type=InterconnectLocations,
            params=params,
            **kw,
        )

    def delete_interconnect_location_info(
        self, interconnect_type: str, interconnect_account_id: str, **kw
    ):
        """
        API to delete the stored regions for an Interconnect provider and account from vManage.

        :param interconnect_type: Interconnect provider type
        :param interconnect_account_id: Interconnect account id
        :returns: None
        """
        params = {
            "interconnect-type": interconnect_type,
            "interconnect-account-id": interconnect_account_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/locations",
            params=params,
            **kw,
        )
