=====================
v1.licensing.licenses
=====================


Operation: POST /dataservice/v1/licensing/licenses
--------------------------------------------------


Get applicable licenses based on platform class

.. code:: python

    def get_msla_licenses(
        payload: Optional[LicensesRequest] = None,
    ) -> LicensesResponse: ...


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
        client.v1.licensing.licenses.get_msla_licenses()


.. toctree::
    :maxdepth: 1

    models

