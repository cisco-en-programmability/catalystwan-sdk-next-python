=========================
disasterrecovery.remotedc
=========================


Operation: GET /dataservice/disasterrecovery/remotedc
-----------------------------------------------------


Get remote data center details

.. code:: python

    def get_remote_data_center_state() -> List[Any]: ...


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
        client.disasterrecovery.remotedc.get_remote_data_center_state()


.. toctree::
    :maxdepth: 1

    swversion

