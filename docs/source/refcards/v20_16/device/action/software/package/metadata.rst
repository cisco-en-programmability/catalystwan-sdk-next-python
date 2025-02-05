=======================================
device.action.software.package.metadata
=======================================


Operation: GET /dataservice/device/action/software/package/{versionId}/metadata
-------------------------------------------------------------------------------


Update Package Metadata

.. code:: python

    def get_image_metadata(version_id: str) -> Any: ...


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
        client.device.action.software.package.metadata.get_image_metadata()


Operation: PUT /dataservice/device/action/software/package/{versionId}/metadata
-------------------------------------------------------------------------------


Update Package Metadata

.. code:: python

    def edit_image_metadata(
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
        client.device.action.software.package.metadata.edit_image_metadata()


