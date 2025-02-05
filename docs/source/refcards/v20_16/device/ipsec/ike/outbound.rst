=========================
device.ipsec.ike.outbound
=========================


Operation: GET /dataservice/device/ipsec/ike/outbound
-----------------------------------------------------


Get IPsec IKE outbound connection list from device

.. code:: python

    def create_ike_outbound_list(device_id: str) -> List[Any]: ...


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
        client.device.ipsec.ike.outbound.create_ike_outbound_list()


