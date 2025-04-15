===========================
template.cloudx.sig_tunnels
===========================


Operation: GET /dataservice/template/cloudx/sig_tunnels
-------------------------------------------------------


Get Secure Internet Gateway Tunnel List

.. code:: python

    def get(device_id: str) -> None: ...


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
        client.template.cloudx.sig_tunnels.get()


