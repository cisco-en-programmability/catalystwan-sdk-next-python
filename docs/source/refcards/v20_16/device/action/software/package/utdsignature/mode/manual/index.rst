=======================================================
device.action.software.package.utdsignature.mode.manual
=======================================================


Operation: POST /dataservice/device/action/software/package/utdsignature/{type}/mode/manual
-------------------------------------------------------------------------------------------


upload Utd image

.. code:: python

    def upload_utd_image(
        type_: str, payload: Optional[InstallPkg] = None
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
        client.device.action.software.package.utdsignature.mode.manual.upload_utd_image()


.. toctree::
    :maxdepth: 1

    models

