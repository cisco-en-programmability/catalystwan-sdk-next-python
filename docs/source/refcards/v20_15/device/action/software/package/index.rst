==============================
device.action.software.package
==============================


Operation: GET /dataservice/device/action/software/package/{fileName}
---------------------------------------------------------------------


Download software package file

.. code:: python

    def get(
        file_name: str, image_type: Optional[str] = "software"
    ) -> str: ...


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
        client.device.action.software.package.get()


Operation: POST /dataservice/device/action/software/package
-----------------------------------------------------------


.. code:: python

    @overload
    def post(payload: InstallPkg) -> None: ...


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
        client.device.action.software.package.post()


Operation: POST /dataservice/device/action/software/package/{imageType}
-----------------------------------------------------------------------


.. code:: python

    @overload
    def post(payload: InstallPkg, image_type: str) -> None: ...


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
        client.device.action.software.package.post()


.. toctree::
    :maxdepth: 1

    image_count
    signature/index
    utdsignature/index
    metadata
    models

