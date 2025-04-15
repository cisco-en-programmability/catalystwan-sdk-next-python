====================================
cluster_management.connected_devices
====================================


Operation: GET /dataservice/clusterManagement/connectedDevices/{vmanageIP}
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(vmanage_ip: str) -> List[Any]: ...


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
        client.cluster_management.connected_devices.get()


Operation: GET /dataservice/clusterManagement/{tenantId}/connectedDevices/{vmanageIP}
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(vmanage_ip: str, tenant_id: str) -> List[Any]: ...


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
        client.cluster_management.connected_devices.get()


