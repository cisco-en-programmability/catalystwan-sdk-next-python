================================
device.action.status.tasks.clean
================================


Operation: GET /dataservice/device/action/status/tasks/clean
------------------------------------------------------------


Delete task and status vertex

.. code:: python

    def get(process_id: str) -> DeviceTaskStatus: ...


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
        client.device.action.status.tasks.clean.get()


.. toctree::
    :maxdepth: 1

    models

