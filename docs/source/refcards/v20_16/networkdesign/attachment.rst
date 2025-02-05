========================
networkdesign.attachment
========================


Operation: POST /dataservice/networkdesign/attachment
-----------------------------------------------------


Deprecated!!!

Attach network design

.. code:: python

    def push_network_design(payload: Optional[Any] = None) -> Any: ...


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
        client.networkdesign.attachment.push_network_design()


