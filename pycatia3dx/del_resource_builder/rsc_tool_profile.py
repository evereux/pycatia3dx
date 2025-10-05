"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscToolProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscToolProfile
                | 
                | Interface to manage Generic Tool Profile of Robot controller.
                | Role: This interface provides methods to get/set data related to Tool
                | Profile.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve the tool profile
                |      interface.
                |      
                | 
                |      '1- Retrieve Selection object from active editor
                |       Dim oCurrentActiveEditor As Editor
                |       Set oCurrentActiveEditor = CATIA.ActiveEditor
                |       Dim oObjSelection
                |       Set oObjSelection = oCurrentActiveEditor.Selection
                | 
                |      '2.1-Update selection object with the search criteria and prompt for
                |      selection
                |      'Selection Object updated with selection criteria
                |      (RscToolProfile)
                |       Dim oInputObjectType(0)
                |       oInputObjectType(0) = "RscToolProfile"
                | 
                |      'Application prompts for user selection from CATIA spec
                |      tree
                |       Dim strStatus As String
                |       strStatus = oObjSelection.SelectElement(oInputObjectType, "Select tool Profile from spec tree", False)
                |         
                |      '2.2- Retrieve the tool profile
                |       Dim oSelectedElement As SelectedElement
                |       Set oSelectedElement = oObjSelection.Item(1)
                |      
                |       Dim oRscToolProfile As RscToolProfile
                |       Set oRscToolProfile = oSelectedElement.Value
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def mass(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mass() As double
                |     Retrieves/Sets tool mass.
                | 
                |     Example:
                | 
                |      'Display Mass
                |      MsgBox "Mass = " & oRscToolProfile.Mass 
                | 
                |      'Set Mass to 100
                |      oRscToolProfile.Mass = 100

        :return: float
        """

        return self.com_object.Mass

    @mass.setter
    def mass(self, value: float):
        """
        :param float value:
        """

        self.com_object.Mass = value

    @property
    def tool_mobility(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolMobility() As short
                |     Retrieves/Sets tool mobility flag TRUE if the tool is fixed, FALSE if it is
                |     mobile.
                | 
                |     Example:
                | 
                |      'Display ToolMobility flag
                |      If (0 = oRscToolProfile.ToolMobility) Then
                |         MsgBox "ToolMobility flag =  FALSE"
                |      Else
                |         MsgBox "ToolMobility flag =  TRUE"
                |      End If 
                | 
                |      'Set ToolMobility flag to FALSE
                |      oRscToolProfile.ToolMobility = 0

        :return: int
        """

        return self.com_object.ToolMobility

    @tool_mobility.setter
    def tool_mobility(self, value: int):
        """
        :param int value:
        """

        self.com_object.ToolMobility = value

    def get_centroid(self, o_x: float, o_y: float, o_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCentroid(double oX,double oY,double oZ)
                |     Retrieves the tool centroid of Profile
                | 
                |     Parameters:
                | 
                |         oX
                |             The X Coordinate. 
                |         oY
                |             The Y Coordinate. 
                |         oZ
                |             The Z Coordinate. 
                | 
                |     Example:
                | 
                |          Dim oX As double
                |          Dim oY As double
                |          Dim oZ As double
                |          oRscToolProfile.GetCentroid oX,oY,oZ

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :return: None
        """
        return self.com_object.GetCentroid(o_x, o_y, o_z)

    def get_inertia(self, o_xx: float, o_yy: float, o_zz: float, o_xy: float, o_yz: float, o_zx: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetInertia(double oXX,double oYY,double oZZ,double oXY,double oYZ,double
                | oZX)
                |     Retrieves the underlying coefficient of tool inertia
                | 
                |     Parameters:
                | 
                |         oXX
                |             The XX coefficient. 
                |         oYY
                |             The YY coefficient. 
                |         oZZ
                |             The ZZ coefficient. 
                |         oXY
                |             The XY coefficient. 
                |         oYZ
                |             The YZ coefficient. 
                |         oZX
                |             The ZX coefficient. 
                | 
                |     Example:
                | 
                |          Dim oXX As double
                |          Dim oYY As double
                |          Dim oZZ As double
                |          Dim oXY As double
                |          Dim oYZ As double
                |          Dim oZX As double
                |          oRscToolProfile.GetInertia oXX,oYY,oZZ,oXY,oYZ,oZX

        :param float o_xx:
        :param float o_yy:
        :param float o_zz:
        :param float o_xy:
        :param float o_yz:
        :param float o_zx:
        :return: None
        """
        return self.com_object.GetInertia(o_xx, o_yy, o_zz, o_xy, o_yz, o_zx)

    def get_tcp_offset(self, o_x: float, o_y: float, o_z: float, o_roll: float, o_pitch: float, o_yaw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPOffset(double oX,double oY,double oZ,double oRoll,double
                | oPitch,double oYaw)
                |     Retrieves the underlying x, y, z, roll, pitch, yaw of the TCP
                |     Offset
                | 
                |     Parameters:
                | 
                |         oX
                |             The X Coordinate. 
                |         oY
                |             The Y Coordinate. 
                |         oZ
                |             The Z Coordinate. 
                |         oRoll
                |             The roll Coordinate. 
                |         oPitch
                |             The pitch Coordinate. 
                |         oYaw
                |             The yaw Coordinate. 
                | 
                |     Example:
                | 
                |          Dim oX As double
                |          Dim oY As double
                |          Dim oZ As double
                |          Dim oRoll As double
                |          Dim oPitch As double
                |          Dim oYaw As double
                |          oRscToolProfile.GetTCPOffset
                |          oX,oY,oZ,oRoll,oPitch,oYaw

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :param float o_roll:
        :param float o_pitch:
        :param float o_yaw:
        :return: None
        """
        return self.com_object.GetTCPOffset(o_x, o_y, o_z, o_roll, o_pitch, o_yaw)

    def set_centroid(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCentroid(double iX,double iY,double iZ)
                |     Sets the tool centroid of Profile
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate. 
                |         iY
                |             The Y Coordinate. 
                |         iZ
                |             The Z Coordinate. 
                | 
                |     Example:
                | 
                |          oRscToolProfile.SetCentroid 100,100,100

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: None
        """
        return self.com_object.SetCentroid(i_x, i_y, i_z)

    def set_inertia(self, i_xx: float, i_yy: float, i_zz: float, i_xy: float, i_yz: float, i_zx: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInertia(double iXX,double iYY,double iZZ,double iXY,double iYZ,double
                | iZX)
                |     Sets the underlying coefficient of tool inertia
                | 
                |     Parameters:
                | 
                |         iXX
                |             The XX coefficient. 
                |         iYY
                |             The YY coefficient. 
                |         iZZ
                |             The ZZ coefficient. 
                |         iXY
                |             The XY coefficient. 
                |         iYZ
                |             The YZ coefficient. 
                |         iZX
                |             The ZX coefficient. 
                | 
                |     Example:
                | 
                |          oRscToolProfile.SetInertia 100,100,100,0,0,0

        :param float i_xx:
        :param float i_yy:
        :param float i_zz:
        :param float i_xy:
        :param float i_yz:
        :param float i_zx:
        :return: None
        """
        return self.com_object.SetInertia(i_xx, i_yy, i_zz, i_xy, i_yz, i_zx)

    def set_tcp_offset(self, i_x: float, i_y: float, i_z: float, i_roll: float, i_pitch: float, i_yaw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPOffset(double iX,double iY,double iZ,double iRoll,double
                | iPitch,double iYaw)
                |     Sets the underlying x, y, z, roll, pitch, yaw of the TCP
                |     offset
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate. 
                |         iY
                |             The Y Coordinate. 
                |         iZ
                |             The Z Coordinate. 
                |         iRoll
                |             The roll Coordinate. 
                |         iPitch
                |             The pitch Coordinate. 
                |         iYaw
                |             The yaw Coordinate 
                | 
                |     Example:
                | 
                |          oRscToolProfile.SetTCPOffset 100,100,100,0,0,0

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param float i_roll:
        :param float i_pitch:
        :param float i_yaw:
        :return: None
        """
        return self.com_object.SetTCPOffset(i_x, i_y, i_z, i_roll, i_pitch, i_yaw)

    def __repr__(self):
        return f'RscToolProfile(name="{ self.name }")'
