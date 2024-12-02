=======================================
device.action.status.tasks.active_count
=======================================


Operation: GET /dataservice/device/action/status/tasks/activeCount
------------------------------------------------------------------


Get active task count

.. code:: python

    def get_active_task_count() -> DeviceTaskStatus: ...


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
        client.device.action.status.tasks.active_count.get_active_task_count()


.. toctree::
    :maxdepth: 1

    models

