========================
device.tools.servicepath
========================


Operation: POST /dataservice/device/tools/servicepath/{deviceIP}
----------------------------------------------------------------


Service path

.. code:: python

    def post(device_ip: str, payload: Any) -> None: ...


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
        client.device.tools.servicepath.post()


