"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.part.repartition import Repartition


class AngularRepartition(Repartition):

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
                |                         AngularRepartition
                | 
                | Represents the angular repartition.
                | It is used by the circular pattern. It is made up of a number of times the
                | shape is copied and of an angular spacing between two consecutive copies of the
                | shape along a crown. The number of times the shape is copied is accessible
                | using the Repartition.InstancesCount property.
                | 
                | See also:
                |     CircPattern
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angular_spacing(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngularSpacing() As Angle (Read Only)
                |     Returns the angle between two consecutive copies of a shape along the
                |     repartition crown.
                | 
                |     Example:
                |         The following example returns in AngSpace1 the angular spacing of the
                |         angular repartition firstRepartition:
                | 
                |          Set AngSpace1 = firstRepartition.AngularSpacing

        :return: Angle
        """

        return Angle(self.com_object.AngularSpacing)

    @property
    def instance_spacing(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InstanceSpacing() As Angle (Read Only)
                |     Returns the angle at which the pattern spacing is done for unequal angular
                |     spacing mode.
                | 
                |     Example:
                |         The following example returns in AngSpace1 the angular spacing of the
                |         angular repartition firstRepartition:
                | 
                |          Set AngSpace1 = firstRepartition.AngularSpacing

        :return: Angle
        """

        return Angle(self.com_object.InstanceSpacing)

    def __repr__(self):
        return f'AngularRepartition(name="{ self.name }")'
