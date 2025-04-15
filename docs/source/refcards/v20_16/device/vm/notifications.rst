=======================
device.vm.notifications
=======================


Operation: GET /dataservice/device/vm/notifications
---------------------------------------------------


Get CloudDock vm lifecycle state

.. code:: python

    def get(user_group: str) -> Any: ...


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
        client.device.vm.notifications.get()


