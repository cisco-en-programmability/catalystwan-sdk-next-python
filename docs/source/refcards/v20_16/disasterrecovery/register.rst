=========================
disasterrecovery.register
=========================


Operation: PUT /dataservice/disasterrecovery/register
-----------------------------------------------------


Update data centers for disaster recovery

.. code:: python

    def update_1(payload: Optional[Any] = None) -> Any: ...


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
        client.disasterrecovery.register.update_1()


Operation: POST /dataservice/disasterrecovery/register
------------------------------------------------------


Register data centers for disaster recovery

.. code:: python

    def register(payload: Optional[Any] = None) -> Any: ...


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
        client.disasterrecovery.register.register()


