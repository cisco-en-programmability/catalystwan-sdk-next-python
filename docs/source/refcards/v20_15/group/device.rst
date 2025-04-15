============
group.device
============


Operation: GET /dataservice/group/device
----------------------------------------


Retrieve device groups

.. code:: python

    def get(site_id: Optional[str] = None) -> List[Any]: ...


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
        client.group.device.get()


