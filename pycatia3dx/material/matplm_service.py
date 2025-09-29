"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.interfaces.service import Service
from pycatia3dx.material.applied_material import AppliedMaterial
from pycatia3dx.material.applied_materials import AppliedMaterials
from pycatia3dx.material.material_generic import MaterialGeneric
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection


class MatplmService(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         MATPLMService
                | 
                | Interface representing the PLMNew service.
                | It can be retrieves using the
                | Application.GetSessionService("MATPLMService")
                | Role: provides the services to create and edit in authoring session a new PLM
                | entity. In case this material is not granted the PLMCreate method of the
                | interface fails. The data are created in the default authoring customization
                | domain (environment).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_material_core(
            self,
            i_support: AnyObject,
            o_core_material: MaterialGeneric,
            o_core_applied_material: AppliedMaterial
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetMaterialCore(AnyObject iSupport,MaterialGeneric
                | oCoreMaterial,AppliedMaterial oCoreAppliedMaterial)
                |     Method which allows to get the core material applied on the provided
                |     support or inherited from an upper support in the same
                |     context.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             Defines the support and its context. When the support (target of
                |             CATOmbObjectInContext) is an element inside a RepReference, a RepInstance must
                |             be defined 
                |         oCoreMaterial
                |             The returned material reference. 
                |         oCoreAppliedMaterial
                |             The returned applied-material. 
                | 
                |     Example:
                | 
                |          This example shows you how to retrieve the core material applied on
                |          the provided support
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Set MatService = CATIA.GetSessionService("MATPLMService")
                |            Dim oCoreMatRef As Material
                |            Dim oCoreMatCnx As AppliedMaterial
                |            ...
                |            Dim MyLinkRootOccRepInsFeat As AnyObject
                |            Set MyLinkRootOccRepInsFeat = MyContext.ComposeLink(oRootOcc, MyPartInstance, MyReference)
                |            MatService.GetMaterialCore MyLinkRootOccRepInsFeat, oCoreMatRef,
                |            oCoreMatCnx

        :param AnyObject i_support:
        :param MaterialGeneric o_core_material:
        :param AppliedMaterial o_core_applied_material:
        :return: None
        """
        return self.com_object.GetMaterialCore(
            i_support.com_object,
            o_core_material.com_object,
            o_core_applied_material.com_object
        )

    def get_material_covering(
            self,
            i_support: AnyObject,
            o_list_covering_materials: Collection,
            o_covering_applied_materials: AppliedMaterials
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetMaterialCovering(AnyObject iSupport,Collection
                | oListCoveringMaterials,AppliedMaterials
                | oCoveringAppliedMaterials)
                |     Returns the list of covering materials applied on the support defined in
                |     iSupport. Only covering materials defined in the context of iSupport will be
                |     retrieved.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             Defines the support and its context. 
                |         oListCoveringMaterials
                |             The list of materials references First material in the list is the
                |             upper covering material layer. 
                |         oCoveringAppliedMaterials
                |             The returned applied-material lists. 
                | 
                |     Example:
                | 
                |          This example shows you how to retrieve the core material applied on
                |          the provided support
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Set MatService = CATIA.GetSessionService("MATPLMService")
                |            Dim oCoveringMatRef As Object
                |            Dim oCoveringMatCnx As AppliedMaterials
                |            ...
                |            Dim MyLinkRootOccRepInsFeat As AnyObject
                |            Set MyLinkRootOccRepInsFeat = MyContext.ComposeLink(oRootOcc, MyPartInstance, MyReference)
                |            MatService.GetMaterialCovering MyLinkRootOccRepInsFeat,
                |            oCoveringMatRef, oCoveringMatCnx

        :param AnyObject i_support:
        :param Collection o_list_covering_materials:
        :param AppliedMaterials o_covering_applied_materials:
        :return: None
        """
        return self.com_object.GetMaterialCovering(
            i_support.com_object,
            o_list_covering_materials.com_object,
            o_covering_applied_materials.com_object
        )

    def get_materials_in_session(self, o_materials_in_session: Collection) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetMaterialsInSession(Collection oMaterialsInSession)
                |     Get all materials in session.
                | 
                |     Parameters:
                | 
                |         opiMaterialsInSession
                |             The list of all materials in session. 
                | 
                |     Example:
                | 
                |          This example shows you how to get all material in
                |          session.
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Dim ListMaterialInSession As Object
                |            ...
                |            MatService.GetMaterialsInSession
                |            ListMaterialInSession

        :param Collection o_materials_in_session:
        :return: None
        """
        return self.com_object.GetMaterialsInSession(o_materials_in_session.com_object)

    def load_materials(self, i_vpm_reference: AnyObject, i_recursive: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub LoadMaterials(AnyObject iVPMReference,boolean iRecursive)
                |     Load material attached to a given node.
                | 
                |     Parameters:
                | 
                |         Product
                |             Node (is a VPMreference). 
                |         Indicates
                |             whether the search has to be recursive or not. 
                | 
                |     Example:
                | 
                |          This example shows you how to get all material in
                |          session.
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Dim iVPMReference As CATIABase
                |            ...
                |            MatService.LoadMaterials iVPMReference,TRUE

        :param AnyObject i_vpm_reference:
        :param bool i_recursive:
        :return: None
        """
        return self.com_object.LoadMaterials(i_vpm_reference.com_object, i_recursive)

    def plm_create(self, i_user_type: str, o_plm_mat_entity: MaterialGeneric, o_editor: Editor) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub PLMCreate(CATBSTR iUserType,MaterialGeneric oPLMMatEntity,Editor
                | oEditor)
                |     Method which allows to create a new material reference.
                | 
                |     Parameters:
                | 
                |         iUserType
                |             The user discipline to identify the entity to
                |             create.
                |             Legal values: dsc_matref_ref_Covering: to create a Covering
                |             material, dsc_matref_ref_Core: to create a Core material,
                |             
                |         oPLMMatEntity
                |             The newly material created. 
                |         oEditor
                |             The resulting editor on the newly created data. 
                | 
                |     Example:
                | 
                |          This example shows you how to create a new material
                |          reference.
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Dim oMaterialEditor As Editor
                |            Dim oNewMaterialDomain As MaterialDomain
                |            Dim oNewCoveringMatRef As Material
                |            Set MatService = CATIA.GetSessionService("MATPLMService")
                |            ...
                |            MatService.PLMCreate "dsc_matref_ref_Covering", oNewCoveringMatRef,
                |            oMaterialEditor
                |            oNewCoveringMatRef.AddDomain "dsc_matref_rep_Rendering",
                |            oNewMaterialDomain

        :param str i_user_type:
        :param MaterialGeneric o_plm_mat_entity:
        :param Editor o_editor:
        :return: None
        """
        return self.com_object.PLMCreate(i_user_type, o_plm_mat_entity.com_object, o_editor.com_object)

    def remove_applied_material(self, i_applied_material: AppliedMaterial) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub RemoveAppliedMaterial(AppliedMaterial iAppliedMaterial)
                |     Removes applied material.
                | 
                |     Parameters:
                | 
                |         ipiAppliedMaterial
                |             Defines the applied material that will be removed.
                |             
                | 
                |     Example:
                | 
                |          This example shows you how to remove an applied
                |          material
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Dim oCoreMatCnx As AppliedMaterial
                |            ...
                |            MatService.RemoveAppliedMaterial oCoreMatCnx

        :param AppliedMaterial i_applied_material:
        :return: None
        """
        return self.com_object.RemoveAppliedMaterial(i_applied_material.com_object)

    def set_display_msg_box(self, ibool_display_msg_box: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetDisplayMsgBox(boolean iboolDisplayMsgBox)
                |     Allow to display or not a message Box when there is an
                |     error.
                | 
                |     Parameters:
                | 
                |         iboolDisplayMsgBox
                |             TRUE = display a message Box. FALSE = not display a message Box. 
                | 
                |     Example:
                | 
                |          This example shows you how to not display a message box when there is
                |          an error.
                |            
                | 
                |            Dim MatService As MATPLMService
                |            ...
                |            MatService.SetDisplayMsgBox FALSE

        :param bool ibool_display_msg_box:
        :return: None
        """
        return self.com_object.SetDisplayMsgBox(ibool_display_msg_box)

    def set_material_core(
            self,
            i_support: AnyObject,
            i_core_material: MaterialGeneric,
            o_core_applied_material: AppliedMaterial
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetMaterialCore(AnyObject iSupport,MaterialGeneric
                | iCoreMaterial,AppliedMaterial oCoreAppliedMaterial)
                |     Applies a core material on the support defined in iSupport. If a core
                |     material is already applied on that support, it is
                |     replaced.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             Defines the support and the context used for applying material. The
                |             context is the root reference defined by iSupport. If the support (target of
                |             iSupport) is an element inside a RepReference then a RepInstance must be
                |             provided in iSupport to make it valid. 
                |         iCoreMaterial
                |             The material reference to be applied on the support.
                |             
                |         oCoreAppliedMaterial
                |             The new applied material created. 
                | 
                |     Example:
                | 
                |          This example shows you how to retrieve the core material applied on
                |          the provided support
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Dim iCoreMatRef As Material
                |            Dim MyLinkRootOccRepInsFeat As AnyObject
                |            Set MyLinkRootOccRepInsFeat = MyContext.ComposeLink(oRootOcc, MyPartInstance, MyReference)
                |            ...
                |            Dim oCoreMatCnx As AppliedMaterial
                |            MatService.SetMaterialCore MyLinkRootOccRepInsFeat, iCoreMatRef,
                |            oCoreMatCnx

        :param AnyObject i_support:
        :param MaterialGeneric i_core_material:
        :param AppliedMaterial o_core_applied_material:
        :return: None
        """
        return self.com_object.SetMaterialCore(
            i_support.com_object,
            i_core_material.com_object,
            o_core_applied_material.com_object
        )

    def set_material_covering(
            self,
            i_support: AnyObject,
            i_covering_material: MaterialGeneric,
            o_covering_applied_material: AppliedMaterial
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetMaterialCovering(AnyObject iSupport,MaterialGeneric
                | iCoveringMaterial,AppliedMaterial oCoveringAppliedMaterial)
                |     Applies a covering material on the support defined in
                |     iSupport.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             Defines the support and the context used for applying material. The
                |             context is the root reference defined by iSupport. If the support (target of
                |             iSupport) is an element inside a RepReference then a RepInstance must be
                |             provided in iSupport to make it valid. 
                |         iCoveringMaterial
                |             The material reference to be applied on the support.
                |             
                |         oCoveringAppliedMaterial
                |             The new applied-material created. 
                | 
                |     Example:
                | 
                |          This example shows you how to retrieve the core material applied on
                |          the provided support
                |            
                | 
                |            Dim MatService As MATPLMService
                |            Dim iCoveringMatRef As Material
                |            Dim MyLinkRootOccRepInsFeat As AnyObject
                |            Set MyLinkRootOccRepInsFeat = MyContext.ComposeLink(oRootOcc, MyPartInstance, MyReference)
                |            ...
                |            Dim oCoveringMatCnx As AppliedMaterial
                |            MatService.SetMaterialCore MyLinkRootOccRepInsFeat, iCoveringMatRef,
                |            oCoveringMatCnx

        :param AnyObject i_support:
        :param MaterialGeneric i_covering_material:
        :param AppliedMaterial o_covering_applied_material:
        :return: None
        """
        return self.com_object.SetMaterialCovering(
            i_support.com_object,
            i_covering_material.com_object,
            o_covering_applied_material.com_object
        )

    def __repr__(self):
        return f'MatplmService(name="{self.name}")'
