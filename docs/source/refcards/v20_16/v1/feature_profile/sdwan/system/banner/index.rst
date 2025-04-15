======================================
v1.feature_profile.sdwan.system.banner
======================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner
------------------------------------------------------------------------------


Create a Banner Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateBannerProfileParcelForSystemPostRequest,
    ) -> CreateBannerProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.banner.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId}
----------------------------------------------------------------------------------------


Update a Banner Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        banner_id: str,
        payload: EditBannerProfileParcelForSystemPutRequest,
    ) -> EditBannerProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.banner.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId}
-------------------------------------------------------------------------------------------


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
        client.v1.feature_profile.sdwan.system.banner.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner
-----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemBannerPayload: ...


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
        client.v1.feature_profile.sdwan.system.banner.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId}
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, banner_id: str
    ) -> GetSingleSdwanSystemBannerPayload: ...


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
        client.v1.feature_profile.sdwan.system.banner.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

