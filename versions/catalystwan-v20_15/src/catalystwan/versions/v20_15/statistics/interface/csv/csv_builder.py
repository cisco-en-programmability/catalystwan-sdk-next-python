# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class CsvBuilder:
    """
    Builds and executes requests for operations under /statistics/interface/csv
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_data_raw_data_as_csv_11(self, query: str, **kw) -> str:
        """
        Get raw data with optional query as CSV

        :param query: Query
        :returns: str
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/interface/csv", return_type=str, params=params, **kw
        )
