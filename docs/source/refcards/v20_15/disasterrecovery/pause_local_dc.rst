===============================
disasterrecovery.pause_local_dc
===============================


Operation: POST /dataservice/disasterrecovery/pauseLocalDC
----------------------------------------------------------


Pause DR for Local datacenter

.. code:: python

    def pause_local_dc_for_dr() -> Any: ...


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
        client.disasterrecovery.pause_local_dc.pause_local_dc_for_dr()


