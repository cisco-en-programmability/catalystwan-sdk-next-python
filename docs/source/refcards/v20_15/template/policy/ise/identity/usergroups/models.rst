======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class UsergroupObject:
        name: Optional[str]
        sid: Optional[str]
        type_: Optional[str]


    class ErsActiveDirectoryGroups:
        groups: Optional[List[UsergroupObject]]


    class UserGroupsDataObject:
        """
        Data Object for Users Groups call
        """

        ers_active_directory_groups: Optional[ErsActiveDirectoryGroups]


    class HeaderObject:
        """
        Header for Response
        """

        columns: Optional[Any]
        fields: Optional[Any]
        generated_on: Optional[int]
        view_keys: Optional[Any]


    class UserGroupsResponse:
        """
        User Groups Data from ISE active directory domain
        """

        # Data Object for Users Groups call
        data: Optional[UserGroupsDataObject]
        # Header for Response
        header: Optional[HeaderObject]


    class UserGroupsBody:
        filter: Optional[str]


