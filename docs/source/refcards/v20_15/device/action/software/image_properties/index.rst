=======================================
device.action.software.image_properties
=======================================


Operation: GET /dataservice/device/action/software/imageProperties/{versionId}
------------------------------------------------------------------------------


Get Image Properties

.. code:: python

    def get_image_properties(version_id: str) -> GetImageProperties: ...


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
        client.device.action.software.image_properties.get_image_properties()


.. toctree::
    :maxdepth: 1

    models

