=============================
device.vedgeinventory.summary
=============================


Operation: GET /dataservice/device/vedgeinventory/summary
---------------------------------------------------------


Get vEdge inventory

.. code:: python

    def get_vedge_inventory_summary() -> Any: ...


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
        client.device.vedgeinventory.summary.get_vedge_inventory_summary()


