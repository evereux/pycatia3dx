"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.factory import Factory
from pycatia3dx.tps.annotation import Annotation
from pycatia3dx.tps.noa import Noa
from pycatia3dx.tps.user_surface import UserSurface
from pycatia3dx.types.general import CATVariant


class AnnotationFactory(Factory):

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
                |                         AnnotationFactory
                | 
                | Interface for the TPS Factory.
                | This factory is implemented on the Set object. All the created specifications
                | are added to the Set from which this interface is retrieved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_datum(self, i_surf: UserSurface) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDatum(UserSurface iSurf) As Annotation
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
        :return: Annotation
        """
        return Annotation(self.com_object.CreateDatum(i_surf.com_object))

    def create_datum_reference_frame(self) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDatumReferenceFrame() As Annotation
                |     Create a Reference Frame (DRF). iType = 1 : Straightness 2 : AxisStraightness 3 : Flatness 4 : Circularity 5 : Cylindricity 6 : ProfileOfALine 7 : ProfileOfASurface 8 : Position

        :return: Annotation
        """
        return Annotation(self.com_object.CreateDatumReferenceFrame())

    def create_datum_target(self, i_surf: UserSurface, i_datum: Annotation) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateDatumTarget(UserSurface iSurf,Annotation iDatum) As
                | Annotation
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
        :param Annotation i_datum:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateDatumTarget(i_surf.com_object, i_datum.com_object))

    def create_evoluate_datum(self, i_surf: UserSurface, i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateEvoluateDatum(UserSurface iSurf,double iX,double iY,double
                | iZ,boolean iWithLeader) As Annotation
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
        :return: Annotation
        """
        return Annotation(self.com_object.CreateEvoluateDatum(i_surf.com_object, i_x, i_y, i_z, i_with_leader))

    def create_evoluate_text(self, i_surf: UserSurface, i_x: float, i_y: float, i_z: float, i_with_leader: bool) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateEvoluateText(UserSurface iSurf,double iX,double iY,double iZ,boolean
                | iWithLeader) As Annotation
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
        :return: Annotation
        """
        return Annotation(self.com_object.CreateEvoluateText(i_surf.com_object, i_x, i_y, i_z, i_with_leader))

    def create_flag_note(self, i_surf: UserSurface) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateFlagNote(UserSurface iSurf) As Annotation
                |     Create a FlagNote.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Flag Note. 
                |         oFlagNote
                |             The new created Flag Note.

        :param UserSurface i_surf:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateFlagNote(i_surf.com_object))

    def create_non_semantic_dimension(self, i_surf: UserSurface, i_type: CATVariant, i_sub_type: CATVariant) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateNonSemanticDimension(UserSurface iSurf,CATVariant iType,CATVariant
                | iSubType) As Annotation
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
        :return: Annotation
        """
        return Annotation(self.com_object.CreateNonSemanticDimension(i_surf.com_object, i_type, i_sub_type))

    def create_roughness(self, i_surf: UserSurface) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateRoughness(UserSurface iSurf) As Annotation
                |     Create a Roughness.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Roughness. 
                |         oRoughness
                |             The new created Roughness.

        :param UserSurface i_surf:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateRoughness(i_surf.com_object))

    def create_semantic_dimension(self, i_surf: UserSurface, i_type: CATVariant, i_sub_type: CATVariant) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSemanticDimension(UserSurface iSurf,CATVariant iType,CATVariant
                | iSubType) As Annotation
                |     Creates a semantic Dimension specification.
                | 
                |     Parameters:
                | 
                |         oDimension
                |             The new created Dimension.

        :param UserSurface i_surf:
        :param CATVariant i_type:
        :param CATVariant i_sub_type:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateSemanticDimension(i_surf.com_object, i_type, i_sub_type))

    def create_text(self, i_surf: UserSurface) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateText(UserSurface iSurf) As Annotation
                |     Create a Text.
                | 
                |     Parameters:
                | 
                |         iSurf
                |             User surface needed to construct the Text. 
                |         oText
                |             The new created Text.

        :param UserSurface i_surf:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateText(i_surf.com_object))

    def create_text_noa(self, i_surf: UserSurface) -> Noa:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTextNOA(UserSurface iSurf) As Noa
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
        :return: Noa
        """
        return Noa(self.com_object.CreateTextNOA(i_surf.com_object))

    def create_text_note_object_attribute(self, i_surf: UserSurface, i_noa_type: str) -> Noa:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTextNoteObjectAttribute(UserSurface iSurf,CATBSTR iNOAType) As
                | Noa
                |     Create a "Text" NOA (Note Object Attribute)
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
        :return: Noa
        """
        return Noa(self.com_object.CreateTextNoteObjectAttribute(i_surf.com_object, i_noa_type))

    def create_text_on_annot(self, i_text: str, i_annot: Annotation) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTextOnAnnot(CATBSTR iText,Annotation iAnnot) As
                | Annotation
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
        :param Annotation i_annot:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateTextOnAnnot(i_text, i_annot.com_object))

    def create_tolerance_with_drf(self, i_index: CATVariant, i_surf: UserSurface, i_drf: Annotation) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateToleranceWithDRF(CATVariant iIndex,UserSurface iSurf,Annotation
                | iDRF) As Annotation
                |     Create a Tolerance With a Reference Frame DRF. iType = 1 : Angularity

        :param CATVariant i_index:
        :param UserSurface i_surf:
        :param Annotation i_drf:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateToleranceWithDRF(i_index, i_surf.com_object, i_drf.com_object))

    def create_tolerance_without_drf(self, i_index: CATVariant, i_surf: UserSurface) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateToleranceWithoutDRF(CATVariant iIndex,UserSurface iSurf) As
                | Annotation
                |     Create a Tolerance Without a Reference Frame (DRF). iType = 1 : Straightness 2 : AxisStraightness 3 : Flatness 4 : Circularity 5 : Cylindricity 6 : ProfileOfALine 7 : ProfileOfASurface 8 : Position

        :param CATVariant i_index:
        :param UserSurface i_surf:
        :return: Annotation
        """
        return Annotation(self.com_object.CreateToleranceWithoutDRF(i_index, i_surf.com_object))

    def instanciate_noa(self, i_noa: Noa, i_surf: UserSurface) -> Annotation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func InstanciateNOA(Noa iNoa,UserSurface iSurf) As Annotation
                |     Instanciate an NOA from a Reference NOA.
                | 
                |     Parameters:
                | 
                |         iNOA
                |             Reference NOA. 
                |         iSurf
                |             User surface needed to construct the Dimension. 
                |         oNOA
                |             The new instantiated NOA.

        :param Noa i_noa:
        :param UserSurface i_surf:
        :return: Annotation
        """
        return Annotation(self.com_object.InstanciateNOA(i_noa.com_object, i_surf.com_object))

    def __repr__(self):
        return f'AnnotationFactory(name="{ self.name }")'
