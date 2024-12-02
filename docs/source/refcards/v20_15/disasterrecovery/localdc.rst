========================
disasterrecovery.localdc
========================


Operation: GET /dataservice/disasterrecovery/localdc
----------------------------------------------------


Get local data center details

.. code:: python

    def get_local_data_center_state() -> List[Any]: ...


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
        client.disasterrecovery.localdc.get_local_data_center_state()


