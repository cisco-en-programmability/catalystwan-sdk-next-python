=====================================
statistics.powerconsumption.energymix
=====================================


Operation: POST /dataservice/statistics/powerconsumption/energymix
------------------------------------------------------------------


Get Power Consumption Energy Mix

.. code:: python

    def post(payload: Any) -> PowerConsumptionEnergyMixResp: ...


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
        client.statistics.powerconsumption.energymix.post()


.. toctree::
    :maxdepth: 1

    models

