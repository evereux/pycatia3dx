"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.srs.rfg_grid_face import RfgGridFace


class StrReference(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrReference
                | 
                | Object representing a reference specification for a Structure
                | object.
                | The reference specification is defined by a specification object (surface or
                | Plate), which is often imported into the part document for this structure
                | object. This interface will set or retrieve the original specification object,
                | and will retrieve the local object, which may be the same as the specification
                | object, or may be an imported feature. NOTE: If the specification object is an
                | SDD Product object (Plate, Stiffener or Beam), and not just a feature in these
                | products, specify the Product occurrence as the SDD Product object and the
                | feature as NULL. This way, the modeler can import the proper data for that
                | application object. (But set the feature if you want to reference a specific
                | feature in the SDD product object.)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def rfg_grid_face(self) -> RfgGridFace:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RfgGridFace() As RfgGridFace (Read Only)
                |     Returns the local feature defining the reference geometry. This local
                |     feature is usually an imported datum feature representing the reference
                |     element.
                |     Role:The local feature defining the reference geometry. This feature is
                |     usually an imported datum feature. But if the original specification feature is
                |     in the same 3DShape representation as where it is referenced, then this local
                |     object is the original specification feature.

        :return: RfgGridFace
        """

        return RfgGridFace(self.com_object.RfgGridFace)

    @property
    def role(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Role() As CATBSTR (Read Only)
                |     Returns the role of this parameter. The role is specific to the element
                |     from which this interface was retrieved.

        :return: str
        """

        return self.com_object.Role

    def get_specification(self, ib_to_load: bool, o_ref_prod_occ: AnyObject, o_ref_feature: RfgGridFace) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSpecification(boolean ibToLoad,CATBaseDispatch oRefProdOcc,RfgGridFace
                | oRefFeature)
                |     Retrieves the specification objects for this support
                |     element.
                | 
                |     Parameters:
                | 
                |         ibToLoad
                |             A boolean flag specifying whether to load the referenced product
                |             and representation if they are not already in session.
                |             
                |         oRefProdOcc
                |             The referenced product occurrence defining the reference element.
                |             This product occurrence is unique in a context, so it specifies the assembly
                |             context of the product. 
                |         oRefFeature
                |             The referenced feature.

        :param bool ib_to_load:
        :param AnyObject o_ref_prod_occ:
        :param RfgGridFace o_ref_feature:
        :return: None
        """
        return self.com_object.GetSpecification(ib_to_load, o_ref_prod_occ.com_object, o_ref_feature.com_object)

    def is_synchronized(self, o_status: bool) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsSynchronized(boolean oStatus) As long
                |     Returs the status whether this reference is Synchronized.
                |     Role:If the reference includes an external reference and a local copy of
                |     the data, they may be out of sync. If the reference is to a local object, then
                |     it is always synchronized. If the reference is not synchronized, you may call
                |     Synchronize() to make it in sync. The synchronization
                |     status.
                | 
                |     -1
                |         The status could not be determined. 
                |     0
                |         The reference has no link, so it cannot be out of sync.
                |         
                |     1
                |         The reference local copy is in sync with the original.
                |         
                |     2
                |         The reference local copy is not synchronized with the original.
                |         
                | 
                |     Parameters:
                | 
                |         oStatus.
                | 
                |             TRUE
                |                 The reference does not need synchronization (in sync or no
                |                 link). 
                |             FALSE
                |                 The reference is not synchronized (and could be).

        :param bool o_status:
        :return: int
        """
        return self.com_object.IsSynchronized(o_status)

    def is_valid(self, o_status: bool, o_validation_status: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsValid(boolean oStatus,long oValidationStatus)
                |     Analyzes whether this reference is valid.
                |     Role: Analyzes whether this reference is valid. A reference may be invalid
                |     by itself (if it is the wrong element type or is mandatory but not set), or it
                |     may be invalid in combination with other specifications of the owning
                |     object.
                | 
                |     Parameters:
                | 
                |         oStatus
                | 
                |             TRUE
                |                 The reference is valid (or state could not be determined).
                |                 
                |             FALSE
                |                 The reference is not valid. 
                | 
                |             If not valid 
                |         oValidationStatus
                |             The general status of the validation.
                | 
                |             -1
                |                 The status could not be determined. 
                |             0
                |                 An error occurred in determining the status. 
                |             1
                |                 The referece is valid. 
                |             2
                |                 The reference is invalid.

        :param bool o_status:
        :param int o_validation_status:
        :return: None
        """
        return self.com_object.IsValid(o_status, o_validation_status)

    def set_specification(self, i_ref_prod_occ: AnyObject, i_ref_feature: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSpecification(CATBaseDispatch iRefProdOcc,Reference
                | iRefFeature)
                |     Sets the specification objects for this reference element. The
                |     specification objects are usually in another mechanical product, and are
                |     imported into the current product representation.
                | 
                |     Parameters:
                | 
                |         iRefProdOcc
                |             The referenced product occurrence defining the reference element.
                |             This product occurrence is unique in a context, so it specifies the full
                |             assembly context of the product. 
                |         iRefFeature
                |             The referenced feature. This should be NULL if ispRefProdOcc is a
                |             Structures specialized Product and the modeler is supposed to choose the
                |             features to reference (and import). 
                | 
                |     Example:
                | 
                | 
                |              This example Set the specification object.
                |              
                | 
                |              Dim ObjStrReference1 As StrReference
                |              Set ObjStrReference1 = ObjStrStdPosStParam.GetRef1Data
                |              Set ObjRefU1 = Manager.GetReferencePlane(ObjPart, 2, "CROSS.80")
                |              Set RefU1 = ObjPart.CreateReferenceFromObject(ObjRefU1)
                |              ObjStrReference1.SetSpecification Nothing, RefU1

        :param AnyObject i_ref_prod_occ:
        :param Reference i_ref_feature:
        :return: None
        """
        return self.com_object.SetSpecification(i_ref_prod_occ.com_object, i_ref_feature.com_object)

    def synchronize(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Synchronize()
                |     Synchronize Import.

        :return: None
        """
        return self.com_object.Synchronize()

    def validate_specification(self, i_ref_prod_occ: AnyObject, i_ref_feature: Reference) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ValidateSpecification(CATBaseDispatch iRefProdOcc,Reference iRefFeature)
                | As long
                |     Returns the validation status of a proposed reference
                |     object.
                |     Role:Analyzes and validates whether a proposed reference object is valid. A
                |     reference may be invalid by itself (if it is the wrong element type or is
                |     mandatory but not set), or it may be invalid in combination with other
                |     specifications of the owning object. The general status of the
                |     validation.
                | 
                |     -1
                |         The status could not be determined. 
                |     0
                |         An error occurred in determining the status. 
                |     1
                |         The referece is valid. 
                |     2
                |         The reference is invalid. 
                | 
                |     If not valid
                | 
                |     Parameters:
                | 
                |         iRefProdOcc
                |             The referenced product occurrence. This product occurrence is
                |             unique in a context, so it specifies the assembly context of the product.
                |             
                |         iRefSupport
                |             The referenced feature. In some cases, this feature pointer may be
                |             NULL if the product itself is the reference object.

        :param AnyObject i_ref_prod_occ:
        :param Reference i_ref_feature:
        :return: int
        """
        return self.com_object.ValidateSpecification(i_ref_prod_occ.com_object, i_ref_feature.com_object)

    def __repr__(self):
        return f'StrReference(name="{ self.name }")'
