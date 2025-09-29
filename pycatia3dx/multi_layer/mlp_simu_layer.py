"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.axis_system import AxisSystem
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection


class MLPSimuLayer(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MLPSimuLayer
                | 
                | CATIAMLPSimuLayer Role:Represents CATIAMLPSimuLayer that allow to query on
                | Layer entity.
                | .
                | 
                | Example:
                |     This example illustrates how to call CATIAMLPSimuLayer interfaces .
                |     
                | 
                |       Dim Layer As MLPSimuLayer
                |     		Set Layer = listOfLayers.Item(I)
                | 
                | 
                |     		Debug.Print
                |     "--------------------------------------------"
                |     		Debug.Print "Name : " & Layer.Name
                |     		Debug.Print "IsGlue : " & Layer.IsGlue
                |     		Debug.Print "IsGridOrProfile : " & Layer.IsGridOrProfile
                | 
                | 
                |     'MATERIAL INFORMATION
                |     		If Layer.HasMaterial = True Then
                | 
                |     			Dim LayerMaterial As PLMEntity
                |     			Set LayerMaterial = Layer.LayerMaterial
                |     			Debug.Print "Name Of Material : " & LayerMaterial.Name
                |     			Debug.Print "Thickness : " & Layer.ThicknessValue
                | 
                |     		End If
                |     'GLUE INFORMATION (Relation Layer & Mechanical Bond)
                |     		If Layer.IsGlue = True Then
                | 
                |     			Debug.Print "Type glue : " & Layer.TypeOfGlue
                |     				Dim ListGluedLayer As MLPSimuLayers
                |     				Set ListGluedLayer = StackingSimuService.GetGluedLayers(Layer)
                |     				For J = 1 To ListGluedLayer.Count
                | 
                |     					Dim LayerIsGlued As MLPSimuLayer
                |     					Set LayerIsGlued = ListGluedLayer.Item(J)
                |     					Debug.Print "  - GluedLayers : " & LayerIsGlued.Name
                |     				Next
                |     		Else
                | 
                |     'AXIS SYSTEM
                |     			Dim AxisLayer As AxisSystem
                |     			Set AxisLayer = Layer.LayerAxisSystem
                |     			Debug.Print "Name Axis : " & AxisLayer.Name
                | 
                |     		End If
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def glued_layers(self) -> Collection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GluedLayers() As Collection (Read Only)
                |     Returns the list of glued layers by the current layer.
                | 
                |     Parameters:
                | 
                |         oListOfGluedLayers
                |             The list of glued layers by the current layer

        :return: Collection
        """

        return Collection(self.com_object.GluedLayers)

    @property
    def has_material(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HasMaterial() As boolean (Read Only)
                |     Returns if the current layer have a material.
                | 
                |     Parameters:
                | 
                |         oHasMaterial
                |             The method returns true if the layer have a material

        :return: bool
        """

        return self.com_object.HasMaterial

    @property
    def is_elastic(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsElastic() As boolean (Read Only)
                |     Returns if the Layer is an elastic.
                | 
                |     Parameters:
                | 
                |         oIsElastic
                |             If the method return true, the Layer is an elastic

        :return: bool
        """

        return self.com_object.IsElastic

    @property
    def is_glue(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsGlue() As boolean (Read Only)
                |     Returns if the Layer is a Glue.
                | 
                |     Parameters:
                | 
                |         oIsGlue
                |             If the method return true, the Layer is a Glue

        :return: bool
        """

        return self.com_object.IsGlue

    @property
    def is_grid_or_profile(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsGridOrProfile() As boolean (Read Only)
                |     Returns if the Layer is a grid or a profile.
                | 
                |     Parameters:
                | 
                |         oIsGridOrProfile
                |             If the method return true, the Layer is a grid or profile

        :return: bool
        """

        return self.com_object.IsGridOrProfile

    @property
    def layer_axis_system(self) -> AxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LayerAxisSystem() As AxisSystem (Read Only)
                |     Returns the axis system of a Layer.
                | 
                |     Parameters:
                | 
                |         oAxisSystem
                |             Axis System of the current Layer

        :return: AxisSystem
        """

        return AxisSystem(self.com_object.LayerAxisSystem)

    @property
    def layer_material(self) -> PLMEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LayerMaterial() As PLMEntity (Read Only)
                |     Returns the material reference of a current layer.
                | 
                |     Parameters:
                | 
                |         oMaterial
                |             The material applied to the current layer

        :return: PLMEntity
        """

        return PLMEntity(self.com_object.LayerMaterial)

    @property
    def stretch_ratio(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StretchRatio() As double (Read Only)
                |     Returns the value of the stretch ratio if the layer is an
                |     elastic.
                | 
                |     Parameters:
                | 
                |         oStretchRatio
                |             The method returns the strech ratio

        :return: float
        """

        return self.com_object.StretchRatio

    @property
    def thickness_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessValue() As double (Read Only)
                |     Returns thickness of a Layer.
                | 
                |     Parameters:
                | 
                |         oThickness
                |             Thickness of the current Layer

        :return: float
        """

        return self.com_object.ThicknessValue

    @property
    def type_of_glue(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TypeOfGlue() As CATBSTR (Read Only)
                |     Returns the type of Glue.
                | 
                |     Parameters:
                | 
                |         oGlueType
                |             The method returns the type of the current glue layer

        :return: str
        """

        return self.com_object.TypeOfGlue

    def glued_layers_at_position(self, i_x: float, i_y: float, i_z: float) -> Collection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GluedLayersAtPosition(float iX,float iY,float iZ) As
                | Collection
                |     Returns the list of glued layers by the current layer.
                | 
                |     Parameters:
                | 
                |         oListOfGluedLayers
                |             The list of glued layers by the current layer 
                |         iX
                |             Position X 
                |         iY
                |             Position Y 
                |         iZ
                |             Position Z

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: Collection
        """
        return Collection(self.com_object.GluedLayersAtPosition(i_x, i_y, i_z))

    def __repr__(self):
        return f'MlpSimuLayer(name="{self.name}")'
