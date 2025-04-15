================================================
device.voicet1e1controllerinfo.current15minstats
================================================


Operation: GET /dataservice/device/voicet1e1controllerinfo/current15minstats
----------------------------------------------------------------------------


Retrieve T1E1 controller last 15 min stats from device (Real Time)

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
        client.device.voicet1e1controllerinfo.current15minstats.get()


