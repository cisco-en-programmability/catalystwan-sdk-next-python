=============================
stream.device.nwpi.tasks.stop
=============================


Operation: POST /dataservice/stream/device/nwpi/tasks/stop/{taskId}
-------------------------------------------------------------------


Task Action - Stop

.. code:: python

    def task_stop(task_id: str) -> TasksStopResponsePayload: ...


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
        client.stream.device.nwpi.tasks.stop.task_stop()


.. toctree::
    :maxdepth: 1

    models

