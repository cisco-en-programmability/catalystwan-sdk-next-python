=====================
cloudservices.staging
=====================


Operation: GET /dataservice/cloudservices/staging
-------------------------------------------------


Check if testbed or production

.. code:: python

    def is_staging() -> Any: ...


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
        client.cloudservices.staging.is_staging()


