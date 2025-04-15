==========================
v1.licensing.edit_licenses
==========================


Operation: GET /dataservice/v1/licensing/edit-licenses/{uuid}
-------------------------------------------------------------


Edit licenses associated to a device

.. code:: python

    def get(uuid: str) -> EditLicenseResponse: ...


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
        client.v1.licensing.edit_licenses.get()


.. toctree::
    :maxdepth: 1

    models

