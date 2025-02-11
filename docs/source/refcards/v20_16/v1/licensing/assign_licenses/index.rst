============================
v1.licensing.assign_licenses
============================


Operation: POST /dataservice/v1/licensing/assign-licenses
---------------------------------------------------------


Assign licenses to devices

.. code:: python

    def assign_msla_licenses(
        payload: Optional[AssignLicensesRequest] = None,
    ) -> None: ...


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
        client.v1.licensing.assign_licenses.assign_msla_licenses()


.. toctree::
    :maxdepth: 1

    models

