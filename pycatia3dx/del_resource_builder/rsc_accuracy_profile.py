"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.del_resource_builder.enums import AccuracyType


class RscAccuracyProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscAccuracyProfile
                | 
                | Interface to manage Generic Accuracy Profile of Robot
                | controller.
                | Role: This interface provides methods to get/set data related to Accuracy
                | Profile.
                | 
                | Example:
                | 
                |      This example code shows how to retrieve the Accuracy profile
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
                |      (RscAccuracyProfile)
                |       Dim oInputObjectType(0)
                |       oInputObjectType(0) = "RscAccuracyProfile"
                | 
                |      'Application prompts for user selection from CATIA spec
                |      tree
                |       Dim strStatus As String
                |       strStatus = oObjSelection.SelectElement(oInputObjectType, "Select Accuracy Profile from spec tree", False)
                |         
                |      '2.2- Retrieve accuracy profile
                |       Dim oSelectedElement As SelectedElement
                |       Set oSelectedElement = oObjSelection.Item(1)
                |      
                |       Dim oRscAccuracyProfile As RscAccuracyProfile
                |       Set oRscAccuracyProfile = oSelectedElement.Value
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def accuracy_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccuracyType() As AccuracyType
                |     Retrieves/Sets the accuracy type of the profile. Accuracy type could be
                |     ACCURACY_TYPE_DISTANCE / ACCURACY_TYPE_SPEED.
                | 
                |     Example:
                | 
                |      'Display AccuracyType
                |      If (ACCURACY_TYPE_DISTANCE = oRscAccuracyProfile.AccuracyType) Then
                |         MsgBox "Accuracy type =  ACCURACY_TYPE_DISTANCE"
                |      Else
                |         MsgBox "Accuracy type =  ACCURACY_TYPE_SPEED"
                |      End If 
                | 
                |      'Set AccuracyType to ACCURACY_TYPE_SPEED
                |      oRscAccuracyProfile.AccuracyType = ACCURACY_TYPE_SPEED

        :return: AccuracyType
        """

        return self.com_object.AccuracyType

    @accuracy_type.setter
    def accuracy_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.AccuracyType = value

    @property
    def accuracy_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccuracyValue() As double
                |     Retrieves/Sets the accuracy value of the profile.
                | 
                |     Example:
                | 
                |      'Display AccuracyValue
                |      MsgBox "Accuracy Value is" & oRscAccuracyProfile.AccuracyValue
                |      
                | 
                |      'Set AccuracyValue to 0.9
                |      oRscAccuracyProfile.AccuracyValue = 0.9

        :return: float
        """

        return self.com_object.AccuracyValue

    @accuracy_value.setter
    def accuracy_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.AccuracyValue = value

    @property
    def fly_by_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlyByMode() As short
                |     Retrieves/Sets On/Off status of Flyby mode.
                | 
                |     Example:
                | 
                |      'Display FlyByMode
                |      If (0 = oRscAccuracyProfile.FlyByMode) Then
                |         MsgBox "FlyByMode =  OFF"
                |      Else
                |         MsgBox "FlyByMode =  ON"
                |      End If 
                | 
                |      'Set FlyByMode to OFF
                |      oRscAccuracyProfile.FlyByMode = 0

        :return: int
        """

        return self.com_object.FlyByMode

    @fly_by_mode.setter
    def fly_by_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.FlyByMode = value

    def __repr__(self):
        return f'RscAccuracyProfile(name="{ self.name }")'
