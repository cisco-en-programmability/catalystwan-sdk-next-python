===============================
device.action.firmware.activate
===============================


Operation: POST /dataservice/device/action/firmware/activate
------------------------------------------------------------


Deprecated!!!

Activate firmware on device

.. code:: python

    def post(payload: str) -> None: ...


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
        client.device.action.firmware.activate.post()


