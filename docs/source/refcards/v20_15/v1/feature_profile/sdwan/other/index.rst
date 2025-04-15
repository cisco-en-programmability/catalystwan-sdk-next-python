==============================
v1.feature_profile.sdwan.other
==============================


Operation: POST /dataservice/v1/feature-profile/sdwan/other
-----------------------------------------------------------


Create a SDWAN Other Feature Profile

.. code:: python

    def post(
        payload: CreateSdwanOtherFeatureProfilePostRequest,
    ) -> CreateSdwanOtherFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.other.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/other/{otherId}
--------------------------------------------------------------------


Edit a SDWAN Other Feature Profile

.. code:: python

    def put(
        other_id: str, payload: EditSdwanOtherFeatureProfilePutRequest
    ) -> EditSdwanOtherFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.other.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/other/{otherId}
-----------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(other_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.other.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/other
----------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdwanOtherFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sdwan.other.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}
--------------------------------------------------------------------


.. code:: python

    @overload
    def get(other_id: str) -> GetSingleSdwanOtherPayload: ...


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
        client.v1.feature_profile.sdwan.other.get()


.. toctree::
    :maxdepth: 1

    thousandeyes/index
    ucse/index
    models

