=================================
disasterrecovery.unpause_local_dc
=================================


Operation: POST /dataservice/disasterrecovery/unpauseLocalDC
------------------------------------------------------------


Unpause DR for Local datacenter

.. code:: python

    def unpause_local_dc_for_dr() -> Any: ...


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
        client.disasterrecovery.unpause_local_dc.unpause_local_dc_for_dr()


