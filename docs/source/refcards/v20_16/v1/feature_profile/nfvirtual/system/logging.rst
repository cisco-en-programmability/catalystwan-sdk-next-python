===========================================
v1.feature_profile.nfvirtual.system.logging
===========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging
-----------------------------------------------------------------------------------


Create Logging Profile Parcel for System feature profile

.. code:: python

    def create_nfvirtual_logging_parcel(
        system_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.logging.create_nfvirtual_logging_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


Get Logging Profile Parcels for System feature profile

.. code:: python

    def get_nfvirtual_logging_parcel(
        system_id: str, logging_id: str
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
        client.v1.feature_profile.nfvirtual.system.logging.get_nfvirtual_logging_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


Edit a  Logging Profile Parcel for System feature profile

.. code:: python

    def edit_nfvirtual_logging_parcel(
        system_id: str, logging_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.logging.edit_nfvirtual_logging_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}
-------------------------------------------------------------------------------------------------


Delete a Logging Profile Parcel for System feature profile

.. code:: python

    def delete_nfvirtual_logging_parcel(
        system_id: str, logging_id: str
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
        client.v1.feature_profile.nfvirtual.system.logging.delete_nfvirtual_logging_parcel()


