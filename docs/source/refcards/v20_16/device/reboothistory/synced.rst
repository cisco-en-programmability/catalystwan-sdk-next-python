===========================
device.reboothistory.synced
===========================


Operation: GET /dataservice/device/reboothistory/synced
-------------------------------------------------------


Get device reboot history synchronously

.. code:: python

    def create_synced_reboot_history_list(device_id: str) -> Any: ...


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
        client.device.reboothistory.synced.create_synced_reboot_history_list()


