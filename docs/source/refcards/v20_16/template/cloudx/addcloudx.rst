=========================
template.cloudx.addcloudx
=========================


Operation: POST /dataservice/template/cloudx/addcloudx/{type}
-------------------------------------------------------------


Deprecated!!!

Add cloudx gateway

.. code:: python

    def add_cloudx_type(
        type_: str, payload: Optional[Any] = None
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
        client.template.cloudx.addcloudx.add_cloudx_type()


