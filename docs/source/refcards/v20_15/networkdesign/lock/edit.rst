=======================
networkdesign.lock.edit
=======================


Operation: POST /dataservice/networkdesign/lock/edit
----------------------------------------------------


Deprecated!!!

Acquire edit lock

.. code:: python

    def post() -> Any: ...


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
        client.networkdesign.lock.edit.post()


