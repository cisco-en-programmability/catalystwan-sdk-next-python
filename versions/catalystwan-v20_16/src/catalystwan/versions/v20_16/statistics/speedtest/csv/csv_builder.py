# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class CsvBuilder:
    """
    Builds and executes requests for operations under /statistics/speedtest/csv
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_data_raw_data_as_csv_27(self, query: Optional[str] = None, **kw) -> str:
        """
        Get raw data with optional query as CSV

        :param query: Query string
        :returns: str
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/speedtest/csv", return_type=str, params=params, **kw
        )
