==========================================
sdavc.cloud_sourced.compliance.application
==========================================


Operation: POST /dataservice/sdavc/cloud-sourced/compliance/application
-----------------------------------------------------------------------


.. code:: python

    def post(payload: ExtendedApplicationRequestData) -> Application: ...


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
        client.sdavc.cloud_sourced.compliance.application.post()


.. toctree::
    :maxdepth: 1

    models

