=========================================
stream.device.nwpi.tasks.event_stats_data
=========================================


Operation: GET /dataservice/stream/device/nwpi/tasks/eventStatsData
-------------------------------------------------------------------


Deprecated!!!

Get auto on stats data in one task

.. code:: python

    def get(
        task_id: int, state: str, task_end_time: int, duration: int
    ) -> EventStatsDataResponsePayload: ...


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
        client.stream.device.nwpi.tasks.event_stats_data.get()


.. toctree::
    :maxdepth: 1

    models

