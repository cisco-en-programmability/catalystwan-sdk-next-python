==================================
device.action.software.ztp.version
==================================


Operation: GET /dataservice/device/action/software/ztp/version
--------------------------------------------------------------


Get ZTP software version

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
        client.device.action.software.ztp.version.get()


