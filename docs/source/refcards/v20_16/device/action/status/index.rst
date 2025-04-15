====================
device.action.status
====================


Operation: GET /dataservice/device/action/status/{processId}
------------------------------------------------------------


Find status of action

.. code:: python

    def get(process_id: str) -> Any: ...


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
        client.device.action.status.get()


.. toctree::
    :maxdepth: 1

    cancel
    clean
    clear
    mw
    tasks/index

