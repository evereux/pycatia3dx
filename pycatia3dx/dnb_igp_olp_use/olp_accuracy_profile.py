"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile


class OLPAccuracyProfile(OLPProfile):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpProfile
                |                         OlpAccuracyProfile
                | 
                | An accuracy profile.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | The behavior of this object depends on where it was retrieved from. If the
                | object was retrieved from an OlpRobotMotion or OlpRobotMotionTarget then this
                | object is used to configure the accuracy properties of that motion. The
                | parameters specified with the iMatch input equal to TRUE will be used to find
                | an existing profile to reuse for this motion. If no matching profile is found a
                | new one will be created. If the object was retrieved from
                | OlpController.AccuracyProfileList then any modifications to this object will
                | change an existing or new profile's values directly.
                | 
                | You cannot call Get methods for profiles retrieved from a new OlpRobotMotion or
                | OlpRobotMotionTarget until values have been set.
    
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
                |      If (ACCURACY_TYPE_DISTANCE =AccuracyProfile.AccuracyType)
                |      Then
                |         MsgBox "Accuracy type =  ACCURACY_TYPE_DISTANCE"
                |      Else
                |         MsgBox "Accuracy type =  ACCURACY_TYPE_SPEED"
                |      End If
                | 
                |      'Set AccuracyType to ACCURACY_TYPE_SPEED
                |      AccuracyProfile.AccuracyType = ACCURACY_TYPE_SPEED

        :return: int
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
                |      MsgBox "Accuracy Value is" &AccuracyProfile.AccuracyValue
                | 
                |      'Set AccuracyValue to 0.9
                |      AccuracyProfile.AccuracyValue = 0.9

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
                |      If (0 =AccuracyProfile.FlyByMode) Then
                |         MsgBox "FlyByMode =  OFF"
                |      Else
                |         MsgBox "FlyByMode =  ON"
                |      End If
                | 
                |      'Set FlyByMode to OFF
                |      AccuracyProfile.FlyByMode = 0

        :return: int
        """

        return self.com_object.FlyByMode

    @fly_by_mode.setter
    def fly_by_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.FlyByMode = value

    def get_accuracy_params(self, o_fly_by: bool, o_accuracy_type: int, o_accuracy_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAccuracyParams(boolean oFlyBy,AccuracyType oAccuracyType,double
                | oAccuracyValue)
                |     Get the accuracy profile parameters.
                | 
                |     Parameters:
                | 
                |         oFlyBy
                |             The flyby mode false for flyby off, true for flyby
                |             on.
                |         oAccuracyType
                |             The accuracy type distance or speed based 
                |         oAccuracyValue
                |             The accuracy value as a distance (m) or percent speed.

        :param bool o_fly_by:
        :param int o_accuracy_type:
        :param float o_accuracy_value:
        :return: None
        """
        return self.com_object.GetAccuracyParams(o_fly_by, o_accuracy_type, o_accuracy_value)

    def set_accuracy_params(self, i_fly_by: bool, i_accuracy_type: int, i_accuracy_value: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyParams(boolean iFlyBy,AccuracyType iAccuracyType,double
                | iAccuracyValue,boolean iMatch)
                |     Set the accuracy profile parameters.
                | 
                |     Parameters:
                | 
                |         iFlyBy
                |             The flyby mode false for flyby off, true for flyby
                |             on.
                |         iAccuracyType
                |             The accuracy type distance or speed based 
                |         iAccuracyValue
                |             The accuracy value as a distance (m) or percent speed.
                |             
                |         iMatch
                |             Should the accuracy settings be used to find a controller profile
                |             match

        :param bool i_fly_by:
        :param int i_accuracy_type:
        :param float i_accuracy_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAccuracyParams(i_fly_by, i_accuracy_type, i_accuracy_value, i_match)

    def set_accuracy_type(self, i_accuracy_type: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyType(AccuracyType iAccuracyType,boolean iMatch)
                |     Set the accuracy profile type.
                | 
                |     Parameters:
                | 
                |         iAccuracyType
                |             The accuracy type distance or speed based 
                |         iMatch
                |             Should the accuracy settings be used to find a controller profile
                |             match

        :param int i_accuracy_type:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAccuracyType(i_accuracy_type, i_match)

    def set_accuracy_value(self, i_accuracy_value: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAccuracyValue(double iAccuracyValue,boolean iMatch)
                |     Set the accuracy profile value.
                | 
                |     Parameters:
                | 
                |         iAccuracyValue
                |             The accuracy value as a distance (m) or percent speed.
                |             
                |         iMatch
                |             Should the accuracy settings be used to find a controller profile
                |             match

        :param float i_accuracy_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAccuracyValue(i_accuracy_value, i_match)

    def set_fly_by_mode(self, i_fly_by: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFlyByMode(boolean iFlyBy,boolean iMatch)
                |     Set the accuracy profile fly by mode.
                | 
                |     Parameters:
                | 
                |         iFlyBy
                |             The flyby mode false for flyby off, true for flyby
                |             on.
                |         iMatch
                |             Should the accuracy settings be used to find a controller profile
                |             match 

        :param bool i_fly_by:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetFlyByMode(i_fly_by, i_match)

    def __repr__(self):
        return f'OLPAccuracyProfile(name="{ self.name }")'
