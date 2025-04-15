============================
device.vedgeinventory.detail
============================


Operation: GET /dataservice/device/vedgeinventory/detail
--------------------------------------------------------


Get detailed vEdge inventory

.. code:: python

    def get(status: Optional[str] = None) -> VedgeInventoryData: ...


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
        client.device.vedgeinventory.detail.get()


.. toctree::
    :maxdepth: 1

    models

