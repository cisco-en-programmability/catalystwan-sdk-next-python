====================
device.control.links
====================


Operation: GET /dataservice/device/control/links
------------------------------------------------


Get connections list

.. code:: python

    def create_link_list(state: str) -> List[Any]: ...


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
        client.device.control.links.create_link_list()


