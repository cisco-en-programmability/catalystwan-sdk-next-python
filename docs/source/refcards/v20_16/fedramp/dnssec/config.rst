=====================
fedramp.dnssec.config
=====================


Operation: POST /dataservice/fedramp/dnssec/config
--------------------------------------------------


Configure DNS-Sec

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.fedramp.dnssec.config.post()


