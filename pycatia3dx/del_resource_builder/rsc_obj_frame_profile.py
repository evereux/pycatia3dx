"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscObjFrameProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscObjFrameProfile
                | 
                | Interface to manage Generic ObjFrame Profile of Robot
                | controller.
                | Role: This interface provides methods to get/set data related to ObjFrame
                | Profile.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve the Obj Frame profile
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
                |      (RscObjFrameProfile)
                |       Dim oInputObjectType(0)
                |       oInputObjectType(0) = "RscObjFrameProfile"
                | 
                |      'Application prompts for user selection from CATIA spec
                |      tree
                |       Dim strStatus As String
                |       strStatus = oObjSelection.SelectElement(oInputObjectType, "Select Obj Frame Profile from spec tree", False)
                |         
                |      '2.2- Retrieve obj frame profile
                |       Dim oSelectedElement As SelectedElement
                |       Set oSelectedElement = oObjSelection.Item(1)
                |      
                |       Dim oRscObjFrameProfile As RscObjFrameProfile
                |       Set oRscObjFrameProfile = oSelectedElement.Value
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def offset_target_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OffsetTargetMode() As short
                |     Retrieves/Sets offset mode of the Object Frame. If Offset mode is TRUE
                |     offset will be applied to all Targets defined in the Cartesian Space that is
                |     Tag/Weld, Else If Offset mode is FALSE then the offset will be applied to the
                |     "Cartesian Targets" only.
                | 
                |     Example:
                | 
                |      'Display OffsetTargetMode
                |      If (0 = oRscObjFrameProfile.OffsetTargetMode) Then
                |         MsgBox "OffsetTargetMode =  OFF"
                |      Else
                |         MsgBox "OffsetTargetMode =  ON"
                |      End If 
                | 
                |      'Set OffsetTargetMode to OFF
                |      oRscObjFrameProfile.OffsetTargetMode = 0

        :return: int
        """

        return self.com_object.OffsetTargetMode

    @offset_target_mode.setter
    def offset_target_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.OffsetTargetMode = value

    def get_object_frame(self, o_x: float, o_y: float, o_z: float, o_roll: float, o_pitch: float, o_yaw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetObjectFrame(double oX,double oY,double oZ,double oRoll,double
                | oPitch,double oYaw)
                |     Retrieves the underlying x, y, z, roll, pitch, yaw of the Object
                |     Frame
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
                |          oRscObjFrameProfile.GetObjectFrame
                |          oX,oY,oZ,oRoll,oPitch,oYaw

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :param float o_roll:
        :param float o_pitch:
        :param float o_yaw:
        :return: None
        """
        return self.com_object.GetObjectFrame(o_x, o_y, o_z, o_roll, o_pitch, o_yaw)

    def set_object_frame(self, i_x: float, i_y: float, i_z: float, i_roll: float, i_pitch: float, i_yaw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetObjectFrame(double iX,double iY,double iZ,double iRoll,double
                | iPitch,double iYaw)
                |     Sets the underlying x, y, z, roll, pitch, yaw of the Object
                |     Frame
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
                |          oRscObjFrameProfile.SetObjectFrame 100,100,100,0,0,0

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param float i_roll:
        :param float i_pitch:
        :param float i_yaw:
        :return: None
        """
        return self.com_object.SetObjectFrame(i_x, i_y, i_z, i_roll, i_pitch, i_yaw)

    def __repr__(self):
        return f'RscObjFrameProfile(name="{ self.name }")'
