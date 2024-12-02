=============
networkdesign
=============


Operation: GET /dataservice/networkdesign
-----------------------------------------


Deprecated!!!

Get existing network design

.. code:: python

    def get_network_design() -> Any: ...


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
        client.networkdesign.get_network_design()


Operation: PUT /dataservice/networkdesign
-----------------------------------------


Deprecated!!!

Edit network segment

.. code:: python

    def edit_network_design(
        id: str, payload: Optional[Any] = None
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
        client.networkdesign.edit_network_design()


Operation: POST /dataservice/networkdesign
------------------------------------------


Deprecated!!!

Create network design

.. code:: python

    def create_network_design(payload: Optional[Any] = None) -> Any: ...


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
        client.networkdesign.create_network_design()


.. toctree::
    :maxdepth: 1

    attachment
    circuit
    global_/index
    lock/index
    mytest
    profile/index
    service_profile_config

