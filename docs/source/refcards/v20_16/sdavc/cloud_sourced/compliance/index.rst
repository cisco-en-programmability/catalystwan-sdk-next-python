==============================
sdavc.cloud_sourced.compliance
==============================


Operation: POST /dataservice/sdavc/cloud-sourced/compliance
-----------------------------------------------------------


.. code:: python

    def post(
        payload: ExtendedApplicationRequestData,
    ) -> PolicyComplianceResponse: ...


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
        client.sdavc.cloud_sourced.compliance.post()


.. toctree::
    :maxdepth: 1

    application/index
    models

