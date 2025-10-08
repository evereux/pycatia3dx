"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class StrParameter(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrParameter
                | 
                | Object representing a relationship to a parameter used in the Structures model
                | elements
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def parameter(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parameter() As Parameter
                |     Returns or sets the CKE parameter related to this volatile parameter
                |     object. This CKE parameter may be a volatile or persistent CKE parameter,
                |     depending on the state of the object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ContourParam the parameter of the
                |              object.
                |              
                | 
                |              Set ContourParam = ObjStrParameter.Parameter

        :return: Parameter
        """

        return Parameter(self.com_object.Parameter)

    @parameter.setter
    def parameter(self, value: Parameter):
        """
        :param Parameter value:
        """

        self.com_object.Parameter = value

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
                |              This example retrieves in StrRole the role of the
                |              parameter.
                |              
                | 
                |              Dim ObjStrStandardContourParameters As
                |              StrStandardContourParameters
                |              Set ObjStrStandardContourParameters = ObjStrOpeningsMgr.GetStandardContourParms(ContourName)
                |              Dim ObjStrParameter As StrParameter
                |              Set ObjStrParameter = ObjStrStandardContourParameters.Item(1)
                |              StrRole = ObjStrParameter.Role

        :return: str
        """

        return self.com_object.Role

    def __repr__(self):
        return f'StrParameter(name="{ self.name }")'
