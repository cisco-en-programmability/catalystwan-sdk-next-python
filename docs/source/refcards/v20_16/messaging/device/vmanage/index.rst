========================
messaging.device.vmanage
========================


Operation: GET /dataservice/messaging/device/vmanage
----------------------------------------------------


Create device vManage connection list

.. code:: python

    def get() -> List[MessagingResp]: ...


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
        client.messaging.device.vmanage.get()


.. toctree::
    :maxdepth: 1

    models

