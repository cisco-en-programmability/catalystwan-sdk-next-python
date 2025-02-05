=========================
cloudservices.accesstoken
=========================


Operation: GET /dataservice/cloudservices/accesstoken
-----------------------------------------------------


.. code:: python

    def get_access_tokenfor_device() -> None: ...


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
        client.cloudservices.accesstoken.get_access_tokenfor_device()


