# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class EnrollBuilder:
    """
    Builds and executes requests for operations under /dashboard/enroll
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def enroll_cd_profiles(self, profile_id: str, **kw):
        """
        Enroll a Controller with CD profiles

        :param profile_id: CD profile Id
        :returns: None
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request("POST", "/dataservice/dashboard/enroll/{profileId}", params=params, **kw)
