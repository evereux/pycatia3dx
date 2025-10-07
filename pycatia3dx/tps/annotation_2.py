"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.coord_dim import CoordDim
from pycatia3dx.tps.datum_simple import DatumSimple
from pycatia3dx.tps.datum_target import DatumTarget
from pycatia3dx.tps.default_annotation import DefaultAnnotation
from pycatia3dx.tps.dimension_3d import Dimension3D
from pycatia3dx.tps.flag_note import FlagNote
from pycatia3dx.tps.noa import Noa
from pycatia3dx.tps.non_semantic_datum import NonSemanticDatum
from pycatia3dx.tps.non_semantic_datum_target import NonSemanticDatumTarget
from pycatia3dx.tps.non_semantic_dimension import NonSemanticDimension
from pycatia3dx.tps.non_semantic_gdt import NonSemanticGDT
from pycatia3dx.tps.reference_frame import ReferenceFrame
from pycatia3dx.tps.roughness import Roughness
from pycatia3dx.tps.semantic_gdt import SemanticGDT
from pycatia3dx.tps.text import Text
from pycatia3dx.tps.tps_hyper_links_manager import TPSHyperLinksManager
from pycatia3dx.tps.tps_view import TPSView
from pycatia3dx.tps.weld import Weld


class Annotation2(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Annotation2
                | 
                | Interface for the Technological Product Specification (TPS)
                | objects.
                | Leaf entity in the Design Pattern Composite. TPS modeler enables definition of
                | specification related to surfaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def super_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SuperType() As CATBSTR (Read Only)
                |     Gets the Super Type.
                | 
                |     Parameters:
                | 
                |         oSuperType
                |             The Super Type.
                | 
                |             The list of SuperType available:
                |             "FTA_NonSemantic"
                |             "FTA_Form"
                |             "FTA_Dimension"
                |             "FTA_Position"
                |             "FTA_Datum"
                |             "FTA_Orientation"
                |             "FTA_RunOut"

        :return: str
        """

        return self.com_object.SuperType

    @property
    def tps_status(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TPSStatus() As CATBSTR (Read Only)
                |     Gets the TPS Status.
                | 
                |     Parameters:
                | 
                |         oStatus
                |             The Status.

        :return: str
        """

        return self.com_object.TPSStatus

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Gets the Type.
                | 
                |     Parameters:
                | 
                |         oType
                |             The Type.
                | 
                |             List of types available ordered by SuperType:
                |             SuperType = "FTA_NonSemantic"
                |             Type = "FTA_Text"
                |             Type = "FTA_FlagNote"
                |             Type = "FTA_Roughness"
                |             Type = "FTA_Weld"
                |             Type = "FTA_Noa"
                |             Type = "FTA_NonSemanticDatum"
                |             Type = "FTA_NonSemanticTarget"
                |             Type = "FTA_NonSemanticGDT"
                |             Type = "FTA_NonSemanticDimension"
                | 
                |             SuperType = "FTA_Form"
                |             Type = "FTA_Flatness"
                |             Type = "FTA_Straightness"
                |             Type = "FTA_Circularity"
                |             Type = "FTA_Cylindricity"
                |             Type = "FTA_ProfileOfAnyLine"
                |             Type = "FTA_ProfileOfASurface"
                |             Type = "FTA_PatternTruePos"
                | 
                |             SuperType = "FTA_Dimension"
                |             Type = "FTA_LinearDimension"
                |             Type = "FTA_AngularDimension"
                |             Type = "FTA_SecondLinearDimension"
                |             Type = "FTA_ChamferDimension"
                |             Type = "FTA_BasicDimension"
                | 
                |             SuperType = "FTA_Position"
                |             Type = "FTA_TruePosition"
                |             Type = "FTA_Concentricity"
                |             Type = "FTA_Symmetry"
                |             Type = "FTA_PositionOfAnyLine"
                |             Type = "FTA_PositionOfASurface"
                | 
                |             SuperType = "FTA_Datum"
                |             Type = "FTA_DatumSimple"
                |             Type = "FTA_DatumTarget"
                |             Type = "FTA_DatumSystem"
                |             Type = "FTA_ReferenceFrame"
                | 
                |             SuperType = "FTA_Orientation"
                |             Type = "FTA_Parallelism"
                |             Type = "FTA_Perpendicularity"
                |             Type = "FTA_Angularity"
                | 
                |             SuperType = "FTA_RunOut"
                |             Type = "FTA_TotalRunOut"
                |             Type = "FTA_CircularRunOut"

        :return: str
        """

        return self.com_object.Type

    @property
    def z(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Z(double iZ) (Write Only)
                |     method get_Z will never be exposed. Sets the offset of the
                |     annotation.
                | 
                |     Parameters:
                | 
                |         iZ
                |             The offset.

        :return: None
        """

        return None

    @z.setter
    def z(self, value: float):
        """
        :param float value:
        """

        self.com_object.Z = value

    def add_leader(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddLeader()
                |     Adds a leader.

        :return: None
        """
        return self.com_object.AddLeader()

    def coordinatedimension(self) -> CoordDim:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Coordinatedimension() As CoordDim
                |     Retrieves the FTA co coordinate dimension.

        :return: CoordDim
        """
        return CoordDim(self.com_object.Coordinatedimension())

    def datum_simple(self) -> DatumSimple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DatumSimple() As DatumSimple
                |     Gets the annotation on the DatumSimple interface.

        :return: DatumSimple
        """
        return DatumSimple(self.com_object.DatumSimple())

    def datum_target(self) -> DatumTarget:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DatumTarget() As DatumTarget
                |     Gets the annotation on the DatumTarget interface.

        :return: DatumTarget
        """
        return DatumTarget(self.com_object.DatumTarget())

    def default_annotation(self) -> DefaultAnnotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefaultAnnotation() As DefaultAnnotation
                |     Gets the annotation on the DefaultAnnotation interface.

        :return: DefaultAnnotation
        """
        return DefaultAnnotation(self.com_object.DefaultAnnotation())

    def dimension3_d(self) -> Dimension3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Dimension3D() As Dimension3D
                |     Gets the 3D Dimension on the 3D Dimension interface.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The 3D Dimension.

        :return: Dimension3D
        """
        return Dimension3D(self.com_object.Dimension3D())

    def flag_note(self) -> FlagNote:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FlagNote() As FlagNote
                |     Gets the annotation on the FlagNote interface.
                | 
                |     Parameters:
                | 
                |         oFlagNote
                |             The annotation Flag Note.

        :return: FlagNote
        """
        return FlagNote(self.com_object.FlagNote())

    def get_geometrical_component_name(self, i_index: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGeometricalComponentName(short iIndex) As CATBSTR
                |     Gets the Geometrical Component name at given index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the geometrical component; this value is greater or
                |             equal to 1 and lower or equal to the value returned by
                |             GetNbrOfGeometricalComponent. 
                |         oComponentName
                |             The name of the geometrical component.

        :param int i_index:
        :return: str
        """
        return self.com_object.GetGeometricalComponentName(i_index)

    def get_nbr_of_geometrical_component(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbrOfGeometricalComponent() As short
                |     Gets the number of geometrical components.
                | 
                |     Parameters:
                | 
                |         oGeomLinkNbr
                |             The number of links to the geometry employed by this
                |             annotation.
                |             The returned value is comprise in between 1 and N (N is at most the
                |             total of geometrical links existing under the
                |             annotation).
                |             The amount of Geometrical Component sent back may be different from
                |             the annotation total links to the geometry because
                |             sometimes
                |             the Group of Surfaces may point to the same geometrical component
                |             participating to the definition of several User Surfaces.

        :return: int
        """
        return self.com_object.GetNbrOfGeometricalComponent()

    def get_surfaces(self, o_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSurfaces(CATSafeArrayVariant oSafeArray)
                |     Gets the geometry on which the Annotation is applied to.

        :param tuple o_safe_array:
        :return: None
        """
        return self.com_object.GetSurfaces(o_safe_array)

    def get_surfaces_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSurfacesCount() As long
                |     Counts the geometry on which the Annotation is applied to.

        :return: int
        """
        return self.com_object.GetSurfacesCount()

    def has_a_visualization_dimension(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAVisualizationDimension() As boolean
                |     Checks if the Annotation uses a visualization dimension for its attachment
                |     to the geometry.

        :return: bool
        """
        return self.com_object.HasAVisualizationDimension()

    def hyper_link_manager(self) -> TPSHyperLinksManager:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HyperLinkManager() As TPSHyperLinksManager
                |     Gets the annotation on HyperLinks manager interface.

        :return: TpsHyperLinksManager
        """
        return TPSHyperLinksManager(self.com_object.HyperLinkManager())

    def is_a_consumable_annotation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAConsumableAnnotation() As boolean
                |     Checks if the Annotation is a Consumable Annotation.

        :return: bool
        """
        return self.com_object.IsAConsumableAnnotation()

    def is_a_default_annotation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsADefaultAnnotation() As boolean
                |     Checks if the Annotation is a Default Annotation.

        :return: bool
        """
        return self.com_object.IsADefaultAnnotation()

    def modify_visu(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyVisu()
                |     To refresh the 3D visualization.

        :return: None
        """
        return self.com_object.ModifyVisu()

    def noa(self) -> Noa:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Noa() As Noa
                |     Gets the annotation on the Noa interface.

        :return: Noa
        """
        return Noa(self.com_object.Noa())

    def non_semantic_datum(self) -> NonSemanticDatum:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func NonSemanticDatum() As NonSemanticDatum
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticDatum
        """
        return NonSemanticDatum(self.com_object.NonSemanticDatum())

    def non_semantic_datum_target(self) -> NonSemanticDatumTarget:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func NonSemanticDatumTarget() As NonSemanticDatumTarget
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticDatumTarget
        """
        return NonSemanticDatumTarget(self.com_object.NonSemanticDatumTarget())

    def non_semantic_dimension(self) -> NonSemanticDimension:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func NonSemanticDimension() As NonSemanticDimension
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticDimension
        """
        return NonSemanticDimension(self.com_object.NonSemanticDimension())

    def non_semantic_gdt(self) -> NonSemanticGDT:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func NonSemanticGDT() As NonSemanticGDT
                |     Gets the annotation on the DatumSimple interface.

        :return: NonSemanticGDT
        """
        return NonSemanticGDT(self.com_object.NonSemanticGDT())

    def reference_frame(self) -> ReferenceFrame:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ReferenceFrame() As ReferenceFrame
                |     Gets the annotation on the ReferenceFrame interface.

        :return: ReferenceFrame
        """
        return ReferenceFrame(self.com_object.ReferenceFrame())

    def roughness(self) -> Roughness:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Roughness() As Roughness
                |     Gets the annotation on the Roughness interface.

        :return: Roughness
        """
        return Roughness(self.com_object.Roughness())

    def semantic_gdt(self) -> SemanticGDT:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SemanticGDT() As SemanticGDT
                |     Gets the annotation on the DatumSimple interface.

        :return: SemanticGDT
        """
        return SemanticGDT(self.com_object.SemanticGDT())

    def set_geometrical_component_name(self, i_index: int, i_new_name: str, i_check_name_unicity_option: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGeometricalComponentName(short iIndex,CATBSTR iNewName,boolean
                | iCheckNameUnicityOption)
                |     Sets the Geometrical Component name at given index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the geometrical component; this value is greater or
                |             equal to 1 and lower or equal to the value returned by
                |             GetNbrOfGeometricalComponent.
                |             The user is allowed to pass a 0 value as index; in this case, an
                |             automatic renaming is triggered.
                |             In this case the usual path of a geometrical component (for
                |             instance Face/Name of the feature/Body.1) is used to extract the logical name
                |             to apply "Name of the feature".
                |             Pay attention that geometrical component name must be unique; this
                |             method is exiting in error whenever the unicity is of geometrical component is
                |             broken.
                |             The renaming processing is given up without any change when an
                |             already existing name is passed to this method or when automatic processing
                |             faces naming ambiguity. 
                |         iNewName
                |             The string used to rename the geometrical component.
                |             
                |         iCheckNameUnicityOption
                |             Option to trigger an addition verification during renaming to
                |             guarantee that the entire set of Geometrical Components in the
                |             representation
                |             have a different name.

        :param int i_index:
        :param str i_new_name:
        :param bool i_check_name_unicity_option:
        :return: None
        """
        return self.com_object.SetGeometricalComponentName(i_index, i_new_name, i_check_name_unicity_option)

    def set_xy(self, i_x: float, i_y: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetXY(double iX,double iY)
                |     method GetXY will never be exposed. Sets TPS coordinates in the
                |     view.
                | 
                |     Parameters:
                | 
                |         oX
                |             The X coordinate. 
                |         oY
                |             The Y coordinate.

        :param float i_x:
        :param float i_y:
        :return: None
        """
        return self.com_object.SetXY(i_x, i_y)

    def text(self) -> Text:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Text() As Text
                |     Gets the annotation on the Text interface.
                | 
                |     Parameters:
                | 
                |         oText
                |             The annotation Text.

        :return: Text
        """
        return Text(self.com_object.Text())

    def transfert_to_view(self, i_view: TPSView) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub TransfertToView(TPSView iView)
                |     Moves the annotation in another view.
                | 
                |     Parameters:
                | 
                |         iView
                |             The destination view.

        :param TPSView i_view:
        :return: None
        """
        return self.com_object.TransfertToView(i_view.com_object)

    def visualization_dimension(self) -> Dimension3D:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func VisualizationDimension() As Dimension3D
                |     Gets the dimension visualization associated with the
                |     annotation.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The visualization Dimension oDim employed by the annotation to
                |             display its link to the geometry.

        :return: Dimension3D
        """
        return Dimension3D(self.com_object.VisualizationDimension())

    def weld(self) -> Weld:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Weld() As Weld
                |     Gets the annotation on the Weld interface. 

        :return: Weld
        """
        return Weld(self.com_object.Weld())

    def __repr__(self):
        return f'Annotation2(name="{ self.name }")'
