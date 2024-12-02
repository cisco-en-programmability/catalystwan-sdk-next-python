==========================
template.cloudx.interfaces
==========================


Operation: POST /dataservice/template/cloudx/interfaces
-------------------------------------------------------


Enable cloudx gateway

.. code:: python

    def add_cloudx_interfaces(payload: Optional[Any] = None) -> None: ...


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
        client.template.cloudx.interfaces.add_cloudx_interfaces()


