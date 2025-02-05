==========================
device.action.status.tasks
==========================


Operation: GET /dataservice/device/action/status/tasks
------------------------------------------------------


Find running tasks

.. code:: python

    def find_running_tasks() -> InlineResponse200: ...


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
        client.device.action.status.tasks.find_running_tasks()


.. toctree::
    :maxdepth: 1

    active_count/index
    clean/index
    models

