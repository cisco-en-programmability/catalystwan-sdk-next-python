==============================
template.cloudx.attachedclient
==============================


Operation: GET /dataservice/template/cloudx/attachedclient
----------------------------------------------------------


Get attached client site list

.. code:: python

    def get() -> List[Any]: ...


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
        client.template.cloudx.attachedclient.get()


