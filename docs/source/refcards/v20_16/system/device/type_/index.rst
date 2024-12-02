===================
system.device.type_
===================


Operation: GET /dataservice/system/device/type/{deviceCategory}
---------------------------------------------------------------


Deprecated!!!

Get devices details

.. code:: python

    def get_cloud_dock_data_based_on_device_type(
        device_category: DeviceCategoryParam,
    ) -> List[Any]: ...


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
        client.system.device.type_.get_cloud_dock_data_based_on_device_type()


.. toctree::
    :maxdepth: 1

    default_config/index
    models

