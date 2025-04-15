=====================================
stream.device.nwpi.tasks.task_history
=====================================


Operation: GET /dataservice/stream/device/nwpi/tasks/taskHistory
----------------------------------------------------------------


Get all the auto on tasks

.. code:: python

    def get() -> TaskHistoryResponsePayload: ...


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
        client.stream.device.nwpi.tasks.task_history.get()


.. toctree::
    :maxdepth: 1

    models

