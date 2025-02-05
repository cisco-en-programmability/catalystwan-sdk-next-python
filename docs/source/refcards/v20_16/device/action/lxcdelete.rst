=======================
device.action.lxcdelete
=======================


Operation: POST /dataservice/device/action/lxcdelete
----------------------------------------------------


Process a delete operation

.. code:: python

    def process_lxc_delete(payload: Optional[Any] = None) -> Any: ...


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
        client.device.action.lxcdelete.process_lxc_delete()


