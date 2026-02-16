"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.annotation_factory import AnnotationFactory
from pycatia3dx.tps.annotation_factory_2 import AnnotationFactory2
from pycatia3dx.tps.annotations import Annotations
from pycatia3dx.tps.capture_factory import CaptureFactory
from pycatia3dx.tps.captures import Captures
from pycatia3dx.tps.tps_hyper_links_manager import TPSHyperLinksManager
from pycatia3dx.tps.tps_view import TPSView
from pycatia3dx.tps.tps_view_factory import TPSViewFactory
from pycatia3dx.tps.tps_views import TPSViews


class AnnotationSet(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnnotationSet
                | 
                | Interface for the TPS Set of objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_view(self) -> TPSView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveView() As TPSView
                |     Gets or Sets Annotation Set ActiveView.
                | 
                |     Parameters:
                | 
                |         oView
                |             Value of CATIATPSView.

        :return: TpsView
        """

        return TPSView(self.com_object.ActiveView)

    @active_view.setter
    def active_view(self, value: TPSView):
        """
        :param TPSView value:
        """

        self.com_object.ActiveView = value

    @property
    def an_empty_annotations_list(self) -> Annotations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnEmptyAnnotationsList() As Annotations (Read Only)
                |     Retrieves an empty Annotations'Collection.
                | 
                |     Parameters:
                | 
                |         oAnnots
                |             Empty Annotations' Collection.

        :return: Annotations
        """

        return Annotations(self.com_object.AnEmptyAnnotationsList)

    @property
    def annotation_factory(self) -> AnnotationFactory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnnotationFactory() As AnnotationFactory (Read Only)
                |     Gets the factory to create annotations.
                | 
                |     Parameters:
                | 
                |         oAFact
                |             Annotations' factory. Deprecated method: AnnotationFactory method
                |             is replaced by AnnotationFactory2 has.

        :return: AnnotationFactory
        """

        return AnnotationFactory(self.com_object.AnnotationFactory)

    @property
    def annotation_factory2(self) -> AnnotationFactory2:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnnotationFactory2() As AnnotationFactory2 (Read
                | Only)
                |     Gets the factory to create annotations.
                | 
                |     Parameters:
                | 
                |         oAFact
                |             Annotations' factory.

        :return: AnnotationFactory2
        """

        return AnnotationFactory2(self.com_object.AnnotationFactory2)

    @property
    def annotation_set_pupose(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnnotationSetPupose() As CATBSTR (Read Only)
                |     Gets the annotation Set specifications purpose.
                |     Any existing set is implicitly an Engineering Annotation
                |     Set.
                | 
                |     Parameters:
                | 
                |         oAnnotationSetSpecification
                |             Value indicating purpose of the Annotation Set.
                |             List of legal values:
                |             oAnnotationSetSpecification = "FTA_EngineeringSet",
                |             oAnnotationSetSpecification = "FTA_ManufacturingSet".

        :return: str
        """

        return self.com_object.AnnotationSetPupose

    @property
    def annotation_set_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnnotationSetType() As CatAnnotationSetType (Read
                | Only)
                |     Gets the annotation Set type.
                | 
                |     Parameters:
                | 
                |         oAnnotationSetType
                |             Value of Set Type.

        :return: CatAnnotationSetType
        """

        return self.com_object.AnnotationSetType

    @property
    def annotations(self) -> Annotations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Annotations() As Annotations (Read Only)
                |     Retrieves the TPS components of the set.
                | 
                |     Parameters:
                | 
                |         oAnnots
                |             Collection of returned component.

        :return: Annotations
        """

        return Annotations(self.com_object.Annotations)

    @property
    def capture_factory(self) -> CaptureFactory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CaptureFactory() As CaptureFactory (Read Only)
                |     Gets the factory to create Capture.
                | 
                |     Parameters:
                | 
                |         opiCapFact
                |             Capture factory.

        :return: CaptureFactory
        """

        return CaptureFactory(self.com_object.CaptureFactory)

    @property
    def captures(self) -> Captures:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Captures() As Captures (Read Only)
                |     Retrieves all the Captures that belong to the set.
                | 
                |     Parameters:
                | 
                |         oCaptures
                |             Collection of returned Captures.

        :return: Captures
        """

        return Captures(self.com_object.Captures)

    @property
    def kind_of_set(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KindOfSet() As CATBSTR (Read Only)
                |     Gives the kind of set (Part, Product...).
                | 
                |     Parameters:
                | 
                |         oKindOfSet
                |             It could be : Part Product Product_TP Process_BB Cgr Cgr_TP.

        :return: str
        """

        return self.com_object.KindOfSet

    @property
    def standard(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Standard() As CATBSTR (Read Only)
                |     Retrieves the Parent Standard defined at set creation.
                | 
                |     Parameters:
                | 
                |         oStandard
                |             Name of the Parent Standard applied for all TPS in the set. The
                |             Parent Standard is the international standard on which Standard File is based
                |             on. It can only be ISO, ANSI and JIS (ANSI stands for ASME).

        :return: str
        """

        return self.com_object.Standard

    @property
    def switch_on(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SwitchOn() As boolean
                |     Gets or Sets Annotation Set Visualization.
                | 
                |     Parameters:
                | 
                |         oDisplay
                |             Value of visualisation mode.

        :return: bool
        """

        return self.com_object.SwitchOn

    @switch_on.setter
    def switch_on(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SwitchOn = value

    @property
    def tps_view_factory(self) -> TPSViewFactory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TPSViewFactory() As TPSViewFactory (Read Only)
                |     Gets the factory to create TPS Views.
                | 
                |     Parameters:
                | 
                |         oTPSViewFact
                |             TPS Views' factory.

        :return: TpsViewFactory
        """

        return TPSViewFactory(self.com_object.TPSViewFactory)

    @property
    def tps_views(self) -> TPSViews:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TPSViews() As TPSViews (Read Only)
                |     Retrieves all the TPSViews that belong to the set.
                | 
                |     Parameters:
                | 
                |         oViews
                |             Collection of returned views.

        :return: TpsViews
        """

        return TPSViews(self.com_object.TPSViews)

    def apply_result_with_link_when_copy_set_to(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ApplyResultWithLinkWhenCopySetTo()
                |     Registers for next call to either GlobalCopySetTo and
                |     LogicalGlobalCopySetTo like methods. AnnotationSet.GlobalCopySetTo or
                |     AnnotationSet.LogicalGlobalCopySetTo and their derivatives. Those routines are
                |     used to import annotations in target set located in 3D Shape Representation
                |     usually given by ipiTarget3DSR argument. Incidence of this procedure is about
                |     instanciated annotations: they are copied as result annotations with link to
                |     the corresponding source annotations. This call sets an option valid for the
                |     next import run only; in other words, this option is reset at the end of
                |     import. When activated, the annotations are copied as result with link
                |     annotations.
                | 
                |     Example:
                | 
                |          This example illustrates activation of the 'as result with link'
                |          option for the next import (GlobalCopySetTo) run. 
                | 
                |          Dim myPart As Part
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim mySelection As Selection
                |          Set mySelection = CATIA.ActiveEditor.Selection
                |          Dim SelectionFilter(0)
                |          SelectionFilter(0)="AnnotationSet"
                |          Dim Status As String
                |          Status = mySelection.SelectElement2(SelectionFilter, "Select an Annotation Set to copy: ", False)
                |          Dim SelectedEntity As SelectedElement
                |          Set SelectedEntity = mySelection.Item( 1 )
                |          Dim SetToReplicate As AnnotationSet
                |          Set SetToReplicate = SelectedEntity.Value
                |          SetToReplicate.ApplyResultWithLinkWhenCopySetTo
                |          SetToReplicate.GlobalCopySetTo(myPart)

        :return: None
        """
        return self.com_object.ApplyResultWithLinkWhenCopySetTo()

    def apply_view_re_use_when_copy_set_to(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ApplyViewReUseWhenCopySetTo()
                |     Registers for next call to either GlobalCopySetTo and
                |     LogicalGlobalCopySetTo like methods. AnnotationSet.GlobalCopySetTo or
                |     AnnotationSet.LogicalGlobalCopySetTo and their derivatives. Those routines are
                |     used to import annotations in target set located in 3D Shape Representation
                |     usually given by ipiTarget3DSR argument. Incidence of this procedure is about
                |     instanciated annotations: as much as possible, they are placed in existing
                |     Views. This call sets an option valid for the next import run only; in other
                |     words, this option is reset at the end of import. When activated, this option
                |     will not break the import processing; if no View in target set can receive a
                |     candidate FTA entity resulting from the import, regular handling is carried on.

        :return: None
        """
        return self.com_object.ApplyViewReUseWhenCopySetTo()

    def global_copy_set_to(self, i_destination_part: Part) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GlobalCopySetTo(Part iDestinationPart) As CATBSTR
                |     Copies the entire or a subpart of a 3D Shape Representation level
                |     Annotation Set into a destination 3D Shape Representation.
                | 
                |     Parameters:
                | 
                |         iDestinationPart
                |             destination 3D Shape Representation. 
                |         oMessage
                |             result of datums merge.

        :param Part i_destination_part:
        :return: str
        """
        return self.com_object.GlobalCopySetTo(i_destination_part.com_object)

    def global_copy_set_to_with_filter(self, i_destination_part: Part, i_capture_filter_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GlobalCopySetToWithFilter(Part iDestinationPart,CATBSTR
                | iCaptureFilterName) As CATBSTR
                |     Copies the entire or a subpart of a 3D Shape Representation level
                |     Annotation Set into a destination 3D Shape Representation.
                | 
                |     Parameters:
                | 
                |         iDestinationPart
                |             destination 3D Shape Representation. 
                |         iCaptureFilterName
                |             String used to filter FTA features. The system keeps only the FTA
                |             features that belong to the captures FTA that contains the string.
                |             
                |         oMessage
                |             result of datums merge.

        :param Part i_destination_part:
        :param str i_capture_filter_name:
        :return: str
        """
        return self.com_object.GlobalCopySetToWithFilter(i_destination_part.com_object, i_capture_filter_name)

    def global_copy_set_to_with_filter_with_transformation(self, i_destination_part: Part, i_transfo: tuple,
                                                           i_capture_filter_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GlobalCopySetToWithFilterWithTransformation(Part
                | iDestinationPart,CATSafeArrayVariant iTransfo,CATBSTR iCaptureFilterName) As
                | CATBSTR
                |     Copies the entire or a subpart of a part level Annotation Set into a
                |     destination 3D Shape Representation.
                | 
                |     Parameters:
                | 
                |         iDestinationPart
                |             destination 3D Shape Representation. 
                |         iSymmetryPlane
                |             symmetry plane used to retrieve the geometrical elements pointed by
                |             the annotations. 
                |         iTransfo
                |             Optional argument. Transformation matrix to apply to FTA features
                |             during copy. The transformation is also used for retrieving in the destination
                |             3D Shape Representation the geometrical elements the FTA features are rerouted
                |             on.
                |             Transformation matrix is composed by a matrix3x3 and a translation
                |             vector:
                |             [[a11 a12 a13
                |             a21 a22 a23
                |             a31 a32 a33]
                |             [u1 u2 u3]]
                | 
                |             a11 is in iTransfo(0)
                |             a12 is in iTransfo(1)
                |             a13 is in iTransfo(2)
                |             a21 is in iTransfo(3)
                |             a22 is in iTransfo(4)
                |             a23 is in iTransfo(5)
                |             a31 is in iTransfo(6)
                |             a32 is in iTransfo(7)
                |             a33 is in iTransfo(8)
                |             u1 is in iTransfo(9)
                |             u2 is in iTransfo(10)
                |             u3 is in iTransfo(11) 
                |         iCaptureFilterName
                |             String used to filter FTA features. The system keeps only the FTA
                |             features that belong to the captures FTA that contain the string.
                |             
                |         oMessage
                |             result of datums merge.

        :param Part i_destination_part:
        :param tuple i_transfo:
        :param str i_capture_filter_name:
        :return: str
        """
        return self.com_object.GlobalCopySetToWithFilterWithTransformation(i_destination_part.com_object, i_transfo,
                                                                           i_capture_filter_name)

    def global_copy_set_to_with_transformation(self, i_destination_part: Part, i_transfo: tuple) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GlobalCopySetToWithTransformation(Part
                | iDestinationPart,CATSafeArrayVariant iTransfo) As CATBSTR
                |     Copies the entire Annotation Set into a destination 3D Shape
                |     Representation.
                | 
                |     Parameters:
                | 
                |         iDestinationPart
                |             destination 3D Shape Representation. 
                |         iTransfo
                |             Optional argument. Transformation matrix to apply to FTA features
                |             during copy. The transformation is also used for retrieving in the destination
                |             3D Shape Representation the geometrical elements the FTA features are rerouted
                |             on.
                |             Transformation matrix is composed by a matrix3x3 and a translation
                |             vector:
                |             [[a11 a12 a13
                |             a21 a22 a23
                |             a31 a32 a33]
                |             [u1 u2 u3]]
                | 
                |             a11 is in iTransfo(0)
                |             a12 is in iTransfo(1)
                |             a13 is in iTransfo(2)
                |             a21 is in iTransfo(3)
                |             a22 is in iTransfo(4)
                |             a23 is in iTransfo(5)
                |             a31 is in iTransfo(6)
                |             a32 is in iTransfo(7)
                |             a33 is in iTransfo(8)
                |             u1 is in iTransfo(9)
                |             u2 is in iTransfo(10)
                |             u3 is in iTransfo(11) 
                |         oMessage
                |             result of datums merge.

        :param Part i_destination_part:
        :param tuple i_transfo:
        :return: str
        """
        return self.com_object.GlobalCopySetToWithTransformation(i_destination_part.com_object, i_transfo)

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

    def isolate_links_of_noa(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsolateLinksOfNOA()
                |     Removes all the links in between ditto NOA and the 2D instantiated Detail.
                |     This call focuses the remaining link in between the ditto NOA and the 2D
                |     Drafting component used for its representation. The handling is global to the
                |     authored content and results in isolating all the existing ditto NOAs.

        :return: None
        """
        return self.com_object.IsolateLinksOfNOA()

    def logical_global_copy_set_to(self, ipi_target3_dsr: Part, i_list_of_bodies_and_geometrical_sets: tuple,
                                   ib_import_once: bool) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func LogicalGlobalCopySetTo(Part ipiTarget3DSR,CATSafeArrayVariant
                | iListOfBodiesAndGeometricalSets,boolean ibImportOnce) As
                | CATBSTR
                |     Copies the entire or a subpart of an Annotation Set into a target 3D Shape
                |     Representation using logical reroute.
                | 
                |     Parameters:
                | 
                |         ipiTarget3DSR
                |             target 3D Shape Representation. 
                |         iListOfBodiesAndGeometricalSets
                |             List of bodies and geometrical sets on which the reroute of the FTA
                |             features will apply. If this list is empty, the system uses all the bodies and
                |             geometrical sets of the ipiTarget3DSR to reroute the copied FTA features.
                |             
                |         ibImportOnce
                |             TRUE if the system launches one import which is applied on all the
                |             bodies and geometrical sets of the previous list
                |             iListOfBodiesAndGeometricalSets. FALSE if the system launches 1 import per body
                |             and geometrical set of the previous list iListOfBodiesAndGeometricalSets. In
                |             this case the reroute of FTA features is done on the current body or
                |             geometrical set. 
                |         oMessage
                |             result of datums merge.

        :param Part ipi_target3_dsr:
        :param tuple i_list_of_bodies_and_geometrical_sets:
        :param bool ib_import_once:
        :return: str
        """
        return self.com_object.LogicalGlobalCopySetTo(ipi_target3_dsr.com_object, i_list_of_bodies_and_geometrical_sets,
                                                      ib_import_once)

    def logical_global_copy_set_to_with_filter(self, ipi_target3_dsr: Part,
                                               i_list_of_bodies_and_geometrical_sets: tuple, ib_import_once: bool,
                                               i_capture_filter_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func LogicalGlobalCopySetToWithFilter(Part ipiTarget3DSR,CATSafeArrayVariant
                | iListOfBodiesAndGeometricalSets,boolean ibImportOnce,CATBSTR
                | iCaptureFilterName) As CATBSTR
                |     Copies the entire or a subpart of an Annotation Set into a target 3D Shape
                |     Representation using logical reroute.
                | 
                |     Parameters:
                | 
                |         ipiTarget3DSR
                |             target 3D Shape Representation. 
                |         iListOfBodiesAndGeometricalSets
                |             List of bodies and geometrical sets on which the reroute of the FTA
                |             features will apply. If this list is empty, the system uses all the bodies and
                |             geometrical sets of the ipiTarget3DSR to reroute the copied FTA features.
                |             
                |         ibImportOnce
                |             TRUE if the system launches one import which is applied on all the
                |             bodies and geometrical sets of the previous list
                |             iListOfBodiesAndGeometricalSets. FALSE if the system launches 1 import per body
                |             and geometrical set of the previous list iListOfBodiesAndGeometricalSets. In
                |             this case the reroute of FTA features is done on the current body or
                |             geometrical set. 
                |         iCaptureFilterName
                |             String used to filter FTA features. The system keeps only the FTA
                |             features that belong to the captures FTA that contain the string.
                |             
                |         oMessage
                |             result of datums merge.

        :param Part ipi_target3_dsr:
        :param tuple i_list_of_bodies_and_geometrical_sets:
        :param bool ib_import_once:
        :param str i_capture_filter_name:
        :return: str
        """
        return self.com_object.LogicalGlobalCopySetToWithFilter(ipi_target3_dsr.com_object,
                                                                i_list_of_bodies_and_geometrical_sets, ib_import_once,
                                                                i_capture_filter_name)

    def read_iso_default_properties(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func ReadISODefaultProperties(CATSafeArrayVariant oISODefaults) As
                | long
                |     Retrieves the ISO 14405 and ISO 1101 default specifications. This method is
                |     not relevant in case of ASME Standard.
                |
                |     Parameters:
                |
                |         oISODefaults
                |             Array of ISO default defined onto the annotation set. Composition
                |             of the array may looks like the following schema
                |             [ Linear size ISO 14405 property
                |             Angular size ISO 14405 property
                |             Default specification elements for form association
                |             property
                |             Default specification elements for toleranced feature filtering
                |             property ]
                |             When oCount is not null, minimal size of oISODefaults "vector" of
                |             string is 3 (the 3 first strings are always existing); depending on GDT
                |             toleranced feature filtering options activated on the annotation set, oCount
                |             may reach the limit of 7 (4 more texts).
                |         oCount
                |             Number of lines in returned array of strings. When this procedure
                |             is not applicable (either due to wrong Standard, old annotation set), oCount
                |             equals 0.

        :return: tuple
        """
        return self.com_object.ReadISODefaultProperties(o_iso_defaults)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'read_iso_default_properties'
        # vba_code = """
        # Public Function read_iso_default_properties(annotation_set)
        #     Dim oISODefaults (2)
        #     annotation_set.ReadISODefaultProperties oISODefaults
        #     read_iso_default_properties = oISODefaults
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def repair_delete_invalid_fta_features(self, options_to_repair_delete: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RepairDeleteInvalidFTAFeatures(long OptionsToRepairDelete)
                |     Repairs Deletes invalid FTA features.
                | 
                |     Parameters:
                | 
                |         OptionsToRepairDelete
                |             Repair and Delete options. For the available values
                |             RepairDeleteOptionFTAFeatures these options must be combined using the
                |             different values of typedef RepairDeleteOptionFTAFeatures. The operations
                |             associated to these options must be launched in the order given by the list of
                |             RepairDeleteOptionFTAFeatures whatever the order of options given in arguments
                |             of this method. The options order given by the list of
                |             RepairDeleteOptionFTAFeatures is the same as the order of options into the
                |             interactive panel of command "Repair/Delete Invalid FTA
                |             Features".
                |             The options order:
                |             RepairDeleteOptionFTAFeatures_RepairUserSurfaceGeometricComponents
                |             RepairDeleteOptionFTAFeatures_RepairGroupOfSurfacesComponents
                |             RepairDeleteOptionFTAFeatures_DeleteInvalidFTAHavingAllLinksBroken
                |             RepairDeleteOptionFTAFeatures_DeleteInvalidFTAHavingAtLeast1BrokenLink
                |             RepairDeleteOptionFTAFeatures_DeleteAllInvalidFTA
                | 
                |     Returns:
                |         S_OK when SUCCEEDED.
                |         E_INVALIDARG if there is no option selected.
                |         E_FAIL otherwise. 

        :param int options_to_repair_delete:
        :return: None
        """
        return self.com_object.RepairDeleteInvalidFTAFeatures(options_to_repair_delete)

    def __repr__(self):
        return f'AnnotationSet(name="{self.name}")'
