==============================
cloudservices.telemetry.optout
==============================


Operation: DELETE /dataservice/cloudservices/telemetry/optout
-------------------------------------------------------------


Telemetry Opt Out

.. code:: python

    def delete(payload: Optional[str] = None) -> Any: ...


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
        client.cloudservices.telemetry.optout.delete()


