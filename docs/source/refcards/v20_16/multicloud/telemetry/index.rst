====================
multicloud.telemetry
====================


Operation: POST /dataservice/multicloud/telemetry
-------------------------------------------------


Reports telemetry data

.. code:: python

    def post(payload: TelemetryRequests) -> Taskid: ...


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
        client.multicloud.telemetry.post()


.. toctree::
    :maxdepth: 1

    models

