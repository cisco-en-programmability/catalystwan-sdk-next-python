============================
v1.device.analyze_cli_config
============================


Operation: POST /dataservice/v1/device/analyzeCliConfig
-------------------------------------------------------


Analyze CLI Config for device

.. code:: python

    def post(payload: AnalyzeCliConfig) -> Any: ...


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
        client.v1.device.analyze_cli_config.post()


.. toctree::
    :maxdepth: 1

    models

