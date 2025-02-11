=========================================
template.feature.default.networkinterface
=========================================


Operation: GET /dataservice/template/feature/default/networkinterface
---------------------------------------------------------------------


Get default network interface<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_network_interface(device_model: DeviceModelParam) -> Any: ...


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
        client.template.feature.default.networkinterface.get_network_interface()


.. toctree::
    :maxdepth: 1

    models

