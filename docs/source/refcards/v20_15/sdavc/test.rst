==========
sdavc.test
==========


Operation: POST /dataservice/sdavc/test
---------------------------------------


Test SD_AVC load balancer

.. code:: python

    def post() -> None: ...


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
        client.sdavc.test.post()


