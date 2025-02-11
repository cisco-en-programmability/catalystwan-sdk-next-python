=================
dca.cloudservices
=================


Operation: GET /dataservice/dca/cloudservices
---------------------------------------------


Get cloud service settings

.. code:: python

    def get_cloud_settings() -> Any: ...


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
        client.dca.cloudservices.get_cloud_settings()


.. toctree::
    :maxdepth: 1

    accesstoken
    alarm
    idtoken
    otp
    telemetry
    vanalytics

