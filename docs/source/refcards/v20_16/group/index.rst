=====
group
=====


Operation: GET /dataservice/group
---------------------------------


Retrieve device group list

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
        client.group.get()


.. toctree::
    :maxdepth: 1

    device
    devices/index
    map/index

