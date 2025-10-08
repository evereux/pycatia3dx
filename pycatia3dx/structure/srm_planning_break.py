"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class SrmPlanningBreak(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrmPlanningBreak
                | 
                | Object to manage the Planning Break the design unit.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def limit(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Limit() As Reference (Read Only)
                |     Returns the limit of this planning break.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Limit object of the
                |              SrmPlanningBreak.
                |              
                | 
                |              Dim StartPB As SrmPlanningBreak
                |              Dim EndPB As SrmPlanningBreak
                |              ObjSrmProxyProfile.GetPlanningBreaks StartPB,
                |              EndPB
                |              Set LimitObj = StartPB.Limit

        :return: Reference
        """

        return Reference(self.com_object.Limit)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Orientation() As long (Read Only)
                |     Returns the Orientation of this planning break.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Orientation object of the
                |              SrmPlanningBreak.
                |              
                | 
                |              LimitObj = ObjStartSrmPB.Orientation

        :return: int
        """

        return self.com_object.Orientation

    def get_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOffset() As Parameter
                |     Returns the offset of this planning break.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves oOffset SrmPlanningBreak.
                |              
                | 
                |              Dim parmOffset As Parameter
                |              Set parmOffset = ObjStartSrmPB.GetOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetOffset())

    def __repr__(self):
        return f'SrmPlanningBreak(name="{ self.name }")'
