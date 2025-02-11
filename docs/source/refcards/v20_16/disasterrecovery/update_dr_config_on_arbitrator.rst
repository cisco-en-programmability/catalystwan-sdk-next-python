===============================================
disasterrecovery.update_dr_config_on_arbitrator
===============================================


Operation: POST /dataservice/disasterrecovery/updateDRConfigOnArbitrator
------------------------------------------------------------------------


Update arbitrator with primary and secondary states cluster

.. code:: python

    def update_dr_state() -> Any: ...


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
        client.disasterrecovery.update_dr_config_on_arbitrator.update_dr_state()


