===============================
stream.device.nwpi.tasks.traces
===============================


Operation: GET /dataservice/stream/device/nwpi/tasks/{taskId}/traces
--------------------------------------------------------------------


Get all traces in one task

.. code:: python

    def get_task_trace(task_id: str) -> TaskTracesResponsePayload: ...


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
        client.stream.device.nwpi.tasks.traces.get_task_trace()


.. toctree::
    :maxdepth: 1

    models

