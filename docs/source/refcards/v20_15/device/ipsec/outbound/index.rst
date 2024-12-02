=====================
device.ipsec.outbound
=====================


Operation: GET /dataservice/device/ipsec/outbound
-------------------------------------------------


Get IPsec outbound connection list from device (Real Time)

.. code:: python

    def create_out_bound_list(
        device_id: str,
        remote_tloc_address: Optional[str] = None,
        remote_tloc_color: Optional[RemoteTlocColorParam] = None,
    ) -> List[Any]: ...


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
        client.device.ipsec.outbound.create_out_bound_list()


.. toctree::
    :maxdepth: 1

    models

