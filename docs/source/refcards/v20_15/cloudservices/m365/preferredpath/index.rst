================================
cloudservices.m365.preferredpath
================================


Operation: POST /dataservice/cloudservices/m365/preferredpath
-------------------------------------------------------------


Get vAnalytics Preferred Path for Office365 over time. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def post(
        payload: GetO365PreferredPathFromVAnalyticsPostRequest,
    ) -> None: ...


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
        client.cloudservices.m365.preferredpath.post()


.. toctree::
    :maxdepth: 1

    models

