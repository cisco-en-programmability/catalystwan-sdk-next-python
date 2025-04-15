==============================
stream.device.nwpi.flow_detail
==============================


Operation: GET /dataservice/stream/device/nwpi/flowDetail
---------------------------------------------------------


Deprecated!!!

flowDetail for NWPI.

.. code:: python

    def get(
        trace_id: int, timestamp: int, flow_id: int
    ) -> List[NwpiflowDetailRespPayloadInner]: ...


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
        client.stream.device.nwpi.flow_detail.get()


.. toctree::
    :maxdepth: 1

    models

