"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingMacroMotion(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMacroMotion
                | 
                | Interface to manage the motions of macros.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def delete_elementary_motion(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteElementaryMotion(long iPosition)
                |     Deletes an elementary motion in the macro motion.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the motion to delete in the sequence

        :param int i_position:
        :return: None
        """
        return self.com_object.DeleteElementaryMotion(i_position)

    def get_elementary_motion(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetElementaryMotion(long iPosition) As AnyObject
                |     Access to an elementary macro motion.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the motion to access. 
                | 
                |     Returns:
                |         The corresponding motion found.

        :param int i_position:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetElementaryMotion(i_position))

    def get_number_of_elementary_motions(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfElementaryMotions() As long
                |     Returns the number of elementary macro motions.
                | 
                |     Returns:
                |         The number of elementary macro motions.

        :return: int
        """
        return self.com_object.GetNumberOfElementaryMotions()

    def insert_elementary_motion(self, i_position: int, i_motion_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func InsertElementaryMotion(long iPosition,CATBSTR iMotionType) As
                | AnyObject
                |     Inserts an elementary motion in the macro motion.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position in the sequence. 
                |         iMotionType
                |             The type of motion to add. Authorized values are :
                | 
                |                 MfgMacroClearanceMotion
                |                 MfgMacroElementaryAxialMotion
                |                 MfgMacroElementaryHorizontalMotion
                |                 MfgMacroElementaryCircularMotion
                |                 MfgMacroPPWord
                |                 MfgMacroElementaryRampingMotion
                |                 MfgMacroElementaryGoToAPlaneMotion
                |                 MfgMacroElementaryGoToAPointMotion
                |                 MfgMacroElementaryDeltaLnDistMotion
                |                 MfgMacroElementaryToolAxisMotion
                |                 MfgMacroElementaryHelixMotion
                |                 MfgMacroElementaryGoToALineMotion
                |                 MfgMacroElementarySimultaneousAxisMotion
                | 
                |     Returns:
                |         The new motion.

        :param int i_position:
        :param str i_motion_type:
        :return: AnyObject
        """
        return AnyObject(self.com_object.InsertElementaryMotion(i_position, i_motion_type))

    def __repr__(self):
        return f'ManufacturingMacroMotion(name="{ self.name }")'
