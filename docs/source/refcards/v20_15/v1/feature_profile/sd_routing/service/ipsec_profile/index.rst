===================================================
v1.feature_profile.sd_routing.service.ipsec_profile
===================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile
--------------------------------------------------------------------------------------------


Create a SD-Routing IPSec Profile Feature for Service Feature Profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceIpsecProfileFeaturePostRequest,
    ) -> CreateSdroutingServiceIpsecProfileFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile/{ipsecProfileId}
------------------------------------------------------------------------------------------------------------


Edit a SD-Routing IPSec Profile Feature for Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        ipsec_profile_id: str,
        payload: EditSdroutingServiceIpsecProfileFeaturePutRequest,
    ) -> EditSdroutingServiceIpsecProfileFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile/{ipsecProfileId}
---------------------------------------------------------------------------------------------------------------


Delete a SD-Routing IPSec Profile Feature for Service Feature Profile

.. code:: python

    def delete(service_id: str, ipsec_profile_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile
-------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceIpsecProfilePayload: ...


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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipsec-profile/{ipsecProfileId}
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, ipsec_profile_id: str
    ) -> GetSingleSdRoutingServiceIpsecProfilePayload: ...


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
        client.v1.feature_profile.sd_routing.service.ipsec_profile.get()


.. toctree::
    :maxdepth: 1

    models

