"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.part.repartition import Repartition


class LinearRepartition(Repartition):

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
                |                         LinearRepartition
                | 
                | Represents the linear repartition.
                | It is used by the rectangular and circular patterns. It is made up of a number
                | of times the shape is copied and of a spacing distance between two consecutive
                | copies of this shape along a direction. The number of times the shape is copied
                | is accessible using the Repartition.InstancesCount property.
                | 
                | See also:
                |     RectPattern, CircPattern
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def spacing(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Spacing() As Length (Read Only)
                |     Returns the distance between two consecutive shapes along the repartition
                |     direction.
                | 
                |     Example:
                |         The following example returns in space1 the spacing distance of the
                |         linear repartition firstRepartition:
                | 
                |          Set space1 = firstRepartition.Spacing

        :return: Length
        """

        return Length(self.com_object.Spacing)

    def __repr__(self):
        return f'LinearRepartition(name="{ self.name }")'
