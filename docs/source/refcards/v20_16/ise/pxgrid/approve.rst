==================
ise.pxgrid.approve
==================


Operation: PUT /dataservice/ise/pxgrid/approve
----------------------------------------------


Approve pxGrid account

.. code:: python

    def put() -> bool: ...


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
        client.ise.pxgrid.approve.put()


