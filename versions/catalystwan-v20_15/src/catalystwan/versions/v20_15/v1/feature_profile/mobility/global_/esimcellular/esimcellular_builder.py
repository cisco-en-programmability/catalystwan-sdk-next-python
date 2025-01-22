# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class EsimcellularBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/esimcellular
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_esim_cellular_profile_feature_for_mobility(self, profile_id: str, **kw) -> str:
        """
        Get EsimCellular Profile Features for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular",
            return_type=str,
            params=params,
            **kw,
        )

    def create_esim_cellular_profile_feature_for_mobility(
        self, profile_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a EsimCellular Profile Feature for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param payload: EsimCellular Profile Feature
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_esim_cellular_profile_feature_by_esim_cellular_id_for_mobility(
        self, profile_id: str, esim_cellular_id: str, **kw
    ) -> str:
        """
        Get EsimCellular Profile Feature by Feature Id for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param esim_cellular_id: Feature ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "esimCellularId": esim_cellular_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_esim_cellular_profile_feature_for_mobility(
        self, profile_id: str, esim_cellular_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a EsimCellular Profile Feature for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param esim_cellular_id: Feature ID
        :param payload: EsimCellular Profile Feature
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "esimCellularId": esim_cellular_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_esim_cellular_profile_feature_for_mobility(
        self, profile_id: str, esim_cellular_id: str, **kw
    ):
        """
        Delete a EsimCellular Profile Feature for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param esim_cellular_id: Feature ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "esimCellularId": esim_cellular_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/esimcellular/{esimCellularId}",
            params=params,
            **kw,
        )
