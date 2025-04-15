========================================
device.action.software.package.signature
========================================


Operation: GET /dataservice/device/action/software/package/signature/{utdsignature}
-----------------------------------------------------------------------------------


Get list of Utd images

.. code:: python

    def get(utdsignature: UtdsignatureParam, type_: str) -> ImageData: ...


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
        client.device.action.software.package.signature.get()


.. toctree::
    :maxdepth: 1

    models

