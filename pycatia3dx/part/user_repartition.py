"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.todo_part.repartition import Repartition
from pycatia3dx.system.any_object import AnyObject


class UserRepartition(Repartition):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATPartIDLItf.Repartition
                |                         UserRepartition
                | 
                | Represents the User Pattern repartition.
                | It is made up of a number of times the shape is copied and the location of
                | instances. The number of times the shape is copied is accessible using the
                | Repartition.InstancesCount property.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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
                |             The new face to process 
                | 
                |     Example:
                |         The following example adds the new feature to locate instances
                |         of the Pattern firstPattern:
                | 
                |          call firstPattern.AddFeatureToLocatePositions(face)

        :param AnyObject i_feature_to_locate_positions:
        :return: None
        """
        return self.com_object.AddFeatureToLocatePositions(i_feature_to_locate_positions.com_object)

    def __repr__(self):
        return f'UserRepartition(name="{ self.name }")'
