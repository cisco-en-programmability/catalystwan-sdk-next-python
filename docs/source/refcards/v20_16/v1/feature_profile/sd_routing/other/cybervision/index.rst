===============================================
v1.feature_profile.sd_routing.other.cybervision
===============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision
--------------------------------------------------------------------------------------


Create a Cybervision Profile feature for Other feature profile

.. code:: python

    def post(
        other_id: str,
        payload: CreateCybervisionProfileFeatureForOtherPostRequest,
    ) -> CreateCybervisionProfileFeatureForOtherPostResponse: ...


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
        client.v1.feature_profile.sd_routing.other.cybervision.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}
-----------------------------------------------------------------------------------------------------


Update a Cybervision Profile feature for Other feature profile

.. code:: python

    def put(
        other_id: str,
        cybervision_id: str,
        payload: EditCybervisionProfileFeatureForOtherPutRequest,
    ) -> EditCybervisionProfileFeatureForOtherPutResponse: ...


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
        client.v1.feature_profile.sd_routing.other.cybervision.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}
--------------------------------------------------------------------------------------------------------


Delete a Cybervision Profile feature for Other feature profile

.. code:: python

    def delete(other_id: str, cybervision_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.other.cybervision.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(other_id: str) -> GetListSdRoutingOtherCybervisionPayload: ...


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
        client.v1.feature_profile.sd_routing.other.cybervision.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/other/{otherId}/cybervision/{cybervisionId}
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        other_id: str, cybervision_id: str
    ) -> GetSingleSdRoutingOtherCybervisionPayload: ...


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
        client.v1.feature_profile.sd_routing.other.cybervision.get()


.. toctree::
    :maxdepth: 1

    models

