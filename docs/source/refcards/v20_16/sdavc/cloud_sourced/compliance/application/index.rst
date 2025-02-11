==========================================
sdavc.cloud_sourced.compliance.application
==========================================


Operation: POST /dataservice/sdavc/cloud-sourced/compliance/application
-----------------------------------------------------------------------


.. code:: python

    def application_compliance_with_extended_applications(
        payload: Optional[ExtendedApplicationRequestData] = None,
    ) -> Application: ...


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
        client.sdavc.cloud_sourced.compliance.application.application_compliance_with_extended_applications()


.. toctree::
    :maxdepth: 1

    models

