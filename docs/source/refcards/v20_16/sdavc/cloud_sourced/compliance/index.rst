==============================
sdavc.cloud_sourced.compliance
==============================


Operation: POST /dataservice/sdavc/cloud-sourced/compliance
-----------------------------------------------------------


.. code:: python

    def compliance_with_extended_applications(
        payload: Optional[ExtendedApplicationRequestData] = None,
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
        client.sdavc.cloud_sourced.compliance.compliance_with_extended_applications()


.. toctree::
    :maxdepth: 1

    application/index
    models

