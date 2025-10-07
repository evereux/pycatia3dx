"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.surface_based_shape import SurfaceBasedShape


class Partition(SurfaceBasedShape):

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
                |                         CATPartIDLItf.SurfaceBasedShape
                |                             Partition
                | 
                | Represents the partition operation.
                | It create a partitioned body using a cutting element, such as a surface, a face
                | or a plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def auto_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AutoMode() As boolean
                |     Returns or sets the Automatic Partition Mode.
                |     True if the automatic mode is active

        :return: bool
        """

        return self.com_object.AutoMode

    @auto_mode.setter
    def auto_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AutoMode = value

    @property
    def limit_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LimitType() As CatPartitionLimitType
                |     Returns or sets the Limit Type . The limiting type is the mode of cutting element extrapolation The limitation type of partition : None, Infinite, Up to next
                | 
                |     Example:
                |         The following example returns in limitType the limit type of the
                |         partition myPartition, and then sets it to
                |         CatPartitionLimit_None:
                | 
                |          Set limitType = myPartition.LimitType
                |          myPartition.LimitType = CatPartitionLimit_None

        :return: CatPartitionLimitType
        """

        return self.com_object.LimitType

    @limit_type.setter
    def limit_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.LimitType = value

    @property
    def volume(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Volume() As Reference
                |     Returns or sets the volume to partition. 

        :return: Reference
        """

        return Reference(self.com_object.Volume)

    @volume.setter
    def volume(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Volume = value

    def __repr__(self):
        return f'Partition(name="{ self.name }")'
