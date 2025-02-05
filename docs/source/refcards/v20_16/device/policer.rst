==============
device.policer
==============


Operation: GET /dataservice/device/policer
------------------------------------------


Get policed interface list from device

.. code:: python

    def get_policed_interface(device_id: str) -> Any: ...


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
        client.device.policer.get_policed_interface()


