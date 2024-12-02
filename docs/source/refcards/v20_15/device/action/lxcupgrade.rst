========================
device.action.lxcupgrade
========================


Operation: POST /dataservice/device/action/lxcupgrade
-----------------------------------------------------


Process an upgrade operation

.. code:: python

    def process_lxc_upgrade(payload: Optional[Any] = None) -> Any: ...


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
        client.device.action.lxcupgrade.process_lxc_upgrade()


