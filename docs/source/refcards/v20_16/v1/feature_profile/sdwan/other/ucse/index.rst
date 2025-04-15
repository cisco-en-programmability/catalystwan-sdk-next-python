===================================
v1.feature_profile.sdwan.other.ucse
===================================


Operation: POST /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse
--------------------------------------------------------------------------


Create a Ucse Profile feature for Other feature profile

.. code:: python

    def post(
        other_id: str,
        payload: CreateUcseProfileFeatureForOtherPostRequest,
    ) -> CreateUcseProfileFeatureForOtherPostResponse: ...


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
        client.v1.feature_profile.sdwan.other.ucse.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}
----------------------------------------------------------------------------------


Update a Ucse Profile feature for Other feature profile

.. code:: python

    def put(
        other_id: str,
        ucse_id: str,
        payload: EditUcseProfileFeatureForOtherPutRequest,
    ) -> EditUcseProfileFeatureForOtherPutResponse: ...


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
        client.v1.feature_profile.sdwan.other.ucse.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}
-------------------------------------------------------------------------------------


Delete a Ucse Profile feature for Other feature profile

.. code:: python

    def delete(other_id: str, ucse_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.other.ucse.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse
-------------------------------------------------------------------------


.. code:: python

    @overload
    def get(other_id: str) -> GetListSdwanOtherUcsePayload: ...


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
        client.v1.feature_profile.sdwan.other.ucse.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/ucse/{ucseId}
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        other_id: str, ucse_id: str
    ) -> GetSingleSdwanOtherUcsePayload: ...


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
        client.v1.feature_profile.sdwan.other.ucse.get()


.. toctree::
    :maxdepth: 1

    models

