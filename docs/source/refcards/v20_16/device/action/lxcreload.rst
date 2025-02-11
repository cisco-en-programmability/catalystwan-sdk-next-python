=======================
device.action.lxcreload
=======================


Operation: POST /dataservice/device/action/lxcreload
----------------------------------------------------


Process a reload operation

.. code:: python

    def process_lxc_reload(payload: Optional[Any] = None) -> Any: ...


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
        client.device.action.lxcreload.process_lxc_reload()


