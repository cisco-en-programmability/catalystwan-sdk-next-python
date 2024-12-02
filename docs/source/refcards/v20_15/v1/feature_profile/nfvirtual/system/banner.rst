==========================================
v1.feature_profile.nfvirtual.system.banner
==========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner
----------------------------------------------------------------------------------


Create Banner Profile Parcel for System feature profile

.. code:: python

    def create_nfvirtual_banner_parcel(
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
        client.v1.feature_profile.nfvirtual.system.banner.create_nfvirtual_banner_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}
--------------------------------------------------------------------------------------------


Get Banner Profile Parcels for System feature profile

.. code:: python

    def get_nfvirtual_banner_parcel(
        system_id: str, banner_id: str
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
        client.v1.feature_profile.nfvirtual.system.banner.get_nfvirtual_banner_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}
--------------------------------------------------------------------------------------------


Edit a  Banner Profile Parcel for System feature profile

.. code:: python

    def edit_nfvirtual_banner_parcel(
        system_id: str, banner_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.banner.edit_nfvirtual_banner_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}
-----------------------------------------------------------------------------------------------


Delete a Banner Profile Parcel for System feature profile

.. code:: python

    def delete_nfvirtual_banner_parcel(
        system_id: str, banner_id: str
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
        client.v1.feature_profile.nfvirtual.system.banner.delete_nfvirtual_banner_parcel()


