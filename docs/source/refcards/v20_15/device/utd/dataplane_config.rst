===========================
device.utd.dataplane_config
===========================


Operation: GET /dataservice/device/utd/dataplane-config
-------------------------------------------------------


Get data plane config from Device

.. code:: python

    def get_utd_dataplane_config(device_id: str) -> Any: ...


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
        client.device.utd.dataplane_config.get_utd_dataplane_config()


