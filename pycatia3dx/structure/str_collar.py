"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_parameters import StrParameters


class StrCollar(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrCollar
                | 
                | Object to manage Collar on a Slot.
                | Role: Allows accessing of Collars's data.
                | 
                | See also:
                |     StrCollars
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def collar_parameters(self) -> StrParameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CollarParameters() As StrParameters (Read Only)
                |     Gets the Collar Public Parameters. Valuate them as
                |     required.
                | 
                |     Parameters:
                | 
                |         oListOfParameters
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the collar public parameters and evaluates
                |              them to 205mm & 35deg respectively.
                |              
                | 
                |              Dim ObjCollarParameters As StrParameters
                |             Set ObjCollarParameters = iObjStrCollar.CollarParameters
                |             Dim Width As Parameter
                |              Set Width = ObjCollarParameters.Item(1)
                |             Width.ValuateFromString("205mm")
                |             Dim Angle As Parameter
                |              Set Angle = ObjCollarParameters.Item(2)
                |             Angle.ValuateFromString("35deg")

        :return: StrParameters
        """

        return StrParameters(self.com_object.CollarParameters)

    @property
    def material(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Material(CATBSTR iMaterial)
                |     Sets/Gets the Collar Material.
                | 
                |     Example:
                | 
                | 
                |              This example sets the Collar Material.
                |              
                |              
                | 
                |     Parameters:
                | 
                |         iMaterial
                | 
                |              iObjStrCollar.Material = "Steel A90"
                |              
                | 
                |     Example:
                | 
                | 
                |              This example gets the Collar Material.
                |              
                |              
                | 
                |     Parameters:
                | 
                |         oMaterial
                | 
                |              Dim oMaterial As String
                |             oMaterial = iObjStrCollar.Material

        :return: str
        """

        return self.com_object.Material

    @material.setter
    def material(self, value: str):
        """
        :param False value:
        """

        self.com_object.Material = value

    @property
    def material_throw_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialThrowOrientation(CATStrCollarThrowOrientation
                | iMaterialThrowOrientation)
                |     Sets/gets the Collar Material Throw Orientation. (@see
                |     CATStrUseCollarThrowOrientation) Valid values for Material Throw Orientation
                |     are:
                |     - 0 : - catStrCollarThrowOrientationInvert
                |     - 1 : - catStrCollarThrowOrientationNormal
                |     - 2 : - catStrCollarThrowOrientationCentered
                | 
                |     Example:
                | 
                |          This example sets the material throw orientation
                | 
                |     Parameters:
                |         oMaterialThrowOrientation
                |              Dim oMaterialThrowOrientation As
                |              CATStrCollarThrowOrientation
                |              oMaterialThrowOrientation = iObjStrCollar.MaterialThrowOrientation
                |
                |     Example:
                |          This example gets the material throw orientation
                |     Parameters:
                |         iMaterialThrowOrientation
                |              iObjStrCollar.MaterialThrowOrientation = 1

        :return: int
        """

        return self.com_object.MaterialThrowOrientation

    @material_throw_orientation.setter
    def material_throw_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaterialThrowOrientation = value

    @property
    def thickness(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Thickness() As Parameter (Read Only)
                |     Gets the Collar Thickness. This property returns a Parameter (@see
                |     CATIAParameter) to Thickness for Collar. Valuate it as per
                |     required.
                | 
                |     Example:
                | 
                | 
                |              This example sets the Thickness. 
                |              
                |              
                | 
                |     Parameters:
                | 
                |         oThickness
                | 
                |              Dim oThickness As Parameter
                |             Set oThickness = iObjStrCollar.Thickness
                |             oThickness.ValuateFromString("20mm")

        :return: Parameter
        """

        return Parameter(self.com_object.Thickness)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Updates the Collars created. 

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'StrCollar(name="{self.name}")'
