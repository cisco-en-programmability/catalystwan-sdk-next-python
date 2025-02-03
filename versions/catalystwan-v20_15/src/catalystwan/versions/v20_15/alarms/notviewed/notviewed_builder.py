# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import Alarm


class NotviewedBuilder:
    """
    Builds and executes requests for operations under /alarms/notviewed
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_non_viewed_alarms(self, state: Optional[str] = None, **kw) -> List[Alarm]:
        """
        Get alarms which are not acknowledged by the user.

        :param state: Specify the not viewed alarm state to be fetched. Allowed values : ["active", "cleared"]
        :returns: List[Alarm]
        """
        params = {
            "state": state,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/alarms/notviewed", return_type=List[Alarm], params=params, **kw
        )
