=========================================
disasterrecovery.delete_local_data_center
=========================================


Operation: POST /dataservice/disasterrecovery/deleteLocalDataCenter
-------------------------------------------------------------------


Delete local data center

.. code:: python

    def post() -> Any: ...


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
        client.disasterrecovery.delete_local_data_center.post()


