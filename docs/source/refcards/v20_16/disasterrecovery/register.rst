=========================
disasterrecovery.register
=========================


Operation: PUT /dataservice/disasterrecovery/register
-----------------------------------------------------


Update data centers for disaster recovery

.. code:: python

    def put(payload: Any) -> Any: ...


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
        client.disasterrecovery.register.put()


Operation: POST /dataservice/disasterrecovery/register
------------------------------------------------------


Register data centers for disaster recovery

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.disasterrecovery.register.post()


