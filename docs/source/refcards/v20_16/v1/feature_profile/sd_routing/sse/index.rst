=================================
v1.feature_profile.sd_routing.sse
=================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse
-------------------------------------------------------------


Get all SD-ROUTING Feature Profiles with giving Family and profile type

.. code:: python

    def get_sd_routing_sse_feature_profiles(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> Any: ...


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
        client.v1.feature_profile.sd_routing.sse.get_sd_routing_sse_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sd-routing/sse
--------------------------------------------------------------


Create a SD-ROUTING SSE Feature Profile

.. code:: python

    def create_sd_routing_sse_feature_profile(
        payload: Optional[str] = None,
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
        client.v1.feature_profile.sd_routing.sse.create_sd_routing_sse_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse/{sseId}
---------------------------------------------------------------------


Get a SD-ROUTING SSE Feature Profile with sseId

.. code:: python

    def get_sd_routing_sse_feature_profile_by_profile_id(
        sse_id: str, references: Optional[bool] = False
    ) -> Any: ...


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
        client.v1.feature_profile.sd_routing.sse.get_sd_routing_sse_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/sse/{sseId}
---------------------------------------------------------------------


Edit a SD-ROUTING SSE Feature Profile

.. code:: python

    def edit_sd_routing_sse_feature_profile(
        sse_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.sse.edit_sd_routing_sse_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/sse/{sseId}
------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sd_routing_sse_feature_profile(sse_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.sse.delete_sd_routing_sse_feature_profile()


.. toctree::
    :maxdepth: 1

    cisco

