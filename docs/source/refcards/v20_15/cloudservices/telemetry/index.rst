=======================
cloudservices.telemetry
=======================


Operation: GET /dataservice/cloudservices/telemetry
---------------------------------------------------


Get Telemetry state

.. code:: python

    def get() -> Any: ...


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
        client.cloudservices.telemetry.get()


.. toctree::
    :maxdepth: 1

    optin
    optout

