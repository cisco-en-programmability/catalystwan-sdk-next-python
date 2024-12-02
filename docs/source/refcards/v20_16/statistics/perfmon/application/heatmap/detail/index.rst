=============================================
statistics.perfmon.application.heatmap.detail
=============================================


Operation: GET /dataservice/statistics/perfmon/application/heatmap/detail
-------------------------------------------------------------------------


Get single applicaiton site health detail in a time range

.. code:: python

    def get_application_heat_map_detail(
        application: str,
        start_time: int,
        heatmap_time: int,
        siteid: Optional[str] = None,
        last_n_hours: Optional[LastNHoursParam] = "12",
    ) -> List[ApplicationHeatMapDetail]: ...


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
        client.statistics.perfmon.application.heatmap.detail.get_application_heat_map_detail()


.. toctree::
    :maxdepth: 1

    models

