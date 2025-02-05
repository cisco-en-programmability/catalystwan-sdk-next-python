=========================
device.action.ztp.upgrade
=========================


Operation: GET /dataservice/device/action/ztp/upgrade
-----------------------------------------------------


Get ZTP upgrade configuration

.. code:: python

    def get_ztp_upgrade_config() -> Any: ...


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
        client.device.action.ztp.upgrade.get_ztp_upgrade_config()


Operation: POST /dataservice/device/action/ztp/upgrade
------------------------------------------------------


Process ZTP upgrade configuration setting

.. code:: python

    def postprocess_ztp_upgrade_config_setting(
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
        client.device.action.ztp.upgrade.postprocess_ztp_upgrade_config_setting()


.. toctree::
    :maxdepth: 1

    setting

