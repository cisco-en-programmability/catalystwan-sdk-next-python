===========================
sdavc.cloud_sourced.approve
===========================


Operation: POST /dataservice/sdavc/cloud-sourced/approve
--------------------------------------------------------


.. code:: python

    def approve_extended_applications(
        payload: Optional[ExtendedApplicationRequestData] = None,
    ) -> DefaultSuccessResponse: ...


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
        client.sdavc.cloud_sourced.approve.approve_extended_applications()


.. toctree::
    :maxdepth: 1

    models

