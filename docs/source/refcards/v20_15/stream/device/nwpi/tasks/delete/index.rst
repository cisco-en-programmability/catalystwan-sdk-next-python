===============================
stream.device.nwpi.tasks.delete
===============================


Operation: DELETE /dataservice/stream/device/nwpi/tasks/delete/{taskId}
-----------------------------------------------------------------------


Delete Auto On Task

.. code:: python

    def delete(task_id: str) -> TasksDeleteResponsePayload: ...


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
        client.stream.device.nwpi.tasks.delete.delete()


.. toctree::
    :maxdepth: 1

    models

