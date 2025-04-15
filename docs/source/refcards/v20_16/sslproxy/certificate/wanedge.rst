============================
sslproxy.certificate.wanedge
============================


Operation: POST /dataservice/sslproxy/certificate/wanedge/{deviceId}
--------------------------------------------------------------------


Add SSL proxy wan edge

.. code:: python

    def post(device_id: str, payload: Any) -> None: ...


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
        client.sslproxy.certificate.wanedge.post()


