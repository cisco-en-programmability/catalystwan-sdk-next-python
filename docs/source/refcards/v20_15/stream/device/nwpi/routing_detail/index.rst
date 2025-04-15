=================================
stream.device.nwpi.routing_detail
=================================


Operation: GET /dataservice/stream/device/nwpi/routingDetail
------------------------------------------------------------


Deprecated!!!

Get Routing Details for NWPI.

.. code:: python

    def get(
        trace_id: int,
        timestamp: int,
        trace_state: str,
        route_prefixs: str,
    ) -> List[RoutingDetailResponsePayloadInner]: ...


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
        client.stream.device.nwpi.routing_detail.get()


.. toctree::
    :maxdepth: 1

    models

