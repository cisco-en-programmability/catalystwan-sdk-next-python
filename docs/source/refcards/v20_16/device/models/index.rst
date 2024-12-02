=============
device.models
=============


Operation: GET /dataservice/device/models
-----------------------------------------


Get all device models supported by the vManage

.. code:: python

    def list_all_device_models() -> DeviceModelsResponse: ...


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
        client.device.models.list_all_device_models()


Operation: GET /dataservice/device/models/{uuid}
------------------------------------------------


Get device model for the device

.. code:: python

    def get_device_models(uuid: str) -> Any: ...


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
        client.device.models.get_device_models()


.. toctree::
    :maxdepth: 1

    models

