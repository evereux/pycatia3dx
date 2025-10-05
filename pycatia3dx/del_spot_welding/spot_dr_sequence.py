"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrSequence(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrSequence

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_drill_rivet_profile(self, i_pos_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDrillRivetProfile(short iPosIndex) As AnyObject
                |     Get the assigned Drill-Rivet Profile for the specified
                |     index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oDRProfile
                |             Assigned Drill-Rivet Profile 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetDrillRivetProfile(i_pos_index))

    def get_manufacturing_fastener(self, i_pos_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingFastener(short iPosIndex) As AnyObject
                |     Get the Fastener associated to the specified index.
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         opFastener
                |             Manufacturing Fastener. 
                | 
                |     Returns:
                |         S_OK = Successfully get the handle to Manufacturing Fastener. E_FAIL = Failed to get the associated Manufacturing Fastener.

        :param int i_pos_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetManufacturingFastener(i_pos_index))

    def get_manufacturing_pattern(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingPattern() As AnyObject
                |     Get the Pattern associated to the Sequence
                | 
                |     Parameters:
                | 
                |         opPattern
                |             Manufacturing Pattern. 
                | 
                |     Returns:
                |         S_OK = Successfully get the handle to Manufacturing Pattern. E_FAIL = Failed to get the associated Manufacturing Pattern.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetManufacturingPattern())

    def get_object_profile(self, i_pos_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetObjectProfile(short iPosIndex) As AnyObject
                |     Get the assigned Object Frame Profile for the specified
                |     index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oObjectProfile
                |             Assigned Object Frame Profile 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetObjectProfile(i_pos_index))

    def get_position_coordinates(self, i_pos_index: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPositionCoordinates(short iPosIndex) As
                | CATSafeArrayVariant
                |     Gets the position coordinates(like X, Y, Z, Y, P, R) for the specified
                |     index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oFastenerPosCoords
                |             The X, Y, Z, Y, P, R values of pattern position The position are of
                |             double type. The values get via CATSafeArrayVariant for oFastenerPosCoords is
                |             array of double pointers, having 6 position values.
                |             
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: tuple
        """
        return self.com_object.GetPositionCoordinates(i_pos_index)

    def get_tool_profile(self, i_pos_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetToolProfile(short iPosIndex) As AnyObject
                |     Get the assigned Tool Profile for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         oToolProfile
                |             Assigned ToolProfile 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetToolProfile(i_pos_index))

    def set_drill_rivet_profile(self, i_pos_index: int, i_dr_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDrillRivetProfile(short iPosIndex,AnyObject iDRProfile)
                |     Get the assigned Drill-Rivet Profile for the specified
                |     index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iDRProfile
                |             Drill-Rivet Profile to Assign. 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param AnyObject i_dr_profile:
        :return: None
        """
        return self.com_object.SetDrillRivetProfile(i_pos_index, i_dr_profile.com_object)

    def set_object_profile(self, i_pos_index: int, i_object_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetObjectProfile(short iPosIndex,AnyObject iObjectProfile)
                |     Set the Object Frame Profile for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iObjectProfile
                |             Object Frame Profile to Assign 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param AnyObject i_object_profile:
        :return: None
        """
        return self.com_object.SetObjectProfile(i_pos_index, i_object_profile.com_object)

    def set_position_coordinates(self, i_pos_index: int, i_fastener_pos_coords: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPositionCoordinates(short iPosIndex,CATSafeArrayVariant
                | iFastenerPosCoords)
                |     Sets the position coordinates(like X, Y, Z, Y, P, R) for the specified
                |     index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iFastenerPosCoords
                |             The X, Y, Z, Y, P, R values of pattern position The position are of
                |             double type. The values get via CATSafeArrayVariant for oFastenerPosCoords is
                |             array of double pointers, having 6 position values.
                |             
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :param int i_pos_index:
        :param tuple i_fastener_pos_coords:
        :return: None
        """
        return self.com_object.SetPositionCoordinates(i_pos_index, i_fastener_pos_coords)

    def set_tool_profile(self, i_pos_index: int, i_tool_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetToolProfile(short iPosIndex,AnyObject iToolProfile)
                |     Set the Tool Profile for the specified index
                | 
                |     Parameters:
                | 
                |         iPosIndex
                |             The position Index 
                |         iToolProfile
                |             Tool Profile to Assign 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error 

        :param int i_pos_index:
        :param AnyObject i_tool_profile:
        :return: None
        """
        return self.com_object.SetToolProfile(i_pos_index, i_tool_profile.com_object)

    def __repr__(self):
        return f'SpotDrSequence(name="{ self.name }")'
