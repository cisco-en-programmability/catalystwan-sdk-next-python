=======================================
v1.feature_profile.nfvirtual.system.aaa
=======================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa
-------------------------------------------------------------------------------


Create AAA Profile Parcel for System feature profile

.. code:: python

    def create_nfvirtual_aaa_parcel(
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
        client.v1.feature_profile.nfvirtual.system.aaa.create_nfvirtual_aaa_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}
--------------------------------------------------------------------------------------


Get AAA Profile Parcels for System feature profile

.. code:: python

    def get_nfvirtual_aaa_parcel(system_id: str, aaa_id: str) -> str: ...


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
        client.v1.feature_profile.nfvirtual.system.aaa.get_nfvirtual_aaa_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}
--------------------------------------------------------------------------------------


Edit a  AAA Profile Parcel for System feature profile

.. code:: python

    def edit_nfvirtual_aaa_parcel(
        system_id: str, aaa_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.aaa.edit_nfvirtual_aaa_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}
-----------------------------------------------------------------------------------------


Delete a AAA Profile Parcel for System feature profile

.. code:: python

    def delete_nfvirtual_aaa_parcel(
        system_id: str, aaa_id: str
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
        client.v1.feature_profile.nfvirtual.system.aaa.delete_nfvirtual_aaa_parcel()


