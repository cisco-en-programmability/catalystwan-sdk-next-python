======================
device.action.lxcreset
======================


Operation: POST /dataservice/device/action/lxcreset
---------------------------------------------------


Process a reset operation

.. code:: python

    def process_lxc_reset(payload: Optional[Any] = None) -> Any: ...


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
        client.device.action.lxcreset.process_lxc_reset()


