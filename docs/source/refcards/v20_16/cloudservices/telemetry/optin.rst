=============================
cloudservices.telemetry.optin
=============================


Operation: PUT /dataservice/cloudservices/telemetry/optin
---------------------------------------------------------


Telemetry Opt In

.. code:: python

    def put(payload: str) -> Any: ...


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
        client.cloudservices.telemetry.optin.put()


