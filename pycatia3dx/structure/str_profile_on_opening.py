"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_opening import StrOpening


class StrProfileOnOpening(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfileOnOpening
                | 
                | Object to manage a Profile built on an Opening
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def opening(self) -> StrOpening:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Opening() As StrOpening
                |     Returns or Sets the Opening on which this Profile will be
                |     built.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Opening on which the profile will be
                |              built.
                |              
                | 
                |              Dim ObjStrProfileOnOpening As StrProfileOnOpening
                |              Set ObjStrProfileOnOpening = ObjSfdStiffenerOnFreeEdge.StrProfileOnOpening
                |              Set ObjStrOpening = ObjStrProfileOnOpening.Opening

        :return: StrOpening
        """

        return StrOpening(self.com_object.Opening)

    @opening.setter
    def opening(self, value: StrOpening):
        """
        :param StrOpening value:
        """

        self.com_object.Opening = value

    def get_trace_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTraceOffset() As Parameter
                |     Returns the TraceOffset offset.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in CurveOffset of the
                |              curve.
                |              
                | 
                |               Dim OffsetParm As Parameter
                |               Set OffsetParm = ObjStrProfileOnOpening.GetTraceOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetTraceOffset())

    def __repr__(self):
        return f'StrProfileOnOpening(name="{self.name}")'
