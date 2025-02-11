===================
system.reverseproxy
===================


Operation: GET /dataservice/system/reverseproxy/{uuid}
------------------------------------------------------


Get reverse proxy IP/Port mappings for controller

.. code:: python

    def get_reverse_proxy_mappings(uuid: str) -> Any: ...


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
        client.system.reverseproxy.get_reverse_proxy_mappings()


Operation: POST /dataservice/system/reverseproxy/{uuid}
-------------------------------------------------------


Create reverse proxy IP/Port mappings for controller

.. code:: python

    def create_reverse_proxy_mappings(
        uuid: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.system.reverseproxy.create_reverse_proxy_mappings()


