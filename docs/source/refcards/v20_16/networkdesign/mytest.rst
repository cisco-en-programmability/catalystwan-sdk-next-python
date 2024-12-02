====================
networkdesign.mytest
====================


Operation: GET /dataservice/networkdesign/mytest/{name}
-------------------------------------------------------


Deprecated!!!

Get all device templates for this feature template

.. code:: python

    def run_my_test(name: str) -> Any: ...


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
        client.networkdesign.mytest.run_my_test()


