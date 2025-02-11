=========================
cloudservices.credentials
=========================


Operation: GET /dataservice/cloudservices/credentials
-----------------------------------------------------


Get cloud service credentials

.. code:: python

    def get_cloud_credentials() -> Any: ...


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
        client.cloudservices.credentials.get_cloud_credentials()


Operation: POST /dataservice/cloudservices/credentials
------------------------------------------------------


Add cloud service credentials

.. code:: python

    def add_cloud_credentials(payload: Optional[Any] = None) -> None: ...


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
        client.cloudservices.credentials.add_cloud_credentials()


