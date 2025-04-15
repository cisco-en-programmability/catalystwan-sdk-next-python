=============
networkdesign
=============


Operation: GET /dataservice/networkdesign
-----------------------------------------


Deprecated!!!

Get existing network design

.. code:: python

    def get() -> Any: ...


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
        client.networkdesign.get()


Operation: PUT /dataservice/networkdesign
-----------------------------------------


Deprecated!!!

Edit network segment

.. code:: python

    def put(id: str, payload: Any) -> Any: ...


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
        client.networkdesign.put()


Operation: POST /dataservice/networkdesign
------------------------------------------


Deprecated!!!

Create network design

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.networkdesign.post()


.. toctree::
    :maxdepth: 1

    attachment
    circuit
    global_/index
    lock/index
    mytest
    profile/index
    service_profile_config

