=================================
v1.cloudonramp.saas.cloud_tunnels
=================================


Operation: GET /dataservice/v1/cloudonramp/saas/cloud_tunnels
-------------------------------------------------------------


Get Secure Internet Gateway Tunnel List

.. code:: python

    def get(device_ip: str) -> None: ...


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
        client.v1.cloudonramp.saas.cloud_tunnels.get()


