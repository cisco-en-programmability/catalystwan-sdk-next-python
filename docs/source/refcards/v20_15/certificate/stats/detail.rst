========================
certificate.stats.detail
========================


Operation: GET /dataservice/certificate/stats/detail
----------------------------------------------------


Get certificate details

.. code:: python

    def get_certificate_detail(
        status: Optional[str] = None,
    ) -> List[str]: ...


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
        client.certificate.stats.detail.get_certificate_detail()


