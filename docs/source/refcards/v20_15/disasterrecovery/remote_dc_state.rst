================================
disasterrecovery.remote_dc_state
================================


Operation: GET /dataservice/disasterrecovery/remoteDcState
----------------------------------------------------------


Gets remote data center member state

.. code:: python

    def get_remote_dc_members_state() -> List[Any]: ...


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
        client.disasterrecovery.remote_dc_state.get_remote_dc_members_state()


