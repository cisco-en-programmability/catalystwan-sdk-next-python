=======================
certificate.device.list
=======================


Operation: GET /dataservice/certificate/device/list
---------------------------------------------------


get device list

.. code:: python

    def get_devices_list() -> str: ...


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
        client.certificate.device.list.get_devices_list()


