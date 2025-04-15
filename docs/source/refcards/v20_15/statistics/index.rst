==========
statistics
==========


Operation: GET /dataservice/statistics
--------------------------------------


Get statistics types

.. code:: python

    def get() -> List[Any]: ...


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
        client.statistics.get()


Operation: POST /dataservice/statistics
---------------------------------------


Get stats raw data

.. code:: python

    def post(
        payload: Any,
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
        client.statistics.post()


.. toctree::
    :maxdepth: 1

    aggregation
    app_agg/index
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
    process/index
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

