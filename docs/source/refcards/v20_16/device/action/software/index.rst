======================
device.action.software
======================


Operation: GET /dataservice/device/action/software
--------------------------------------------------


Get software images

.. code:: python

    def find_software_images() -> Any: ...


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
        client.device.action.software.find_software_images()


Operation: POST /dataservice/device/action/software
---------------------------------------------------


Create software image URL

.. code:: python

    def create_image_url(payload: Optional[Any] = None) -> None: ...


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
        client.device.action.software.create_image_url()


Operation: PUT /dataservice/device/action/software/{versionId}
--------------------------------------------------------------


Deprecated!!!

Update software image URL

.. code:: python

    def update_image_url(
        version_id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.device.action.software.update_image_url()


Operation: DELETE /dataservice/device/action/software/{versionId}
-----------------------------------------------------------------


Delete software image URL

.. code:: python

    def delete_image_url(version_id: str) -> None: ...


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
        client.device.action.software.delete_image_url()


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

