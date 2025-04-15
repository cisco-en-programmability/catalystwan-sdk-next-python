=========================
certificate.stats.summary
=========================


Operation: GET /dataservice/certificate/stats/summary
-----------------------------------------------------


Get certificate expiration status

.. code:: python

    def get() -> List[str]: ...


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
        client.certificate.stats.summary.get()


