===========
device.vrrp
===========


Operation: GET /dataservice/device/vrrp
---------------------------------------


Get VRRP interface list from device

.. code:: python

    def get_vrrp_interface(device_id: str) -> List[Any]: ...


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
        client.device.vrrp.get_vrrp_interface()


