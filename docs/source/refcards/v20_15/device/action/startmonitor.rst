==========================
device.action.startmonitor
==========================


Operation: GET /dataservice/device/action/startmonitor
------------------------------------------------------


Triggers global monitoring thread

.. code:: python

    def trigger_pending_tasks_monitoring() -> None: ...


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
        client.device.action.startmonitor.trigger_pending_tasks_monitoring()


