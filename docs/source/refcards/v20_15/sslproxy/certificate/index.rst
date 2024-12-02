====================
sslproxy.certificate
====================


Operation: GET /dataservice/sslproxy/certificate
------------------------------------------------


Get edge proxy certificate

.. code:: python

    def get_proxy_cert_of_edge(device_id: str) -> Any: ...


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
        client.sslproxy.certificate.get_proxy_cert_of_edge()


Operation: PUT /dataservice/sslproxy/certificate
------------------------------------------------


Upload device certificate

.. code:: python

    def update_certificate(payload: Optional[Any] = None) -> Any: ...


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
        client.sslproxy.certificate.update_certificate()


.. toctree::
    :maxdepth: 1

    wanedge

