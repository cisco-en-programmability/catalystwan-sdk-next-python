======================================
system.device.controllers.vedge.status
======================================


Operation: GET /dataservice/system/device/controllers/vedge/status
------------------------------------------------------------------


Get controllers vEdge sync status

.. code:: python

    def get() -> List[Any]: ...


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
        client.system.device.controllers.vedge.status.get()


