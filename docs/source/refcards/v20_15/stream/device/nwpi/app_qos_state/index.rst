================================
stream.device.nwpi.app_qos_state
================================


Operation: GET /dataservice/stream/device/nwpi/appQosState
----------------------------------------------------------


Deprecated!!!

Get QoS Application state to received timestamp mapping for NWPI.

.. code:: python

    def get_app_qos_state(
        trace_id: int, timestamp: int, trace_state: str
    ) -> List[AppQosStateResponsePayloadInner]: ...


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
        client.stream.device.nwpi.app_qos_state.get_app_qos_state()


.. toctree::
    :maxdepth: 1

    models

