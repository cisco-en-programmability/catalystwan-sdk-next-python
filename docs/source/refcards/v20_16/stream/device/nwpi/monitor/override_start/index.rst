=========================================
stream.device.nwpi.monitor.override_start
=========================================


Operation: POST /dataservice/stream/device/nwpi/monitor/overrideStart
---------------------------------------------------------------------


Deprecated!!!

CXP Monitor Action - Override Start

.. code:: python

    def monitor_override_start(
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
        client.stream.device.nwpi.monitor.override_start.monitor_override_start()


.. toctree::
    :maxdepth: 1

    models

