===================
device.unconfigured
===================


Operation: GET /dataservice/device/unconfigured
-----------------------------------------------


Get wan edge devices not configured by vManage (that is, those in CLI mode)

.. code:: python

    def get() -> List[Device]: ...


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
        client.device.unconfigured.get()


.. toctree::
    :maxdepth: 1

    models

