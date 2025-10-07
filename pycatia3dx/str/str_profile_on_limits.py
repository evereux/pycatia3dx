"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.structure_plate import StructurePlate


class StrProfileOnLimits(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfileOnLimits
                | 
                | Object to manage a Profile built on Limits
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def reference_support_plate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceSupportPlate(StructurePlate iStrPlate) (Write
                | Only)
                |     Set the reference support plate whose limits will be applied. In the two
                |     methods GetLimits & SetLimits, the limits of this reference plate are
                |     used.
                | 
                |     Example:
                | 
                | 
                |              This example sets the reference plate on the
                |              profileonlimits.
                |              
                | 
                |               ObjStrProfileOnLimits.ReferenceSupportPlate = ObjStrPlate

        :return: None
        """

        return None

    @reference_support_plate.setter
    def reference_support_plate(self, value: StructurePlate):
        """
        :param StructurePlate value:
        """

        self.com_object.ReferenceSupportPlate = value.com_object

    def get_limits(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLimits() As References
                |     Returns the list of limits on which profile is built. The limits has to be
                |     mono domain.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves limits of profile.
                |              
                | 
                |               Dim ObjStrProfileOnLimits As StrProfileOnLimits
                |               Set ObjStrProfileOnLimits = ObjSfdStiffenerOnFreeEdge.StrProfileOnLimits
                |               Set ListOfLimitRefs = ObjStrProfileOnLimits.GetLimits

        :return: References
        """
        return References(self.com_object.GetLimits())

    def get_trace_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTraceOffset() As Parameter
                |     Returns the offset used to perform a geodesic parallel curve from the
                |     Limits.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in limit offset.
                |              
                | 
                |               Dim OffsetParm As Parameter
                |               Set OffsetParm = ObjStrProfileOnLimits.GetTraceOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetTraceOffset())

    def set_limits(self, i_list_of_limit_index: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLimits(CATSafeArrayVariant iListOfLimitIndex)
                |     Sets the Limits indexes on which this Profile will be
                |     built.
                | 
                |     Parameters:
                | 
                |         iListOfLimitIndex
                |             List of Limits indexes. Array should contain long values like 1,
                |             2...
                |             These values corresponds to the limits of the
                |             panel.
                |             1 corresponds to the 1st limit
                |             2 corresponds to the 2nd limit ... 
                | 
                |     Example:
                | 
                | 
                |              This example sets limits indexes on which this profile will be
                |              created.
                |              
                | 
                |               Dim LimitIndexList(1) As Variant
                |               LimitIndexList(0) = 1
                |               LimitIndexList(1) = 4
                |               ObjStrProfileOnLimits.SetLimits (LimitIndexList)

        :param tuple i_list_of_limit_index:
        :return: tuple
        """
        return self.com_object.SetLimits(i_list_of_limit_index)

    def __repr__(self):
        return f'StrProfileOnLimits(name="{ self.name }")'
