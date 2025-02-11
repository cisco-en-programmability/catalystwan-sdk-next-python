=================================
statistics.powerconsumption.total
=================================


Operation: POST /dataservice/statistics/powerconsumption/total
--------------------------------------------------------------


Get Power Consumption Total stats

.. code:: python

    def get_power_consumption_total(
        payload: Optional[Any] = None,
    ) -> PowerConsumptionTotalResp: ...


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
        client.statistics.powerconsumption.total.get_power_consumption_total()


.. toctree::
    :maxdepth: 1

    models

