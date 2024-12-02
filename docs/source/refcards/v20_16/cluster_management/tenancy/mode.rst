===============================
cluster_management.tenancy.mode
===============================


Operation: GET /dataservice/clusterManagement/tenancy/mode
----------------------------------------------------------


Get vManage tenancy mode<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_tenancy_mode() -> Any: ...


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
        client.cluster_management.tenancy.mode.get_tenancy_mode()


Operation: POST /dataservice/clusterManagement/tenancy/mode
-----------------------------------------------------------


Update vManage tenancy mode

.. code:: python

    def set_tenancy_mode(payload: Optional[Any] = None) -> None: ...


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
        client.cluster_management.tenancy.mode.set_tenancy_mode()


