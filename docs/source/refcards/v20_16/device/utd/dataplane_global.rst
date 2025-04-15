===========================
device.utd.dataplane_global
===========================


Operation: GET /dataservice/device/utd/dataplane-global
-------------------------------------------------------


Get data plane global from Device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.utd.dataplane_global.get()


