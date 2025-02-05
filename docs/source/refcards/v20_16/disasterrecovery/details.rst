========================
disasterrecovery.details
========================


Operation: GET /dataservice/disasterrecovery/details
----------------------------------------------------


Get disaster recovery details

.. code:: python

    def get_details() -> Any: ...


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
        client.disasterrecovery.details.get_details()


