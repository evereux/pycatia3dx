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


class StrPanelSurf(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrPanelSurf
                | 
                | Object to manage an structure Panel created in surface mode.
                | Role: To access Support of panel.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Support() As Reference
                |     Returns or Sets the support of this Panel.
                | 
                |     Example:
                | 
                | 
                |              This example sets Support of the panel.
                |              
                | 
                |               Dim PanelSupport As Reference
                |               Set ObjPanelSupport = Manager.GetReferencePlane(ObjPart, 2, "CROSS.0")
                |               Set PanelSupport = ObjPart.CreateReferenceFromObject(ObjPanelSupport)
                |               Dim ObjStrPanelSurf As StrPanelSurf
                |               Set ObjStrPanelSurf = ObjSfdPanel.StrPanelSurf
                |               ObjStrPanelSurf.Support = PanelSupport

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    def get_support_offset(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSupportOffset() As Parameter
                |     Returns the parameter offset applied on the user support of this SuperPlate
                |     function.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves SupportOffset of the panel
                |              support.
                |              
                | 
                |               Dim OffsetParm As Parameter
                |               Set OffsetParm = ObjStrPanelSurf.GetSupportOffset

        :return: Parameter
        """
        return Parameter(self.com_object.GetSupportOffset())

    def __repr__(self):
        return f'StrPanelSurf(name="{ self.name }")'
