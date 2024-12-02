=================================
template.feature.default.networks
=================================


Operation: GET /dataservice/template/feature/default/networks
-------------------------------------------------------------


Get default networks<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_default_networks(device_model: DeviceModelParam) -> Any: ...


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
        client.template.feature.default.networks.get_default_networks()


.. toctree::
    :maxdepth: 1

    models

