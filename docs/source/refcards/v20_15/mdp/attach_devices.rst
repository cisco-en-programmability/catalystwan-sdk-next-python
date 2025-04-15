==================
mdp.attach_devices
==================


Operation: GET /dataservice/mdp/attachDevices/{nmsId}
-----------------------------------------------------


Retrieve MDP attached devices

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
        client.mdp.attach_devices.get()


Operation: PUT /dataservice/mdp/attachDevices/{nmsId}
-----------------------------------------------------


Edit attached devices

.. code:: python

    def put(nms_id: str, payload: Any) -> Any: ...


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
        client.mdp.attach_devices.put()


Operation: POST /dataservice/mdp/attachDevices/{nmsId}
------------------------------------------------------


Share devices with MDP

.. code:: python

    def post(nms_id: str, payload: Any) -> Any: ...


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
        client.mdp.attach_devices.post()


