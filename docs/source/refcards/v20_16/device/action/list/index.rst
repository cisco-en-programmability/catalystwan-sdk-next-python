==================
device.action.list
==================


Operation: GET /dataservice/device/action/list
----------------------------------------------


Get device action list

.. code:: python

    def get() -> List[GenerateDeviceActionListInner]: ...


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
        client.device.action.list.get()


.. toctree::
    :maxdepth: 1

    models

