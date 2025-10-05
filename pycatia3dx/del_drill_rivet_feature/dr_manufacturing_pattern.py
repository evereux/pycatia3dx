"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrManufacturingPattern(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrManufacturingPattern
                | 
                | Represents an object that is Drilling Riveting Pattern Role: To manage Drill
                | Rivet patterns
                | 
                | See also:
                |     DrManufacturingPattern
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_manufacturing_fastener(self, ih_mfg_fastener: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub AddManufacturingFastener(AnyObject ihMfgFastener)
                |     Add a Manufacturing Fastener.
                | 
                |     Parameters:
                | 
                |         ihMfgFastener
                |             The Manufacturing Fastener to add.

        :param AnyObject ih_mfg_fastener:
        :return: None
        """
        return self.com_object.AddManufacturingFastener(ih_mfg_fastener.com_object)

    def get_manufacturing_fastener_from_index(self, i_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetManufacturingFastenerFromIndex(long iIndex) As
                | AnyObject
                |     Get the Manufacturing Fastener from the index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position index. 
                |         ohMfgFastener
                |             The Manufacturing Fastener.

        :param int i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetManufacturingFastenerFromIndex(i_index))

    def get_manufacturing_fasteners(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetManufacturingFasteners() As CATSafeArrayVariant
                |     Get all the Manufacturing Fasteners that belong to this
                |     pattern.
                | 
                |     Parameters:
                | 
                |         oListMfgFasteners
                |             The list of Manufacturing Fasteners.

        :return: tuple
        """
        return self.com_object.GetManufacturingFasteners()

    def get_ordering_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetOrderingMode() As long
                |     Get the ordering mode of this pattern.
                | 
                |     Parameters:
                | 
                |         oOrderingMode
                |             Ordering mode.

        :return: int
        """
        return self.com_object.GetOrderingMode()

    def move_after(self, i_from_index: int, i_to_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub MoveAfter(long iFromIndex,long iToIndex)
                |     Move the Manufacturing Fastener from one index to another
                |     index
                | 
                |     Parameters:
                | 
                |         iFromIndex
                |             Position index from where the Manufacturing Fastener needs to be
                |             moved. 
                |         iToIndex
                |             Position index to where the Manufacturing Fastener needs to be
                |             moved.

        :param int i_from_index:
        :param int i_to_index:
        :return: None
        """
        return self.com_object.MoveAfter(i_from_index, i_to_index)

    def remove_manufacturing_fastener(self, ih_mfg_fastener: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub RemoveManufacturingFastener(AnyObject ihMfgFastener)
                |     Remove a Manufacturing Fastener.
                | 
                |     Parameters:
                | 
                |         ihMfgFastener
                |             The Manufacturing Fastener to remove.

        :param AnyObject ih_mfg_fastener:
        :return: None
        """
        return self.com_object.RemoveManufacturingFastener(ih_mfg_fastener.com_object)

    def set_ordering_mode(self, i_ordering_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetOrderingMode(long iOrderingMode)
                |     Set the ordering mode for this pattern
                | 
                |     Parameters:
                | 
                |         iOrderingMode
                |             Ordering mode. 

        :param int i_ordering_mode:
        :return: None
        """
        return self.com_object.SetOrderingMode(i_ordering_mode)

    def __repr__(self):
        return f'DrManufacturingPattern(name="{ self.name }")'
