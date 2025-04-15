============================
system.device.migrate_device
============================


Operation: PUT /dataservice/system/device/migrateDevice/{uuid}
--------------------------------------------------------------


Migrate device software to vedge/cedge

.. code:: python

    def put(uuid: str) -> Any: ...


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
        client.system.device.migrate_device.put()


