===========================================
v1.feature_profile.mobility.global_.logging
===========================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/logging
----------------------------------------------------------------------------------


Get Logging Profile Features for Mobility Global Feature Profile

.. code:: python

    def get_logging_profile_feature_for_mobility(
        profile_id: str,
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
        client.v1.feature_profile.mobility.global_.logging.get_logging_profile_feature_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/logging
-----------------------------------------------------------------------------------


Create a Logging Profile Feature for Mobility Global Feature Profile

.. code:: python

    def create_logging_profile_feature_for_mobility(
        profile_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.logging.create_logging_profile_feature_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


Get Logging Profile Feature by parcelId for Mobility Global Feature Profile

.. code:: python

    def get_logging_profile_feature_by_feature_id_for_mobility(
        profile_id: str, logging_id: str
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
        client.v1.feature_profile.mobility.global_.logging.get_logging_profile_feature_by_feature_id_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


Update a Logging Profile Feature for Mobility Global Feature Profile

.. code:: python

    def edit_logging_profile_feature_for_mobility(
        profile_id: str, logging_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.mobility.global_.logging.edit_logging_profile_feature_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/logging/{loggingId}
-------------------------------------------------------------------------------------------------


Delete a Logging Profile Feature for Mobility Global Feature Profile

.. code:: python

    def delete_logging_profile_feature_for_mobility(
        profile_id: str, logging_id: str
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
        client.v1.feature_profile.mobility.global_.logging.delete_logging_profile_feature_for_mobility()


