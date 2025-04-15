===================================
template.config.device.mode.vmanage
===================================


Operation: GET /dataservice/template/config/device/mode/vmanage
---------------------------------------------------------------


Get list of devices that are allowable for vmanage modes

.. code:: python

    def get(type_: TypeParam) -> List[Any]: ...


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
        client.template.config.device.mode.vmanage.get()


.. toctree::
    :maxdepth: 1

    models

