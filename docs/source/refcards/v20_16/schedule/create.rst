===============
schedule.create
===============


Operation: POST /dataservice/schedule/create
--------------------------------------------


create  backup scheduler config-db and statstics database with startDateTime and persist to config-db

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
        client.schedule.create.post()


