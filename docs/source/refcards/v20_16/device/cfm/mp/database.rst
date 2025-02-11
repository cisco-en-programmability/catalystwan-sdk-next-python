======================
device.cfm.mp.database
======================


Operation: GET /dataservice/device/cfm/mp/database
--------------------------------------------------


Get mp database from device

.. code:: python

    def get_mp_database(device_id: str) -> Any: ...


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
        client.device.cfm.mp.database.get_mp_database()


