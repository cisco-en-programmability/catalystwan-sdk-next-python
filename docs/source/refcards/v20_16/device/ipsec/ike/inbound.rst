========================
device.ipsec.ike.inbound
========================


Operation: GET /dataservice/device/ipsec/ike/inbound
----------------------------------------------------


Get IPsec IKE inbound connection list from device

.. code:: python

    def create_ike_inbound_list(device_id: str) -> List[Any]: ...


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
        client.device.ipsec.ike.inbound.create_ike_inbound_list()


