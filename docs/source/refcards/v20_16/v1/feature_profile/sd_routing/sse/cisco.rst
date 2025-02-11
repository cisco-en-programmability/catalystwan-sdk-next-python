=======================================
v1.feature_profile.sd_routing.sse.cisco
=======================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco
---------------------------------------------------------------------------


Get Cisco Sse feature list for Sse feature profile

.. code:: python

    def get_cisco_sse_feature_for_sse(sse_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.sse.cisco.get_cisco_sse_feature_for_sse()


Operation: POST /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco
----------------------------------------------------------------------------


Create Cisco Sse feature for sse feature profile type

.. code:: python

    def create_cisco_sse_feature_for_sse(
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
        client.v1.feature_profile.sd_routing.sse.cisco.create_cisco_sse_feature_for_sse()


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}
----------------------------------------------------------------------------------------


Get Cisco SSE Profile Feature by feature Id

.. code:: python

    def get_cisco_sse_feature_by_feature_id_for_sse(
        sse_id: str, cisco_sse_id: str
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
        client.v1.feature_profile.sd_routing.sse.cisco.get_cisco_sse_feature_by_feature_id_for_sse()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}
----------------------------------------------------------------------------------------


Update a Cisco Sse feature

.. code:: python

    def edit_cisco_sse_feature(
        sse_id: str, cisco_sse_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.sse.cisco.edit_cisco_sse_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}
-------------------------------------------------------------------------------------------


Delete a Cisco Sse Feature

.. code:: python

    def delete_cisco_sse_feature(
        sse_id: str, cisco_sse_id: str
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
        client.v1.feature_profile.sd_routing.sse.cisco.delete_cisco_sse_feature()


