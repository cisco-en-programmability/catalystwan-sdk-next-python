=========================================
certificate.revoke.enterprise.certificate
=========================================


Operation: POST /dataservice/certificate/revoke/enterprise/certificate
----------------------------------------------------------------------


Revoking enterprise CSR for hardware vEdge

.. code:: python

    def decommission_enterprise_csr_for_vedge(
        payload: Optional[str] = None,
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
        client.certificate.revoke.enterprise.certificate.decommission_enterprise_csr_for_vedge()


