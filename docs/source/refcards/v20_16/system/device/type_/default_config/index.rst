==================================
system.device.type_.default_config
==================================


Operation: GET /dataservice/system/device/type/{deviceCategory}/defaultConfig
-----------------------------------------------------------------------------


Deprecated!!!

Get devices default config

.. code:: python

    def get(device_category: DeviceCategoryParam) -> List[Any]: ...


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
        client.system.device.type_.default_config.get()


.. toctree::
    :maxdepth: 1

    models

