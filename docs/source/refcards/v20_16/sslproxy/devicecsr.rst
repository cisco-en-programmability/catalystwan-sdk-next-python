==================
sslproxy.devicecsr
==================


Operation: POST /dataservice/sslproxy/devicecsr
-----------------------------------------------


Get CSR for all cEdges

.. code:: python

    def get_all_device_csr(payload: Optional[Any] = None) -> Any: ...


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
        client.sslproxy.devicecsr.get_all_device_csr()


