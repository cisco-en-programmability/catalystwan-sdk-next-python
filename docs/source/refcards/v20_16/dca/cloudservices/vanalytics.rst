============================
dca.cloudservices.vanalytics
============================


Operation: POST /dataservice/dca/cloudservices/vanalytics
---------------------------------------------------------


Get session from DCS for vAnalytics

.. code:: python

    def getv_analytics(payload: Optional[str] = None) -> Any: ...


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
        client.dca.cloudservices.vanalytics.getv_analytics()


