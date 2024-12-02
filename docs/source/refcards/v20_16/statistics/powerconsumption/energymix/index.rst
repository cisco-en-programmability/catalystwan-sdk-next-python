=====================================
statistics.powerconsumption.energymix
=====================================


Operation: POST /dataservice/statistics/powerconsumption/energymix
------------------------------------------------------------------


Get Power Consumption Energy Mix

.. code:: python

    def get_power_consumption_energy_mix(
        payload: Optional[Any] = None,
    ) -> PowerConsumptionEnergyMixResp: ...


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
        client.statistics.powerconsumption.energymix.get_power_consumption_energy_mix()


.. toctree::
    :maxdepth: 1

    models

