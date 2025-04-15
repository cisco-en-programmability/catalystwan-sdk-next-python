==============================
device.action.firmware.install
==============================


Operation: POST /dataservice/device/action/firmware/install
-----------------------------------------------------------


Deprecated!!!

Install firmware on device

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
        client.device.action.firmware.install.post()


