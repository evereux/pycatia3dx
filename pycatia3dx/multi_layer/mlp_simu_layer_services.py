"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mmr_automation_interfaces.hybrid_body import HybridBody
from pycatia3dx.mode.reference import Reference
from pycatia3dx.multi_layer.mlp_simu_layer import MLPSimuLayer
from pycatia3dx.multi_layer.mlp_simu_layers import MLPSimuLayers
from pycatia3dx.system.any_object import AnyObject


class MLPSimuLayerServices(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MLPSimuLayerServices
                | 
                | CATIAMLPSimuLayerServices Role:Represents CATIAMLPSimuLayerServices that allow
                | to query simulation geometries from layers.
                | 
                | Example:
                |     This example illustrates how to call CATIAMLPSimuLayerServices interfaces .
                |     
                | 
                | 
                |     'FIND THE STACKING
                |     	Set Stacking = myPart.FindObjectByName("Stacking")
                |     	Dim StackingSimu As MLPStackingSimu
                |     	Set StackingSimu = Stacking.GetItem("CATMLPVBStackingSimu")
                | 
                |     'CREATE MLP SERVICES
                |     	Dim StackingSimuService As MLPSimuLayerServices
                |     	Set StackingSimuService = Stacking.GetItem("CATMLPVBStackingSimu")
                | 
                |     'CREATE SURFACE
                |     	Dim Surface As Reference
                |     	Set Surface = StackingSimuService.CreateSurfaceOfLayer(Layer, DestinationGeom)
                |     	Debug.Print "Name Surface : " & Surface.Name
                | 
                |     'GLUE INFORMATION
                |     	Dim ListGluedLayer As MLPSimuLayers
                |     	Set ListGluedLayer = StackingSimuService.GetGluedLayers(Layer)
                |     	For J = 1 To ListGluedLayer.Count
                |     		Dim LayerIsGlued As MLPSimuLayer
                |     		Set LayerIsGlued = ListGluedLayer.Item(J)
                |     		Debug.Print "  - GluedLayers : " & LayerIsGlued.Name
                |     	Next
                | 
                |        Dim LayerForComputation1 As MLPSimuLayer
                |     	Set LayerForComputation1 = listOfLayers.Item("TopSheetLotion")
                |     	Dim LayerForComputation2 As MLPSimuLayer
                |     	Set LayerForComputation2 = listOfLayers.Item("TopSheet")
                | 
                |     'TEST INTERSECTION
                |     	Dim Intersect As Reference
                |     	Set Intersect = StackingSimuService.CreateIntersectSurfacesOfLayers(LayerForComputation1, LayerForComputation2, DestinationGeom)
                |     	Debug.Print "Name Intersect : " & Intersect.Name
                | 
                |     'TEST JOIN
                |     	Dim Join As Reference
                |     	Set Join = StackingSimuService.CreateJoinSurfacesOfLayers(LayerForComputation1, LayerForComputation2, DestinationGeom)
                |     	Debug.Print "Name Join : " & Join.Name
                | 
                |     'TEST SUBSTRACT
                |     	Dim Subtract As Reference
                |     	Set Subtract = StackingSimuService.CreateSubstractSurfacesOfLayers(LayerForComputation2, LayerForComputation1, DestinationGeom)
                |     	Debug.Print "Name Subtract : " & Subtract.Name
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_geometry_of_layer(self, i_layer_simu: MLPSimuLayer, i_datum_destination: HybridBody) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateGeometryOfLayer(MLPSimuLayer iLayerSimu,HybridBody
                | iDatumDestination) As Reference
                |     Creates geometry of one layer (shell or solid according to the type of
                |     layer).
                | 
                |     Parameters:
                | 
                |         iLayerSimu
                |             The input layer 
                |         iDatumDestination
                |             The geometrical set destination where the surface will be created
                |             
                |         oDatumGeometry
                |             New layer surface

        :param MLPSimuLayer i_layer_simu:
        :param HybridBody i_datum_destination:
        :return: Reference
        """
        return Reference(self.com_object.CreateGeometryOfLayer(i_layer_simu.com_object, i_datum_destination.com_object))

    def create_intersect_surfaces_of_layers(
            self,
            i_layer_simu1: MLPSimuLayer,
            i_layer_simu2: MLPSimuLayer,
            i_datum_destination: HybridBody
    ) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateIntersectSurfacesOfLayers(MLPSimuLayer iLayerSimu1,MLPSimuLayer
                | iLayerSimu2,HybridBody iDatumDestination) As Reference
                |     Creates intersection of 2 layers.
                | 
                |     Parameters:
                | 
                |         iLayerSimu1
                |             The input layer1 
                |         iLayerSimu2
                |             The input layer2 
                |         iDatumDestination
                |             The geometrical set destination where the surface will be created
                |             
                |         oDatumGeometry
                |             The created intersection geometry

        :param MLPSimuLayer i_layer_simu1:
        :param MLPSimuLayer i_layer_simu2:
        :param HybridBody i_datum_destination:
        :return: Reference
        """
        return Reference(
            self.com_object.CreateIntersectSurfacesOfLayers(
                i_layer_simu1.com_object,
                i_layer_simu2.com_object,
                i_datum_destination.com_object
            )
        )

    def create_join_surfaces_of_layers(
            self,
            i_layer_simu1: MLPSimuLayer,
            i_layer_simu2: MLPSimuLayer,
            i_datum_destination: HybridBody
    ) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateJoinSurfacesOfLayers(MLPSimuLayer iLayerSimu1,MLPSimuLayer
                | iLayerSimu2,HybridBody iDatumDestination) As Reference
                |     Creates join of 2 layers.
                | 
                |     Parameters:
                | 
                |         iLayerSimu1
                |             The input layer1 
                |         iLayerSimu2
                |             The input layer2 
                |         iDatumDestination
                |             The geometrical set destination where the surface will be created
                |             
                |         oDatumGeometry
                |             The created join geometry

        :param MLPSimuLayer i_layer_simu1:
        :param MLPSimuLayer i_layer_simu2:
        :param HybridBody i_datum_destination:
        :return: Reference
        """
        return Reference(self.com_object.CreateJoinSurfacesOfLayers(
            i_layer_simu1.com_object,
            i_layer_simu2.com_object,
            i_datum_destination.com_object
        )
        )

    def create_substract_surfaces_of_layers(
            self,
            i_layer_simu1: MLPSimuLayer,
            i_layer_simu2: MLPSimuLayer,
            i_datum_destination: HybridBody
    ) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSubstractSurfacesOfLayers(MLPSimuLayer iLayerSimu1,MLPSimuLayer
                | iLayerSimu2,HybridBody iDatumDestination) As Reference
                |     Creates substraction of 2 layers.
                | 
                |     Parameters:
                | 
                |         iLayerSimu1
                |             The input layer1 
                |         iLayerSimu2
                |             The input substract layer2 
                |         iDatumDestination
                |             The geometrical set destination where the surface will be created
                |             
                |         oDatumGeometry
                |             The created substract geometry

        :param MLPSimuLayer i_layer_simu1:
        :param MLPSimuLayer i_layer_simu2:
        :param HybridBody i_datum_destination:
        :return: Reference
        """
        return Reference(
            self.com_object.CreateSubstractSurfacesOfLayers(
                i_layer_simu1.com_object,
                i_layer_simu2.com_object,
                i_datum_destination.com_object
            )
        )

    def create_surface_of_layer(self, i_layer_simu: MLPSimuLayer, i_datum_destination: HybridBody) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSurfaceOfLayer(MLPSimuLayer iLayerSimu,HybridBody iDatumDestination)
                | As Reference
                |     Creates surface of one layer.
                | 
                |     Parameters:
                | 
                |         iLayerSimu
                |             The input layer 
                |         iDatumDestination
                |             The geometrical set destination where the surface will be created
                |             
                |         oDatumGeometry
                |             New layer surface

        :param MLPSimuLayer i_layer_simu:
        :param HybridBody i_datum_destination:
        :return: Reference
        """
        return Reference(self.com_object.CreateSurfaceOfLayer(i_layer_simu.com_object, i_datum_destination.com_object))

    def get_glued_layers(self, i_glue_l_ayer_simu: MLPSimuLayer) -> MLPSimuLayers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGluedLayers(MLPSimuLayer iGlueLAyerSimu) As
                | MLPSimuLayers
                |     Retrieves Layer impacted by a glue layer at a specific
                |     position.
                | 
                |     Parameters:
                | 
                |         iGlueLAyerSimu
                |             The glue layer 
                |         oListOfGluedLayers
                |             return the list of glued layers

        :param MLPSimuLayer i_glue_l_ayer_simu:
        :return: MLPSimuLayers
        """
        return MLPSimuLayers(self.com_object.GetGluedLayers(i_glue_l_ayer_simu.com_object))

    def get_glued_layers_at_point(
            self,
            i_glue_l_ayer_simu: MLPSimuLayer,
            i_x: float,
            i_y: float,
            i_z: float
    ) -> MLPSimuLayers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGluedLayersAtPoint(MLPSimuLayer iGlueLAyerSimu,float iX,float iY,float
                | iZ) As MLPSimuLayers
                |     Retrieves Layer impacted by a glue layer at a specific
                |     position.
                | 
                |     Parameters:
                | 
                |         iGlueLAyerSimu
                |             The glue layer 
                |         iX
                |             Position X 
                |         iY
                |             Position Y 
                |         iZ
                |             Position Z 
                |         oListOfGluedLayers
                |             return the list of glued layers at position (X,Y,Z)

        :param MLPSimuLayer i_glue_l_ayer_simu:
        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: MLPSimuLayers
        """
        return MLPSimuLayers(self.com_object.GetGluedLayersAtPoint(i_glue_l_ayer_simu.com_object, i_x, i_y, i_z))

    def __repr__(self):
        return f'MlpSimuLayerServices(name="{self.name}")'
