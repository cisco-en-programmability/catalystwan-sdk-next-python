=================
multicloud.device
=================


Operation: GET /dataservice/multicloud/device
---------------------------------------------


Get available WAN edge devices

.. code:: python

    def get_wan_devices() -> WanEdgeDevicesResponse: ...


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
        client.multicloud.device.get_wan_devices()


.. toctree::
    :maxdepth: 1

    models

