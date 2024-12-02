==================
device.featurelist
==================


Operation: GET /dataservice/device/featurelist
----------------------------------------------


Get feature lists from device (Real Time)

.. code:: python

    def get_feature_list(device_id: str) -> Any: ...


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
        client.device.featurelist.get_feature_list()


.. toctree::
    :maxdepth: 1

    synced

