======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Entry:
        """
        list
        """

        user_group: Optional[str]


    class Reference:
        """
        single policy where list is referenced
        """

        id: Optional[str]
        type_: Optional[str]


    class ReferencedList:
        """
        A single list and where it is referenced
        """

        description: Optional[str]
        entries: Optional[List[Entry]]
        info_tag: Optional[str]
        is_activated_by_vsmart: Optional[bool]
        last_updated: Optional[int]
        list_id: Optional[str]
        name: Optional[str]
        owner: Optional[str]
        read_only: Optional[bool]
        reference_count: Optional[int]
        references: Optional[List[Reference]]
        type_: Optional[str]
        version: Optional[str]


