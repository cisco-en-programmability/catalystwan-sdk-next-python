===========================
multicloud.cloudgatewaytype
===========================


Operation: GET /dataservice/multicloud/cloudgatewaytype
-------------------------------------------------------


Get cloud gateway types for specified cloudType

.. code:: python

    def get_cgw_types(
        cloud_type: Optional[CloudTypeParam] = None,
    ) -> Any: ...


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
        client.multicloud.cloudgatewaytype.get_cgw_types()


.. toctree::
    :maxdepth: 1

    models

