=======================
device.tools.traceroute
=======================


Operation: POST /dataservice/device/tools/traceroute/{deviceIP}
---------------------------------------------------------------


Traceroute

.. code:: python

    def post(
        device_ip: str, payload: TracerouteRequest
    ) -> TracerouteResponse: ...


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
        client.device.tools.traceroute.post()


.. toctree::
    :maxdepth: 1

    models

