=============
alarms.master
=============


Operation: GET /dataservice/alarms/master
-----------------------------------------


Get topic details.

.. code:: python

    def get_master_manager_state() -> str: ...


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
        client.alarms.master.get_master_manager_state()


