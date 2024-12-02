================================
certificate.generate.wanedge.csr
================================


Operation: POST /dataservice/certificate/generate/wanedge/csr
-------------------------------------------------------------


generate CSR on WAN edge device

.. code:: python

    def generate_edge_device_csr(
        payload: Optional[Any] = None,
    ) -> str: ...


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
        client.certificate.generate.wanedge.csr.generate_edge_device_csr()


