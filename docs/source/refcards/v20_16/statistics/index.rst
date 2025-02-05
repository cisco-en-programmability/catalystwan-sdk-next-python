==========
statistics
==========


Operation: GET /dataservice/statistics
--------------------------------------


Get statistics types

.. code:: python

    def get_statistic_type() -> List[Any]: ...


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
        client.statistics.get_statistic_type()


Operation: POST /dataservice/statistics
---------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data_13(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> Any: ...


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
        client.statistics.get_stats_raw_data_13()


.. toctree::
    :maxdepth: 1

    aggregation
    apphosting/index
    apphostinginterface/index
    approute/index
    art/index
    bfd/index
    bridgeinterface/index
    bridgemac/index
    cflowd/index
    cloudx/index
    collect/index
    collection/index
    cryptovpn/index
    csv
    demomode
    device/index
    devicehealth/index
    doccount
    download/index
    dpi/index
    eiolte/index
    endpoint_tracker/index
    fields
    flowlog/index
    fwall/index
    interface/index
    ipsalert/index
    nwa/index
    on_demand/index
    page
    perfmon/index
    powerconsumption/index
    process/index
    qfp/index
    qos/index
    query/index
    sdra/index
    settings/index
    sitehealth/index
    speedtest/index
    sul/index
    system/index
    tunnelhealth/index
    umbrella/index
    urlf/index
    vnfstatistics/index
    wlanclientinfo/index

