=====================
alarms.purgefrequency
=====================


Operation: GET /dataservice/alarms/purgefrequency
-------------------------------------------------


Set alarm purge timer

.. code:: python

    def get(
        interval: Optional[str] = None, active_time: Optional[str] = None
    ) -> PurgeFrequency: ...


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
        client.alarms.purgefrequency.get()


.. toctree::
    :maxdepth: 1

    models

