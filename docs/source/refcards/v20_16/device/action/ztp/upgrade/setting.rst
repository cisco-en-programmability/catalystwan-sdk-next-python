=================================
device.action.ztp.upgrade.setting
=================================


Operation: GET /dataservice/device/action/ztp/upgrade/setting
-------------------------------------------------------------


Get ZTP upgrade configuration setting

.. code:: python

    def get() -> Any: ...


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
        client.device.action.ztp.upgrade.setting.get()


Operation: POST /dataservice/device/action/ztp/upgrade/setting
--------------------------------------------------------------


Process ZTP upgrade configuration setting

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.device.action.ztp.upgrade.setting.post()


