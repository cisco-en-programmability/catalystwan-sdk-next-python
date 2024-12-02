====================================
stream.device.nwpi.get_monitor_state
====================================


Operation: GET /dataservice/stream/device/nwpi/getMonitorState
--------------------------------------------------------------


Deprecated!!!

getMonitorState

.. code:: python

    def get_monitor_state(
        trace_id: int, state: str
    ) -> NwpiDomainMonitorStateRespPayload: ...


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
        client.stream.device.nwpi.get_monitor_state.get_monitor_state()


.. toctree::
    :maxdepth: 1

    models

