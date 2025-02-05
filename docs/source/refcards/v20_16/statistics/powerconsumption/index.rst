===========================
statistics.powerconsumption
===========================


Operation: POST /dataservice/statistics/powerconsumption
--------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_stats_raw_data_3(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> List[PowerConsumptionResp]: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.statistics.powerconsumption.get_stats_raw_data_3()


.. toctree::
    :maxdepth: 1

    aggregation/index
    device/index
    energymix/index
    supportdevicelist/index
    total/index
    models

