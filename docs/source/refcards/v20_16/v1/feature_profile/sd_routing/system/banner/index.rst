===========================================
v1.feature_profile.sd_routing.system.banner
===========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner
-----------------------------------------------------------------------------------


Create a SD-Routing banner feature from a specific system feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateSdroutingBannerFeaturePostRequest
    ) -> CreateSdroutingBannerFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.banner.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}
---------------------------------------------------------------------------------------------


Edit the SD-Routing banner feature from a specific system feature profile

.. code:: python

    def put(
        system_id: str,
        banner_id: str,
        payload: EditSdroutingBannerFeaturePutRequest,
    ) -> EditSdroutingBannerFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.banner.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}
------------------------------------------------------------------------------------------------


Delete the SD-Routing banner feature from a specific system feature profile

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
        client.v1.feature_profile.sd_routing.system.banner.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdRoutingSystemBannerPayload: ...


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
        client.v1.feature_profile.sd_routing.system.banner.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, banner_id: str
    ) -> GetSingleSdRoutingSystemBannerPayload: ...


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
        client.v1.feature_profile.sd_routing.system.banner.get()


.. toctree::
    :maxdepth: 1

    models

