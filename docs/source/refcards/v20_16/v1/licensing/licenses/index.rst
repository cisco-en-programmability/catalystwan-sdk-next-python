=====================
v1.licensing.licenses
=====================


Operation: POST /dataservice/v1/licensing/licenses
--------------------------------------------------


Get applicable licenses based on platform class

.. code:: python

    def post(payload: LicensesRequest) -> LicensesResponse: ...


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
        client.v1.licensing.licenses.post()


.. toctree::
    :maxdepth: 1

    models

