============================================
template.cor.transitvpc.autoscale_properties
============================================


Operation: PUT /dataservice/template/cor/transitvpc/autoscale-properties
------------------------------------------------------------------------


Deprecated!!!

Update transit VPC autoscale properties

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
        client.template.cor.transitvpc.autoscale_properties.put()


