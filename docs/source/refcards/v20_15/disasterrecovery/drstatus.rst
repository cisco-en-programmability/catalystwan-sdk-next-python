=========================
disasterrecovery.drstatus
=========================


Operation: GET /dataservice/disasterrecovery/drstatus
-----------------------------------------------------


Disaster recovery status

.. code:: python

    def get_disaster_recovery_status() -> List[Any]: ...


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
        client.disasterrecovery.drstatus.get_disaster_recovery_status()


