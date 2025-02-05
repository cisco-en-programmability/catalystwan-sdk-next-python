===========================
template.cloudx.gatewaylist
===========================


Operation: GET /dataservice/template/cloudx/gatewaylist
-------------------------------------------------------


Get gateway list

.. code:: python

    def get_gateway_list() -> List[Any]: ...


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
        client.template.cloudx.gatewaylist.get_gateway_list()


