==========================
network.issues.rebootcount
==========================


Operation: GET /dataservice/network/issues/rebootcount
------------------------------------------------------


Retrieve reboot count

.. code:: python

    def get(is_cached: bool) -> Any: ...


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
        client.network.issues.rebootcount.get()


