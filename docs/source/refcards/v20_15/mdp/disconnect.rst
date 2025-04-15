==============
mdp.disconnect
==============


Operation: GET /dataservice/mdp/disconnect/{nmsId}
--------------------------------------------------


disconnect from mpd controller

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
        client.mdp.disconnect.get()


