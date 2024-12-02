=====================================
device.control.synced.localproperties
=====================================


Operation: GET /dataservice/device/control/synced/localproperties
-----------------------------------------------------------------


Get local properties list

.. code:: python

    def create_local_properties_synced_list(
        device_id: str,
    ) -> List[Any]: ...


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
        client.device.control.synced.localproperties.create_local_properties_synced_list()


