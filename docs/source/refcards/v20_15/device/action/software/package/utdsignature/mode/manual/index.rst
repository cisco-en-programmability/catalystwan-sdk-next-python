=======================================================
device.action.software.package.utdsignature.mode.manual
=======================================================


Operation: POST /dataservice/device/action/software/package/utdsignature/{type}/mode/manual
-------------------------------------------------------------------------------------------


upload Utd image

.. code:: python

    def post(type_: str, payload: InstallPkg) -> None: ...


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
        client.device.action.software.package.utdsignature.mode.manual.post()


.. toctree::
    :maxdepth: 1

    models

