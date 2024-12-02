================
device.bfd.links
================


Operation: GET /dataservice/device/bfd/links
--------------------------------------------


Get list of BFD connections

.. code:: python

    def create_bfd_link_list(state: str) -> List[Any]: ...


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
        client.device.bfd.links.create_bfd_link_list()


