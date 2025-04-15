===================================
disasterrecovery.remotedc.swversion
===================================


Operation: GET /dataservice/disasterrecovery/remotedc/swversion
---------------------------------------------------------------


Get remote data center vManage version

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
        client.disasterrecovery.remotedc.swversion.get()


