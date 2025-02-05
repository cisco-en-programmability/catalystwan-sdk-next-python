======================================
cloudservices.vanalytics.dashboardlist
======================================


Operation: GET /dataservice/cloudservices/vanalytics/dashboardlist
------------------------------------------------------------------


Get vAnalytics Dashboard List

.. code:: python

    def getv_analytics_dashboard_list() -> Any: ...


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
        client.cloudservices.vanalytics.dashboardlist.getv_analytics_dashboard_list()


