=====================================
device.action.status.preupgrade.check
=====================================


Operation: PUT /dataservice/device/action/status/preupgrade/check
-----------------------------------------------------------------


Update pre upgrade check status

.. code:: python

    def update_pre_upgrade_check_status(
        payload: Optional[UpdatePreUpgradeCheckStatusPutRequest] = None,
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
        client.device.action.status.preupgrade.check.update_pre_upgrade_check_status()


.. toctree::
    :maxdepth: 1

    models

