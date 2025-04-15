======================
device.action.software
======================


Operation: GET /dataservice/device/action/software
--------------------------------------------------


Get software images

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
        client.device.action.software.get()


Operation: POST /dataservice/device/action/software
---------------------------------------------------


Create software image URL

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.device.action.software.post()


Operation: PUT /dataservice/device/action/software/{versionId}
--------------------------------------------------------------


Deprecated!!!

Update software image URL

.. code:: python

    def put(version_id: str, payload: Any) -> None: ...


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
        client.device.action.software.put()


Operation: DELETE /dataservice/device/action/software/{versionId}
-----------------------------------------------------------------


Delete software image URL

.. code:: python

    def delete(version_id: str) -> None: ...


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
        client.device.action.software.delete()


.. toctree::
    :maxdepth: 1

    image_properties/index
    images/index
    package/index
    remoteserver
    vedge/index
    version/index
    vnfproperties/index
    ztp/index

