============================
device.reboothistory.details
============================


Operation: GET /dataservice/device/reboothistory/details
--------------------------------------------------------


Get detailed reboot history list

.. code:: python

    def get() -> Any: ...


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
        client.device.reboothistory.details.get()


