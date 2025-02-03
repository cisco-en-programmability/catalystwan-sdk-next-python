====================
device.action.status
====================


Operation: PUT /dataservice/device/action/status
------------------------------------------------


Update device action status

.. code:: python

    def update_device_action_task_status(
        payload: Optional[Any] = None,
    ) -> None: ...


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
        client.device.action.status.update_device_action_task_status()


Operation: GET /dataservice/device/action/status/{processId}
------------------------------------------------------------


Find status of action

.. code:: python

    def find_status(process_id: str) -> Any: ...


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
        client.device.action.status.find_status()


.. toctree::
    :maxdepth: 1

    cancel
    clean
    clear
    mw
    preupgrade/index
    tasks/index

