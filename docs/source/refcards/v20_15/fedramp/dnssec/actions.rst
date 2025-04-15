======================
fedramp.dnssec.actions
======================


Operation: GET /dataservice/fedramp/dnssec/actions
--------------------------------------------------


Request DNS-Sec actions

.. code:: python

    def get(action: str) -> Any: ...


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
        client.fedramp.dnssec.actions.get()


