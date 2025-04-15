====================
msla.assign_licenses
====================


Operation: POST /dataservice/msla/assignLicenses
------------------------------------------------


Assign msla licenses to devices

.. code:: python

    def post(payload: AssignMslaLicenses) -> None: ...


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
        client.msla.assign_licenses.post()


.. toctree::
    :maxdepth: 1

    models

