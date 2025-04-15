==================
tenantstatus.force
==================


Operation: POST /dataservice/tenantstatus/force
-----------------------------------------------


Force tenant status collection<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

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
        client.tenantstatus.force.post()


