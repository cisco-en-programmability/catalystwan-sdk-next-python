================================
stream.device.nwpi.monitor.start
================================


Operation: POST /dataservice/stream/device/nwpi/monitor/start
-------------------------------------------------------------


Deprecated!!!

CXP Monitor Action - Start

.. code:: python

    def post(
        payload: NwpiMonitorReqPayload,
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
        client.stream.device.nwpi.monitor.start.post()


.. toctree::
    :maxdepth: 1

    models

