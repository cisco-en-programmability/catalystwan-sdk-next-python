=======================
cloudservices.authtoken
=======================


Operation: POST /dataservice/cloudservices/authtoken
----------------------------------------------------


Get Azure token

.. code:: python

    def post(payload: str) -> Any: ...


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
        client.cloudservices.authtoken.post()


