"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmPathMgt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmPathMgt
                | 
                | Interface representing a Path.
                | 
                | Role: This interface is used to manipulate paths in a certain
                | trajectory.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_next_index_for_append(self, o_next_tag_absolute_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNextIndexForAppend(short oNextTagAbsoluteIndex)
                |     Retrieves the index of the tag which would be inserted immediately after
                |     the current last tag in this path. If there are no tags in this path, the index
                |     is returned for the first previous path which has a tag in it. If no prior
                |     paths have tags, 1 is returned. The index is abolute in the whole
                |     trajectory.
                | 
                |     Parameters:
                | 
                |         oNextTagAbsoluteIndex
                |             The index for the next tag. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The index was calculated successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param int o_next_tag_absolute_index:
        :return: None
        """
        return self.com_object.GetNextIndexForAppend(o_next_tag_absolute_index)

    def get_trajectory(self, osp_trajectory: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTrajectory(AnyObject ospTrajectory)
                |     Get the parent contour trajectory of this path.
                | 
                |     Parameters:
                | 
                |         ospTrajectory
                |             The parent trajectory 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The output was set successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param AnyObject osp_trajectory:
        :return: None
        """
        return self.com_object.GetTrajectory(osp_trajectory.com_object)

    def move_tags(self, i_new_first_index: int, o_next_availabled_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveTags(short iNewFirstIndex,short oNextAvailabledIndex)
                |     Move the tags for this path to a different spot in the
                |     trajectory.
                | 
                |     Parameters:
                | 
                |         iNewFirstIndex
                |             The index in which to put the first tag of this path.
                |             
                |         oNextAvailabledIndex
                |             The index where the first tag of the next path should be put (one
                |             past the end of this path). 
                | 
                |     Returns:
                |         The next available index

        :param int i_new_first_index:
        :param int o_next_availabled_index:
        :return: None
        """
        return self.com_object.MoveTags(i_new_first_index, o_next_availabled_index)

    def number_tags(self, i_new_first_index: float, i_prefix: str, o_next_available_tag_name_index: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub NumberTags(double iNewFirstIndex,CATBSTR iPrefix,double
                | oNextAvailableTagNameIndex)
                |     Renames the tags in this path. The tags are named [Prefix][NameIndex]. For
                |     example if iPrefix="Weld", iNewFirstIndex=4, and there are 3 tags then the tags
                |     are named "Weld4", "Weld5", "Weld6" and oNextAvailableTagNameIndex is set to
                |     7.
                | 
                |     Parameters:
                | 
                |         iNewFirstIndex
                |             The index to append to the prefix for the first tag. This is
                |             incremented by one for each tag in the path. 
                |         iPrefix
                |             The prefix to use for each tag in this path. 
                |         oNextAvailabledIndex
                |             The index to use for the first tag of the next path.
                |             
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The tags were named successfully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param float i_new_first_index:
        :param str i_prefix:
        :param float o_next_available_tag_name_index:
        :return: None
        """
        return self.com_object.NumberTags(i_new_first_index, i_prefix, o_next_available_tag_name_index)

    def __repr__(self):
        return f'CtmPathMgt(name="{ self.name }")'
