==============================
device.action.software.package
==============================


Operation: POST /dataservice/device/action/software/package
-----------------------------------------------------------


Install software package

.. code:: python

    def install_pkg(payload: Optional[InstallPkg] = None) -> None: ...


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
        client.device.action.software.package.install_pkg()


Operation: GET /dataservice/device/action/software/package/{fileName}
---------------------------------------------------------------------


Download software package file

.. code:: python

    def download_package_file(
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
        client.device.action.software.package.download_package_file()


Operation: POST /dataservice/device/action/software/package/{imageType}
-----------------------------------------------------------------------


Install software image package

.. code:: python

    def process_software_image(
        image_type: str, payload: Optional[InstallPkg] = None
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
        client.device.action.software.package.process_software_image()


.. toctree::
    :maxdepth: 1

    image_count
    signature/index
    utdsignature/index
    metadata
    models

