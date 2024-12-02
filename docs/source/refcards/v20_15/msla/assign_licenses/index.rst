====================
msla.assign_licenses
====================


Operation: POST /dataservice/msla/assignLicenses
------------------------------------------------


Assign msla licenses to devices

.. code:: python

    def assign_msla_licenses_to_devices(
        payload: Optional[AssignMslaLicenses] = None,
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
        client.msla.assign_licenses.assign_msla_licenses_to_devices()


.. toctree::
    :maxdepth: 1

    models

