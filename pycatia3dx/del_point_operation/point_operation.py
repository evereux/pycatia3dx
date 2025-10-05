"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PointOperation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PointOperation
                | 
                | Interface representing a PointOperation.
                | 
                | Role: This interface is used to get and set attributes specific to Point
                | Operation
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def point_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointProfile() As AnyObject (Read Only)
                |     This property returns and sets Point profile used by the Point
                |     Operation.
                | 
                |     Returns:
                |         oPointProfile The Point profile (Spot weld or Rivet Profile) used.
                |         
                |     Parameters:
                | 
                |         iPointProfile
                |             Spot weld or Rivet Profile to be set as application profile to the
                |             Point Operation. 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objPointOperation As PointOperation
                |             ....
                |             Dim oSpotProfile As SpotWeldProfile
                |             ....
                |             Set objPointOperation.PointProfile = oSpotProfile
                |             Set oSpotProfile = objPointOperation.PointProfile

        :return: AnyObject
        """

        return AnyObject(self.com_object.PointProfile)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     This property retrieves the Type of the Point Operation.
                | 
                |     Parameters:
                | 
                |         oType
                |             Type of the Point Operation. The value could be either "Weld" or
                |             "Rivet" 
                | 
                |     Example:
                | 
                |            
                | 
                |             Dim objPointOperation As PointOperation
                |                   ......
                |             Dim opType As String
                |             opType = objPointOperation.Type

        :return: str
        """

        return self.com_object.Type

    def set_point_profile(self, i_point_profile: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub set_PointProfile(AnyObject iPointProfile)

        :param AnyObject i_point_profile:
        :return: None
        """
        return self.com_object.set_PointProfile(i_point_profile.com_object)

    def __repr__(self):
        return f'PointOperation(name="{ self.name }")'
