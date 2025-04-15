===========
mdp.devices
===========


Operation: GET /dataservice/mdp/devices/{nmsId}
-----------------------------------------------


Retrieve MDP supported devices

.. code:: python

    def get(nms_id: str) -> List[Any]: ...


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
        client.mdp.devices.get()


