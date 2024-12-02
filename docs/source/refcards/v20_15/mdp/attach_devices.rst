==================
mdp.attach_devices
==================


Operation: GET /dataservice/mdp/attachDevices/{nmsId}
-----------------------------------------------------


Retrieve MDP attached devices

.. code:: python

    def retrieve_mdp_attached_devices(nms_id: str) -> List[Any]: ...


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
        client.mdp.attach_devices.retrieve_mdp_attached_devices()


Operation: PUT /dataservice/mdp/attachDevices/{nmsId}
-----------------------------------------------------


Edit attached devices

.. code:: python

    def edit_attached_devices(
        nms_id: str, payload: Optional[Any] = None
    ) -> Any: ...


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
        client.mdp.attach_devices.edit_attached_devices()


Operation: POST /dataservice/mdp/attachDevices/{nmsId}
------------------------------------------------------


Share devices with MDP

.. code:: python

    def attach_devices(
        nms_id: str, payload: Optional[Any] = None
    ) -> Any: ...


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
        client.mdp.attach_devices.attach_devices()


