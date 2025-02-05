=====================
device.dre.dre_status
=====================


Operation: GET /dataservice/device/dre/dre-status
-------------------------------------------------


Get DRE status

.. code:: python

    def get_dre_status(device_id: str) -> Any: ...


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
        client.device.dre.dre_status.get_dre_status()


