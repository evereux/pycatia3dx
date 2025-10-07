"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.drafting.drawing_component import DrawingComponent
from pycatia3dx.mmr_automation_interfaces.factory import Factory
from pycatia3dx.tps.annotation_2 import Annotation2
from pycatia3dx.tps.user_surface import UserSurface
from pycatia3dx.types.general import CATVariant


class AnnotationFactory2(Factory):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Factory
                |                         AnnotationFactory2
                | 
                | Interface for the TPS Factory.
                | This factory is implemented on the Set object. All the created specifications
                | are added to the Set from which this interface is retrieved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_coord_dimension(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateCoordDimension(UserSurface iSurf) As Annotation2
                |     Create a Coordinate Dimension
                | 
                |     Parameters:
                | 
                |         iSurf
                |             The user surface on which you apply the new Coordinate Dimension.
                |             
                |         oCoorddimension
                |             The new created Coordinate dimension Feature.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateCoordDimension(i_surf.com_object))

    def create_datum(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDatum(UserSurface iSurf) As Annotation2
                |     Create a Datum Feature.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Datum Feature.
                |             
                |         oDatum
                |             The new created Datum Feature.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateDatum(i_surf.com_object))

    def create_datum_reference_frame(self) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDatumReferenceFrame() As Annotation2
                |     Create a Reference Frame (DRF). iType = 1 : Straightness 2 : AxisStraightness 3 : Flatness 4 : Circularity 5 : Cylindricity 6 : ProfileOfALine 7 : ProfileOfASurface 8 : Position

        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateDatumReferenceFrame())

    def create_datum_target(self, i_surf: UserSurface, i_datum: Annotation2) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDatumTarget(UserSurface iSurf,Annotation2 iDatum) As
                | Annotation2
                |     Create a Datum Target.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Datum Target.
                |             
                |         iDatum
                |             Datume Feature that is in relatino with the Datum Target.
                |             
                |         oDatum
                |             The new created Datum Target.

        :param UserSurface i_surf:
        :param Annotation2 i_datum:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateDatumTarget(i_surf.com_object, i_datum.com_object))

    def create_ditto_noa(self, i_surf: UserSurface, i_noa_type: str, i_ditto: DrawingComponent, i_stick_to_geometry_option: bool) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDittoNOA(UserSurface iSurf,CATBSTR iNOAType,DrawingComponent
                | iDitto,boolean iStickToGeometryOption) As Annotation2
                |     Create a "Ditto" NOA
                | 
                |     Parameters:
                | 
                |         iSurf
                |             The user surface on which you apply the created NOA.
                |             
                |         iNOAType
                |             Type of the created NOA; this string defines the Type of Noa. This
                |             type can be filtered using the Filter command. 
                |         iDitto
                |             The drawing component selected to provide NOA display.
                |             
                |         iStickToGeometryOption
                |             This flag is TRUE to tell the factory that Stick Ditto
                |             perpendicularly to geometry option is selected. In this case, the ditto is
                |             instantiated without frame or leader and its origin point is stuck and set on
                |             the selected geometry. In addition, the default anchor point position is the
                |             middle center. This argument is to be set to FALSE if leader attachment to
                |             point out geometry is expected. 
                |         oNoa
                |             The new created NOA.

        :param UserSurface i_surf:
        :param str i_noa_type:
        :param DrawingComponent i_ditto:
        :param bool i_stick_to_geometry_option:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateDittoNOA(i_surf.com_object, i_noa_type, i_ditto.com_object, i_stick_to_geometry_option))

    def create_evoluate_datum(self, i_surf: UserSurface, i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateEvoluateDatum(UserSurface iSurf,double iX,double iY,double
                | iZ,boolean iWithLeader) As Annotation2
                |     Create a Datum Feature.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Datum Feature.
                |             
                |         iX
                |             X coordinate. 
                |         iY
                |             Y coordinate. 
                |         iZ
                |             Z coordinate. 
                |         iWithLeader
                |             Create or not a leader on the annotation. If the leader is
                |             requested: The activated TPSView shall not be parallel to the surface pointed
                |             by the annotation Datum. If the activated TPSView is parallel to the surface
                |             pointed: - The leader will be disconnected - The extremity of the leader will
                |             be positioned at the origin of the part - The annotation Datum is created but
                |             its status will be KO. 
                |         oDatum
                |             The new created Datum Feature.

        :param UserSurface i_surf:
        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param bool i_with_leader:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateEvoluateDatum(i_surf.com_object, i_x, i_y, i_z, i_with_leader))

    def create_evoluate_text(self, i_surf: UserSurface, i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateEvoluateText(UserSurface iSurf,double iX,double iY,double iZ,boolean
                | iWithLeader) As Annotation2
                |     Create a Text.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Text. 
                |         iX
                |             X coordinate. 
                |         iY
                |             Y coordinate. 
                |         iZ
                |             Z coordinate. 
                |         iWithLeader
                |             Create or not a leader on the annotation. If the leader is
                |             requested: The activated TPSView shall not be parallel to the surface pointed
                |             by the annotation Text. If the activated TPSView is parallel to the surface
                |             pointed: - The leader will be disconnected - The extremity of the leader will
                |             be positioned at the origin of the part - The annotation Text is created but
                |             its status will be KO. 
                |         oText
                |             The new created Text.

        :param UserSurface i_surf:
        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param bool i_with_leader:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateEvoluateText(i_surf.com_object, i_x, i_y, i_z, i_with_leader))

    def create_flag_note(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateFlagNote(UserSurface iSurf) As Annotation2
                |     Create a FlagNote.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Flag Note. 
                |         oFlagNote
                |             The new created Flag Note.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateFlagNote(i_surf.com_object))

    def create_gdt(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateGDT(UserSurface iSurf) As Annotation2
                |     Create a GDT
                | 
                |     Parameters:
                | 
                |         iSurf
                |             The user surface on which you apply the new GDT. 
                |         oGDT
                |             The new created GDT Feature.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateGDT(i_surf.com_object))

    def create_non_semantic_dimension(self, i_surf: UserSurface, i_type: CATVariant, i_sub_type: CATVariant) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateNonSemanticDimension(UserSurface iSurf,CATVariant iType,CATVariant
                | iSubType) As Annotation2
                |     Creates a non semantic Dimension specification.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Dimension. 
                |         iSubType
                |             : 1 CATTPSDiameterDimension 2 CATTPSRadiusDimension 
                |         iType
                |             : 1 Linear Dimension 2 Angular Dimension 3 Second Linear Dim (Small diameter/radius for torus) 
                |         oDimension
                |             The new created Dimension.

        :param UserSurface i_surf:
        :param CATVariant i_type:
        :param CATVariant i_sub_type:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateNonSemanticDimension(i_surf.com_object, i_type, i_sub_type))

    def create_roughness(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRoughness(UserSurface iSurf) As Annotation2
                |     Create a Roughness.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Roughness. 
                |         oRoughness
                |             The new created Roughness.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateRoughness(i_surf.com_object))

    def create_semantic_dimension(self, i_surf: UserSurface, i_type: CATVariant, i_sub_type: CATVariant) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSemanticDimension(UserSurface iSurf,CATVariant iType,CATVariant
                | iSubType) As Annotation2
                |     Creates a semantic Dimension specification.
                | 
                |     Parameters:
                | 
                |         oDimension
                |             The new created Dimension.

        :param UserSurface i_surf:
        :param CATVariant i_type:
        :param CATVariant i_sub_type:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateSemanticDimension(i_surf.com_object, i_type, i_sub_type))

    def create_text(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateText(UserSurface iSurf) As Annotation2
                |     Create a Text.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Text. 
                |         oText
                |             The new created Text.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateText(i_surf.com_object))

    def create_text_noa(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTextNOA(UserSurface iSurf) As Annotation2
                |     Create a "Text" NOA
                | 
                |     Parameters:
                | 
                |         iSurf
                |             The user surface on which you apply the created NOA.
                |             
                |         oNoa
                |             The new created NOA.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateTextNOA(i_surf.com_object))

    def create_text_note_object_attribute(self, i_surf: UserSurface, i_noa_type: str) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTextNoteObjectAttribute(UserSurface iSurf,CATBSTR iNOAType) As
                | Annotation2
                |     Create a "Text" NOA
                | 
                |     Parameters:
                | 
                |         iSurf
                |             The user surface on which you apply the created NOA.
                |             
                |         iNOAType
                |             Type of the created NOA; this string defines the Type of Noa. This
                |             type can be filtered using the Filter command. 
                |         oNoa
                |             The new created NOA.

        :param UserSurface i_surf:
        :param str i_noa_type:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateTextNoteObjectAttribute(i_surf.com_object, i_noa_type))

    def create_text_on_annot(self, i_text: str, i_annot: Annotation2) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTextOnAnnot(CATBSTR iText,Annotation2 iAnnot) As
                | Annotation2
                |     Create a Text grouped to an annotation.
                | 
                |     Parameters:
                | 
                |         iText
                |             Character string that makes up the text. 
                |         iAnnot
                |             Annotation reference needed to group the Text. 
                |         oText
                |             The new created Text.

        :param str i_text:
        :param Annotation2 i_annot:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateTextOnAnnot(i_text, i_annot.com_object))

    def create_tolerance_with_drf(self, i_index: CATVariant, i_surf: UserSurface, i_drf: Annotation2) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateToleranceWithDRF(CATVariant iIndex,UserSurface iSurf,Annotation2
                | iDRF) As Annotation2
                |     Create a Tolerance With a Reference Frame DRF. iType = 1 : Angularity

        :param CATVariant i_index:
        :param UserSurface i_surf:
        :param Annotation2 i_drf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateToleranceWithDRF(i_index, i_surf.com_object, i_drf.com_object))

    def create_tolerance_without_drf(self, i_index: CATVariant, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateToleranceWithoutDRF(CATVariant iIndex,UserSurface iSurf) As
                | Annotation2
                |     Create a Tolerance Without a Reference Frame (DRF). iType = 1 : Straightness 2 : AxisStraightness 3 : Flatness 4 : Circularity 5 : Cylindricity 6 : ProfileOfALine 7 : ProfileOfASurface 8 : Position

        :param CATVariant i_index:
        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateToleranceWithoutDRF(i_index, i_surf.com_object))

    def create_weld(self, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateWeld(UserSurface iSurf) As Annotation2
                |     Create a Weld
                | 
                |     Parameters:
                | 
                |         iSurf
                |             The user surface on which you apply the new Weld. 
                |         oWeld
                |             The new created Weld Feature.

        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.CreateWeld(i_surf.com_object))

    def instanciate_noa(self, i_noa: Annotation2, i_surf: UserSurface) -> Annotation2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func InstanciateNOA(Annotation2 iNoa,UserSurface iSurf) As
                | Annotation2
                |     Instanciate an NOA from a Reference NOA.
                | 
                |     Parameters:
                | 
                |         iNOA
                |             Reference NOA. 
                |         iSurf
                |             User surface needed to construct the Dimension. 
                |         oNOA
                |             The new instanciated NOA. 

        :param Annotation2 i_noa:
        :param UserSurface i_surf:
        :return: Annotation2
        """
        return Annotation2(self.com_object.InstanciateNOA(i_noa.com_object, i_surf.com_object))

    def __repr__(self):
        return f'AnnotationFactory2(name="{ self.name }")'
