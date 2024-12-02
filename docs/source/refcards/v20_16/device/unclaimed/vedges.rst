=======================
device.unclaimed.vedges
=======================


Operation: GET /dataservice/device/unclaimed/vedges
---------------------------------------------------


Get unclaimed vEdges from vbond

.. code:: python

    def get_unclaimed_vedges(device_id: str) -> Any: ...


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
        client.device.unclaimed.vedges.get_unclaimed_vedges()


