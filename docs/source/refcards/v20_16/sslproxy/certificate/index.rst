====================
sslproxy.certificate
====================


Operation: GET /dataservice/sslproxy/certificate
------------------------------------------------


Get edge proxy certificate

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.sslproxy.certificate.get()


Operation: PUT /dataservice/sslproxy/certificate
------------------------------------------------


Upload device certificate

.. code:: python

    def put(payload: Any) -> Any: ...


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
        client.sslproxy.certificate.put()


.. toctree::
    :maxdepth: 1

    wanedge

