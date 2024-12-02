=========================================
stream.device.nwpi.concurrent_domain_data
=========================================


Operation: GET /dataservice/stream/device/nwpi/concurrentDomainData
-------------------------------------------------------------------


Deprecated!!!

Get concurrent domain data for NWPI.

.. code:: python

    def get_concurrent_domain_data(
        trace_id: int, timestamp: int, query: Optional[str] = None
    ) -> List[ConcurrentDomainDataResponsePayloadInner]: ...


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
        client.stream.device.nwpi.concurrent_domain_data.get_concurrent_domain_data()


.. toctree::
    :maxdepth: 1

    models

