"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmPath(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmPath
                | 
                | Interface representing a Path.
                | 
                | Role: This interface is used to get and set attributes specific to a path and
                | its parameters
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def append(self, i_mpoint: tuple, i_vone: tuple, i_vtwo: tuple, i_vthree: tuple, posp_tag: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Append(CATSafeArrayVariant iMpoint,CATSafeArrayVariant
                | iVone,CATSafeArrayVariant iVtwo,CATSafeArrayVariant iVthree,AnyObject
                | pospTag)
                |     Appends a position to the end of the path.
                | 
                |     Parameters:
                | 
                |         iMpoint
                |             The MathPoint which consists of three coordinates.
                |             
                |         iVone
                |             The first vector which consists of three coordinates.
                |             
                |         iVtwo
                |             The second vector which consists of three coordinates
                |             
                |         iVthree
                |             The third vector which consists of three coordinates.
                |             
                |         pospTag
                |             The tag added. 
                | 
                |     Returns:
                |         The added tag

        :param tuple i_mpoint:
        :param tuple i_vone:
        :param tuple i_vtwo:
        :param tuple i_vthree:
        :param AnyObject posp_tag:
        :return: None
        """
        return self.com_object.Append(i_mpoint, i_vone, i_vtwo, i_vthree, posp_tag.com_object)

    def get_absolute_index_of_tag(self, i_relative_index: int, o_absolute_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetAbsoluteIndexOfTag(short iRelativeIndex,short
                | oAbsoluteIndex)
                |     Retrieves the index within this trajectory of a given path
                |     tag.
                | 
                |     Parameters:
                | 
                |         iRelativeIndex
                |             The local tag index to calculate the absolute index of.
                |             
                |         oIndex
                |             The index of the tag within this trajectory. The index of the first
                |             tag is 1.

        :param int i_relative_index:
        :param int o_absolute_index:
        :return: None
        """
        return self.com_object.GetAbsoluteIndexOfTag(i_relative_index, o_absolute_index)

    def get_index_of_tag(self, isp_tag: AnyObject, o_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetIndexOfTag(AnyObject ispTag,short oIndex)
                |     Retrieves the index within this path of a given tag.
                | 
                |     Parameters:
                | 
                |         ispTag
                |             The tag to calculate the index of. 
                |         oIndex
                |             The index of the tag within this path. The index of the first tag
                |             is 1.

        :param AnyObject isp_tag:
        :param int o_index:
        :return: None
        """
        return self.com_object.GetIndexOfTag(isp_tag.com_object, o_index)

    def get_position(self, i_index: int, o_mpoint: tuple, o_vone: tuple, o_vtwo: tuple, o_vthree: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPosition(short iIndex,CATSafeArrayVariant oMpoint,CATSafeArrayVariant
                | oVone,CATSafeArrayVariant oVtwo,CATSafeArrayVariant oVthree)
                |     Get the specified position relative to the aggregating product (eg. the
                |     station).
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the position to retrieve. The index of the first
                |             position is 1. 
                |         oMpoint
                |             The MathPoint which consists of three coordinates.
                |             
                |         oVone
                |             The first vector which consists of three coordinates.
                |             
                |         oVtwo
                |             The second vector which consists of three coordinates.
                |             
                |         oVthree
                |             The third vector which consists of three coordinates.
                |             
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The position was returned correctly.
                |         E_INVALIDARG
                |             The index was invalid.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param int i_index:
        :param tuple o_mpoint:
        :param tuple o_vone:
        :param tuple o_vtwo:
        :param tuple o_vthree:
        :return: None
        """
        return self.com_object.GetPosition(i_index, o_mpoint, o_vone, o_vtwo, o_vthree)

    def get_tag(self, i_index: int, osp_tag: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetTag(short iIndex,AnyObject ospTag)
                |     Retrieves the tag at a given index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the tag within this path. The index of the first tag
                |             is 1. 
                |         ospTag
                |             The tag.

        :param int i_index:
        :param AnyObject osp_tag:
        :return: None
        """
        return self.com_object.GetTag(i_index, osp_tag.com_object)

    def insert(self, i_index: int, i_mpoint: tuple, i_vone: tuple, i_vtwo: tuple, i_vthree: tuple, posp_tag: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Insert(short iIndex,CATSafeArrayVariant iMpoint,CATSafeArrayVariant
                | iVone,CATSafeArrayVariant iVtwo,CATSafeArrayVariant iVthree,AnyObject
                | pospTag)
                |     Inserts a position in the middle of the path
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the position to insert. The index of the first
                |             position is 1. 
                |         iMpoint
                |             The MathPoint which consists of three coordinates.
                |             
                |         iVone
                |             The first vector which consists of three coordinates.
                |             
                |         iVtwo
                |             The second vector which consists of three coordinates
                |             
                |         iVthree
                |             The third vector which consists of three coordinates.
                |             
                |         pospTag
                |             The tag added. 
                | 
                |     Returns:
                |         The added tag

        :param int i_index:
        :param tuple i_mpoint:
        :param tuple i_vone:
        :param tuple i_vtwo:
        :param tuple i_vthree:
        :param AnyObject posp_tag:
        :return: None
        """
        return self.com_object.Insert(i_index, i_mpoint, i_vone, i_vtwo, i_vthree, posp_tag.com_object)

    def num_positions(self, o_size: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub NumPositions(short oSize)
                |     Get the number of positions in the path.
                | 
                |     Parameters:
                | 
                |         oSize
                |             The number of positions. 
                | 
                |     Returns:
                |         The number of positions

        :param int o_size:
        :return: None
        """
        return self.com_object.NumPositions(o_size)

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Remove(short iIndex)
                |     Removes a position from the path.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the position to remove. The index of the first
                |             position is 1.

        :param int i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub RemoveAll()
                |     Removes all positions from the path.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The position was set correctly.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :return: None
        """
        return self.com_object.RemoveAll()

    def set_position(self, i_index: int, i_mpoint: tuple, i_vone: tuple, i_vtwo: tuple, i_vthree: tuple, posp_tag: AnyObject, i_save_data: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetPosition(short iIndex,CATSafeArrayVariant iMpoint,CATSafeArrayVariant
                | iVone,CATSafeArrayVariant iVtwo,CATSafeArrayVariant iVthree,AnyObject
                | pospTag,boolean iSaveData)
                |     Set the specified position relative to the aggregating product (eg. the
                |     station).
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the position to set. The index of the first position
                |             is 1. 
                |         oMpoint
                |             The MathPoint which consists of three coordinates.
                |             
                |         oVone
                |             The first vector which consists of three coordinates.
                |             
                |         oVtwo
                |             The second vector which consists of three coordinates.
                |             
                |         oVthree
                |             The third vector which consists of three coordinates.
                |             
                |         pospTag
                |             the tag at iIndex. 
                |         iSaveData
                |             Directs tag group to update persistent model. 

        :param int i_index:
        :param tuple i_mpoint:
        :param tuple i_vone:
        :param tuple i_vtwo:
        :param tuple i_vthree:
        :param AnyObject posp_tag:
        :param bool i_save_data:
        :return: None
        """
        return self.com_object.SetPosition(i_index, i_mpoint, i_vone, i_vtwo, i_vthree, posp_tag.com_object, i_save_data)

    def __repr__(self):
        return f'CtmPath(name="{ self.name }")'
