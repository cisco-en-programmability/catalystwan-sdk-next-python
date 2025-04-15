=============
device.models
=============


Operation: GET /dataservice/device/models
-----------------------------------------


.. code:: python

    @overload
    def get(list: str) -> DeviceModelsResponse: ...


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
        client.device.models.get()


Operation: GET /dataservice/device/models/{uuid}
------------------------------------------------


.. code:: python

    @overload
    def get(uuid: str) -> Any: ...


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
        client.device.models.get()


.. toctree::
    :maxdepth: 1

    models

