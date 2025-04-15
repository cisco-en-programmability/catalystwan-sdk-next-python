==========================================
v1.feature_profile.nfvirtual.system.banner
==========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner
----------------------------------------------------------------------------------


Create Banner Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateNfvirtualBannerParcelPostRequest
    ) -> CreateNfvirtualBannerParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.banner.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}
--------------------------------------------------------------------------------------------


Get Banner Profile Parcels for System feature profile

.. code:: python

    def get(
        system_id: str, banner_id: str
    ) -> GetSingleNfvirtualSystemBannerPayload: ...


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
        client.v1.feature_profile.nfvirtual.system.banner.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}
--------------------------------------------------------------------------------------------


Edit a  Banner Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        banner_id: str,
        payload: EditNfvirtualBannerParcelPutRequest,
    ) -> EditNfvirtualBannerParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.banner.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}
-----------------------------------------------------------------------------------------------


Delete a Banner Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, banner_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.system.banner.delete()


.. toctree::
    :maxdepth: 1

    models

