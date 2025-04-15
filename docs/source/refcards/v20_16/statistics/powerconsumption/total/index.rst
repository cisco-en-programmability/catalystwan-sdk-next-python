=================================
statistics.powerconsumption.total
=================================


Operation: POST /dataservice/statistics/powerconsumption/total
--------------------------------------------------------------


Get Power Consumption Total stats

.. code:: python

    def post(payload: Any) -> PowerConsumptionTotalResp: ...


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
        client.statistics.powerconsumption.total.post()


.. toctree::
    :maxdepth: 1

    models

