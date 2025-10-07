"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.part.defeaturing_filter import DefeaturingFilter


class DefeaturingFilterWithRange(DefeaturingFilter):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATPartIDLItf.DefeaturingFilter
                |                         DefeaturingFilterWithRange
                | 
                | Represents the base object for defeaturing filters which uses range(s) of
                | values
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_maximum_activity(self, i_range_id: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMaximumActivity(CATBSTR iRangeId) As boolean

        :param str i_range_id:
        :return: bool
        """
        return self.com_object.getMaximumActivity(i_range_id)

    def get_maximum_angle(self, i_range_id: str) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMaximumAngle(CATBSTR iRangeId) As Angle

        :param str i_range_id:
        :return: Angle
        """
        return Angle(self.com_object.getMaximumAngle(i_range_id))

    def get_maximum_length(self, i_range_id: str) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMaximumLength(CATBSTR iRangeId) As Length

        :param str i_range_id:
        :return: Length
        """
        return Length(self.com_object.getMaximumLength(i_range_id))

    def get_maximum_value(self, i_range_id: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMaximumValue(CATBSTR iRangeId) As double

        :param str i_range_id:
        :return: float
        """
        return self.com_object.getMaximumValue(i_range_id)

    def get_minimum_activity(self, i_range_id: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMinimumActivity(CATBSTR iRangeId) As boolean
                |     Returns the minimum or maximum value activity of the filter for the given
                |     range id.
                | 
                |     Parameters:
                | 
                |         iRangeId
                |             The identificator of the range on which the minimum/maximum should
                |             be read - if iRangeId is empty or equal to "Default", takes the default range
                |             as defined by the filter ("RibbonRadius" for FilletFilter, "MainDiameter" for
                |             HoleFilter) - else iRangeId should be chosen among: *
                |             {"RibbonRadius","RibbonAngle","RibbonLength"} for FilletFilter *
                |             {"MainDiameter"} for HoleFilter * any defined and supported range id in case of
                |             a user-defined filter 
                | 
                |     Returns:
                |         oValue The filter minimum/maximum activity for the specified
                |         range
                | 
                |         Example:
                |             The following example returns in theMinActivity the minimum value
                |             activity of filter myFilter for the range myRange:
                | 
                |              Set theMinActivity = myFilter.getMinimumActivity(myRange)

        :param str i_range_id:
        :return: bool
        """
        return self.com_object.getMinimumActivity(i_range_id)

    def get_minimum_angle(self, i_range_id: str) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMinimumAngle(CATBSTR iRangeId) As Angle

        :param str i_range_id:
        :return: Angle
        """
        return Angle(self.com_object.getMinimumAngle(i_range_id))

    def get_minimum_length(self, i_range_id: str) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMinimumLength(CATBSTR iRangeId) As Length

        :param str i_range_id:
        :return: Length
        """
        return Length(self.com_object.getMinimumLength(i_range_id))

    def get_minimum_value(self, i_range_id: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getMinimumValue(CATBSTR iRangeId) As double
                |     Returns the minimum or maximum value of the filter for the given range id,
                |     if defined and active.
                | 
                |     Parameters:
                | 
                |         iRangeId
                |             The identificator of the range on which the minimum/maximum should
                |             be read - if iRangeId is empty or equal to "Default", takes the default range
                |             as defined by the filter ("RibbonRadius" for FilletFilter, "MainDiameter" for
                |             HoleFilter) - else iRangeId should be chosen among: *
                |             {"RibbonRadius","RibbonAngle","RibbonLength"} for FilletFilter *
                |             {"MainDiameter"} for HoleFilter * any defined and supported range id in case of
                |             a user-defined filter 
                | 
                |     Returns:
                |         oValue The filter minimum/maximum value for the specified range if
                |         defined and active ELSE the method FAILS (to avoid this,
                |         getMinimumValueActivity/getMaximumValueActivity can be called prior to calling
                |         getMinimumValue/getMaximumValue) Signature with double works for angles as well
                |         as for lengthes / EXPRESSED in MODEL UNIT (mm/deg) Signatures with CATIALength
                |         or CATIAAngle must be used with care and will fail if the range nature and the
                |         expected type are incompatible
                | 
                |         Example:
                |             The following example returns in theMinValue the minimum value of
                |             filter myFilter for the range myRange:
                | 
                |              theMinValue = myFilter.getMinimumValue(myRange)
                | 
                |             The following example returns in theMinAngle the minimum value as
                |             an angle of filter myFilter for the range myRange:
                | 
                |              Set theMinAngle = myFilter.getMinimumAngle(myRange)
                | 
                |             The following example returns in theMaxLength the maximum value as
                |             a length of filter myFilter for the range myRange:
                | 
                |              Set theMaxLength = myFilter.getMaximumLength(myRange)

        :param str i_range_id:
        :return: float
        """
        return self.com_object.getMinimumValue(i_range_id)

    def set_maximum_activity(self, i_range_id: str, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub setMaximumActivity(CATBSTR iRangeId,boolean iValue)

        :param str i_range_id:
        :param bool i_value:
        :return: None
        """
        return self.com_object.setMaximumActivity(i_range_id, i_value)

    def set_maximum_value(self, i_range_id: str, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub setMaximumValue(CATBSTR iRangeId,double iValue)

        :param str i_range_id:
        :param float i_value:
        :return: None
        """
        return self.com_object.setMaximumValue(i_range_id, i_value)

    def set_minimum_activity(self, i_range_id: str, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub setMinimumActivity(CATBSTR iRangeId,boolean iValue)
                |     Sets the defeaturing minimum or maximum value activity of the filter for
                |     the given range id.
                | 
                |     Parameters:
                | 
                |         iRangeId
                |             The identificator of the range on which the minimum/maximum should
                |             be read - if iRangeId is empty or equal to "Default", takes the default range
                |             as defined by the filter ("RibbonRadius" for FilletFilter, "MainDiameter" for
                |             HoleFilter) - else iRangeId should be chosen among: *
                |             {"RibbonRadius","RibbonAngle","RibbonLength"} for FilletFilter *
                |             {"MainDiameter"} for HoleFilter * any defined and supported range id in case of
                |             a user-defined filter 
                |         iValue
                |             The filter minimum/maximum activity for the specified
                |             range
                | 
                |             Example:
                |                 The two following examples set theMaxActivity as the maximum
                |                 value activity of filter myFilter for the range
                |                 myRange:
                | 
                |                  Call
myFilter.setMaximumActivity(myRange,theMaxActivity)                |                  myFilter.setMaximumActivity myRange
                |                  theMaxActivity

        :param str i_range_id:
        :param bool i_value:
        :return: None
        """
        return self.com_object.setMinimumActivity(i_range_id, i_value)

    def set_minimum_value(self, i_range_id: str, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub setMinimumValue(CATBSTR iRangeId,double iValue)
                |     Sets the minimum or maximum value of the filter for the given range id.
                |     Forces the activation of the minimum or maximum value if not the case
                |     yet.
                | 
                |     Parameters:
                | 
                |         iRangeId
                |             The identificator of the range on which the minimum/maximum should
                |             be read - if iRangeId is empty or equal to "Default", takes the default range
                |             as defined by the filter ("RibbonRadius" for FilletFilter, "MainDiameter" for
                |             HoleFilter) - else iRangeId should be chosen among: *
                |             {"RibbonRadius","RibbonAngle","RibbonLength"} for FilletFilter *
                |             {"MainDiameter"} for HoleFilter * any defined and supported range id in case of
                |             a user-defined filter 
                |         iValue
                |             The filter minimum/maximum value for the specified range / MUST BE
                |             EXPRESSED in MODEL UNIT (mm/deg) iValue must be consistent with the other value
                |             if defined and active - new minimum iValue must be smaller than existing active
                |             maximum value if any - new maximum iValue must be larger than existing active
                |             minimum value if any ELSE the method FAILS
                | 
                |             Example:
                |                 The two following examples set theMaxValue as the maximum value
                |                 of filter myFilter for the range myRange:
                | 
                |                  Call
                |                  myFilter.setMaximumValue(myRange,theMaxValue)
                |                  myFilter.setMaximumValue myRange theMaxValue

        :param str i_range_id:
        :param float i_value:
        :return: None
        """
        return self.com_object.setMinimumValue(i_range_id, i_value)

    def __repr__(self):
        return f'DefeaturingFilterWithRange(name="{ self.name }")'
