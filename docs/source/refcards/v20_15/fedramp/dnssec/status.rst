=====================
fedramp.dnssec.status
=====================


Operation: GET /dataservice/fedramp/dnssec/status
-------------------------------------------------


Get DNS-Sec status

.. code:: python

    def get() -> Any: ...


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
        client.fedramp.dnssec.status.get()


