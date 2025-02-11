====================
device.reboothistory
====================


Operation: GET /dataservice/device/reboothistory
------------------------------------------------


Get device reboot history

.. code:: python

    def create_reboot_history_list(device_id: str) -> Any: ...


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
        client.device.reboothistory.create_reboot_history_list()


.. toctree::
    :maxdepth: 1

    details
    synced

