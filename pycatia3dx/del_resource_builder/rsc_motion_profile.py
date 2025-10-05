"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscMotionProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscMotionProfile
                | 
                | Interface to manage Generic Motion Profile of Robot
                | controller.
                | Role: This interface provides methods to get/set data related to Motion
                | Profile.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve the Motion profile
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
                |      (RscMotionProfile)
                |       Dim oInputObjectType(0)
                |       oInputObjectType(0) = "RscMotionProfile"
                | 
                |      'Application prompts for user selection from CATIA spec
                |      tree
                |       Dim strStatus As String
                |       strStatus = oObjSelection.SelectElement(oInputObjectType, "Select Motion Profile from spec tree", False)
                |         
                |      '2.2- Retrieve motion profile
                |       Dim oSelectedElement As SelectedElement
                |       Set oSelectedElement = oObjSelection.Item(1)
                |      
                |       Dim oRscMotionProfile As RscMotionProfile
                |       Set oRscMotionProfile = oSelectedElement.Value
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def acceleration_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccelerationValue() As double
                |     Retrieves/Sets the Acceleration value of the profile.
                |     The value is based on the motion basis:
                |         MOTION_ABSOLUTE : absolute acceleration value.
                |         MOTION_PERCENT : 0-1, percent of max acceleration of the device
                |         MOTION_TIME : percent of total move time used on acceleration/deceleration
                | 
                |     Example:
                | 
                |      'Display AccelerationValue
                |      MsgBox "Acceleration Value is" &
                |      oRscMotionProfile.AccelerationValue
                | 
                |      'Set AccelerationValue to 11
                |      oRscMotionProfile.AccelerationValue = 11

        :return: float
        """

        return self.com_object.AccelerationValue

    @acceleration_value.setter
    def acceleration_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.AccelerationValue = value

    @property
    def angular_acceleration_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngularAccelerationValue() As double
                |     Retrieves/Sets the Angular Acceleration value of the
                |     profile.
                | 
                |     Example:
                | 
                |      'Display Angular Acceleration Value
                |      MsgBox "Angular Acceleration Value is" &
                |      oRscMotionProfile.AngularAccelerationValue 
                | 
                |      'Set Angular Acceleration Value to 5
                |      oRscMotionProfile.AngularAccelerationValue = 5

        :return: float
        """

        return self.com_object.AngularAccelerationValue

    @angular_acceleration_value.setter
    def angular_acceleration_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngularAccelerationValue = value

    @property
    def angular_speed_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngularSpeedValue() As double
                |     Retrieves/Sets the Angular Speed value of the profile.
                | 
                |     Example:
                | 
                |      'Display AngularSpeedValue
                |      MsgBox "Angular Speed Value is" & oRscMotionProfile.AngularSpeedValue
                |      
                | 
                |      'Set AngularSpeedValue to 9
                |      oRscMotionProfile.AngularSpeedValue = 9

        :return: float
        """

        return self.com_object.AngularSpeedValue

    @angular_speed_value.setter
    def angular_speed_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngularSpeedValue = value

    @property
    def motion_basis(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionBasis() As MotionBasis
                |     Retrieves/Sets the Motion basis of the profile. Motion basis could be
                |     MOTION_ABSOLUTE, MOTION_PERCENT, MOTION_TIME
                | 
                |     Example:
                | 
                |      'Display Motion Basis
                |      If (MOTION_ABSOLUTE = oRscMotionProfile.MotionBasis) Then
                |         MsgBox "MotionBasis =  MOTION_ABSOLUTE"
                |      Else
                |         MsgBox "MotionBasis !=  MOTION_ABSOLUTE"
                |      End If 
                | 
                |      'Set Motion Basis to MOTION_PERCENT
                |      oRscMotionProfile.MotionBasis = MOTION_PERCENT

        :return: MotionBasis
        """

        return self.com_object.MotionBasis

    @motion_basis.setter
    def motion_basis(self, value: int):
        """
        :param int value:
        """

        self.com_object.MotionBasis = value

    @property
    def speed_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpeedValue() As double
                |     Retrieves/Sets the Speed value of the profile.
                |     The value is based on the motion basis:
                |         MOTION_ABSOLUTE : absolute speed value.
                |         MOTION_PERCENT : 0-1, percent of max speed of the device
                |         MOTION_TIME : in seconds
                | 
                |     Example:
                | 
                |      'Display SpeedValue
                |      MsgBox "Speed Value is" & oRscMotionProfile.SpeedValue 
                | 
                |      'Set SpeedValue to 99
                |      oRscMotionProfile.SpeedValue = 99

        :return: float
        """

        return self.com_object.SpeedValue

    @speed_value.setter
    def speed_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.SpeedValue = value

    def __repr__(self):
        return f'RscMotionProfile(name="{ self.name }")'
