"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_reference import StrReference


class StrPosDualRef(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrPosDualRef
                | 
                | Object representing a parameter used in the Structures model
                | elements.
                | This interface is used with interfaces to Structures model elements to retrieve
                | the role of the parameter with the parameter object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def role(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Role() As CATBSTR (Read Only)
                |     Returns the role of this parameter. The role is specific to the element
                |     from which this interface was retrieved.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the role of the parameter.
                |              
                | 
                |              Dim ObjStrStandardPosStrategyParameters As
                |              StrStandardPosStrategyParameters
                |              Set ObjStrStandardPosStrategyParameters = ObjStrOpeningsMgr.GetStandardPositioningStrategyParms(StdPosStrategyName)
                |              Dim ObjStrPosDualRef As StrPosDualRef
                |              Set ObjStrPosDualRef = ObjStrStandardPosStrategyParameters.Item(1)
                |              If (TypeName(ObjStrPosDualRef) = "StrPosDualRef") Then
                |                  StrRole = ObjStrPosDualRef.Role
                |              End If

        :return: str
        """

        return self.com_object.Role

    def get_ref1_data(self) -> StrReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRef1Data() As StrReference
                |     Returns the first reference specification to access (set/get) the reference
                |     element. Note: The order of the reference elements is not
                |     significant.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the first reference
                |              specification.
                |              
                | 
                |              Set Reference1 = ObjStrPosDualRef.GetRef1Data

        :return: StrReference
        """
        return StrReference(self.com_object.GetRef1Data())

    def get_ref2_data(self) -> StrReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRef2Data() As StrReference
                |     Returns the second reference specification to access (set/get) the
                |     reference element. Note: The order of the reference elements is not
                |     significant.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the second reference
                |              specification.
                |              
                | 
                |              Set Reference2 = ObjStrPosDualRef.GetRef2Data

        :return: StrReference
        """
        return StrReference(self.com_object.GetRef2Data())

    def __repr__(self):
        return f'StrPosDualRef(name="{self.name}")'
