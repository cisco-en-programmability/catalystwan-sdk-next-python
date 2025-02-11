====================================
cluster_management.connected_devices
====================================


Operation: GET /dataservice/clusterManagement/connectedDevices/{vmanageIP}
--------------------------------------------------------------------------


Get connected device for vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_connected_devices(vmanage_ip: str) -> List[Any]: ...


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
        client.cluster_management.connected_devices.get_connected_devices()


Operation: GET /dataservice/clusterManagement/{tenantId}/connectedDevices/{vmanageIP}
-------------------------------------------------------------------------------------


Get connected device for vManage for a tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_connected_devices_per_tenant(
        tenant_id: str, vmanage_ip: str
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
        client.cluster_management.connected_devices.get_connected_devices_per_tenant()


