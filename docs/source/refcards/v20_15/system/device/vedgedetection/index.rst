============================
system.device.vedgedetection
============================


Operation: GET /dataservice/system/device/vedgedetection
--------------------------------------------------------


Check for Vedge Device Presence

.. code:: python

    def checkv_edge_device_presence() -> VedgeCheckResponse: ...


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
        client.system.device.vedgedetection.checkv_edge_device_presence()


.. toctree::
    :maxdepth: 1

    models

