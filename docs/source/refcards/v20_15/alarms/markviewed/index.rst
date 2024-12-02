=================
alarms.markviewed
=================


Operation: POST /dataservice/alarms/markviewed
----------------------------------------------


Mark alarms as acknowledged based on list of UUIDs.

.. code:: python

    def mark_alarms_as_viewed(
        payload: Optional[Any] = None,
    ) -> List[AlarmCount]: ...


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
        client.alarms.markviewed.mark_alarms_as_viewed()


.. toctree::
    :maxdepth: 1

    models

