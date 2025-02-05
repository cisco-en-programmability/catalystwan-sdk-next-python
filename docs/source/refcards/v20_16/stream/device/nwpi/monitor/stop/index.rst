===============================
stream.device.nwpi.monitor.stop
===============================


Operation: POST /dataservice/stream/device/nwpi/monitor/stop
------------------------------------------------------------


Deprecated!!!

CXP Monitor Action - Stop

.. code:: python

    def monitor_stop(
        payload: Optional[NwpiMonitorReqPayload] = None,
    ) -> NwpiMonitorRespPayload: ...


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
        client.stream.device.nwpi.monitor.stop.monitor_stop()


.. toctree::
    :maxdepth: 1

    models

