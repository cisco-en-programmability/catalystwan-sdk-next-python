===================
system.reverseproxy
===================


Operation: GET /dataservice/system/reverseproxy/{uuid}
------------------------------------------------------


Get reverse proxy IP/Port mappings for controller

.. code:: python

    def get(uuid: str) -> Any: ...


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
        client.system.reverseproxy.get()


Operation: POST /dataservice/system/reverseproxy/{uuid}
-------------------------------------------------------


Create reverse proxy IP/Port mappings for controller

.. code:: python

    def post(uuid: str, payload: Any) -> None: ...


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
        client.system.reverseproxy.post()


