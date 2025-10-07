"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.todo_part.pattern import Pattern
from pycatia3dx.system.any_object import AnyObject


class UserPattern(Pattern):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.TransformationShape
                |                             CATPartIDLItf.Pattern
                |                                 UserPattern
                | 
                | Represents the user pattern.
                | The shape is copied along user's positions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def anchor_point(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnchorPoint() As AnyObject
                |     Returns the anchor point of the user pattern.
                | 
                |     Example:
                |         The following example returns in anchor the anchor point of the Pattern
                |         firstPattern:
                | 
                |          Set anchor = firstPattern.AnchorPoint

        :return: AnyObject
        """

        return AnyObject(self.com_object.AnchorPoint)

    @anchor_point.setter
    def anchor_point(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.AnchorPoint = value

    @property
    def feature_to_locate_positions(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeatureToLocatePositions() As AnyObject (Read Only)
                |     Returns the collection of feature to locate instances.
                | 
                |     Example:
                |         The following example returns in list the list of feature to locate
                |         instances of the Pattern firstPattern:
                | 
                |          Set list = firstPattern.FeatureToLocatePositions

        :return: AnyObject
        """

        return AnyObject(self.com_object.FeatureToLocatePositions)

    def add_feature_to_locate_positions(self, i_feature_to_locate_positions: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFeatureToLocatePositions(AnyObject
                | iFeatureToLocatePositions)
                |     Adds a new feature to locate instances.
                | 
                |     Parameters:
                | 
                |         iFeatureToLocatePositions
                |             The new object containing points of positioning 
                | 
                |     Example:
                |         The following example adds the new feature to locate instances
                |         of the Pattern firstPattern:
                | 
                |          call firstPattern.AddFeatureToLocatePositions(object)

        :param AnyObject i_feature_to_locate_positions:
        :return: None
        """
        return self.com_object.AddFeatureToLocatePositions(i_feature_to_locate_positions.com_object)

    def __repr__(self):
        return f'UserPattern(name="{ self.name }")'
