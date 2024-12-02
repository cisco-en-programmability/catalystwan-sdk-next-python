=======================
device.action.status.mw
=======================


Operation: GET /dataservice/device/action/status/mw
---------------------------------------------------


Get status of maintenance window for vManage upgrade flag

.. code:: python

    def get_maintenance_window_flag() -> Any: ...


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
        client.device.action.status.mw.get_maintenance_window_flag()


Operation: POST /dataservice/device/action/status/mw
----------------------------------------------------


Update maintenance window flag

.. code:: python

    def update_maintenance_window_flag(
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
        client.device.action.status.mw.update_maintenance_window_flag()


