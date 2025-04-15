==============================
stream.device.nwpi.flow_metric
==============================


Operation: GET /dataservice/stream/device/nwpi/flowMetric
---------------------------------------------------------


Deprecated!!!

flowMetric for NWPI.

.. code:: python

    def get(
        trace_id: int,
        timestamp: int,
        flow_id: int,
        first_timestamp: int,
        last_timestamp: int,
    ) -> List[NwpiflowMetricRespPayloadInner]: ...


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
        client.stream.device.nwpi.flow_metric.get()


.. toctree::
    :maxdepth: 1

    models

