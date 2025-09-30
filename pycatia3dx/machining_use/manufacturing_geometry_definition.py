"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingGeometryDefinition(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingGeometryDefinition
                | 
                | Interface dedicated to geometry definition.
                | 
                | Role: This interface offers service to set or get the
                | geometries.
                | 
                | The methods are consider geometries from the given type. This
                | iType parameter corresponds to a key word ending the wanted interface.
                | (CATIM3xiType, CATIMfgiType or CATIiType) For example iType = "Parts"
                | to consider the parts geometries (for CATIMfgParts) iType = "Checks"
                | to consider the checks geometries (for CATIMfgChecks) iType = "MultiAxisPart"
                | to consider the parts geometries for multi-axis operation
                |    iType = "FirstGuideLine"
                |    iType = "FirstStopLine"
                |    iType = "SecondGuideLine"
                |    iType = "SecondStopLine"
                |    iType = "AuxGuidingCurves"
                |    iType = "FirstRelimitingElement"
                |    iType = "SecondRelimitingElement"
                |    iType = "MultiAxisRefPoint"
                |    iType = "MultiAxisStartElement"
                |    iType = "MultiAxisEndElement"
                |    iType = "GuidingCurves"
                |    iType = "SetupStocks" to consider the stock of the PO
                |    iType = "SetupDesigns" to consider the design part of the PO

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_geometry(self, i_type: str, i_reference: AnyObject, i_product: AnyObject, i_verify: int, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddGeometry(CATBSTR iType,AnyObject iReference,AnyObject iProduct,long
                | iVerify,long iPosition)
                |     Adds a geometry.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of the geometry to add. 
                |         iReference
                |             Geometry to add. 
                |         iProduct
                |             Product to whech belongs the geometry to add. 
                |         iVerify
                | 
                |             Legal values: The parameter can be
                |             0
                |                 Add the geometry without any checks. (default value)
                |             1
                |                 Add the geometry only if it is not already in the geometries
                |                 list. 
                | 
                |         iPostion
                |             Position at which add the geometry in the geometries list. (default value = 0)

        :param str i_type:
        :param AnyObject i_reference:
        :param AnyObject i_product:
        :param int i_verify:
        :param int i_position:
        :return: None
        """
        return self.com_object.AddGeometry(i_type, i_reference.com_object, i_product.com_object, i_verify, i_position)

    def get_geometric_elements(self, i_type: str, i_all_geometric_elements: int, i_duplicate: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGeometricElements(CATBSTR iType,long iAllGeometricElements,long
                | iDuplicate) As CATSafeArrayVariant
                |     Gets the list of geometric elements.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of the geometries to get. 
                |         iAllGeometricElements
                |             Specifies if all geometric elements must be
                |             retrieved.
                |             Legal values: The parameter can be
                | 
                |             0
                |                 Only geometric elements on the visible space are retrieved
                |                 (default value) 
                |             1
                |                 All geometric elements are retrieved 
                | 
                |         iDuplicate
                |             Specifies if the geometric elements must be
                |             duplicated
                |             Legal values: The parameter can be
                | 
                |             0
                |                 Geometric elements are duplicated only if necessary in a
                |                 product context (default value) 
                |             1
                |                 Geometric elements are duplicated 
                | 
                |         oGeometricElements
                |             Returned geometric elements list.

        :param str i_type:
        :param int i_all_geometric_elements:
        :param int i_duplicate:
        :return: tuple
        """
        return self.com_object.GetGeometricElements(i_type, i_all_geometric_elements, i_duplicate)

    def get_geometric_elements2(self, i_type: str, i_all_geometric_elements: int, i_duplicate: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGeometricElements2(CATBSTR iType,long iAllGeometricElements,long
                | iDuplicate) As CATSafeArrayVariant
                |     Gets the list of geometric elements.
                | 
                |     Deprecated:
                |         R426 Use DELMIAMfgGeometryDefinition#GetGeometricElements
                |         
                |     Parameters:
                | 
                |         iType
                |             Type of the geometries to get. 
                |         iAllGeometricElements
                |             Specifies if all geometric elements must be
                |             retrieved.
                |             Legal values: The parameter can be
                | 
                |             0
                |                 Only geometric elements on the visible space are retrieved
                |                 (default value) 
                |             1
                |                 All geometric elements are retrieved 
                | 
                |         iDuplicate
                |             Specifies if the geometric elements must be
                |             duplicated
                |             Legal values: The parameter can be
                | 
                |             0
                |                 Geometric elements are duplicated only if necessary in a
                |                 product context (default value) 
                |             1
                |                 Geometric elements are duplicated 
                | 
                |         oGeometricElements
                |             Returned geometric elements list.

        :param str i_type:
        :param int i_all_geometric_elements:
        :param int i_duplicate:
        :return: tuple
        """
        return self.com_object.GetGeometricElements2(i_type, i_all_geometric_elements, i_duplicate)

    def get_geometric_references(self, i_type: str, o_list_geometries: tuple, o_list_products: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetGeometricReferences(CATBSTR iType,CATSafeArrayVariant
                | oListGeometries,CATSafeArrayVariant oListProducts)
                |     Gets the list of geometric references.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of the geometries to get. 
                |         oListGeometries
                |             Returned geometric references list. 
                |         oListProducts
                |             Returned products list corresponding to geometric references.

        :param str i_type:
        :param tuple o_list_geometries:
        :param tuple o_list_products:
        :return: None
        """
        return self.com_object.GetGeometricReferences(i_type, o_list_geometries, o_list_products)

    def get_geometric_references2(self, i_type: str, o_list_geometries: tuple, o_list_products: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetGeometricReferences2(CATBSTR iType,CATSafeArrayVariant
                | oListGeometries,CATSafeArrayVariant oListProducts)
                |     Gets the list of geometric references.
                | 
                |     Deprecated:
                |         R426 Use DELMIAMfgGeometryDefinition#GetGeometricReferences
                |         
                |     Parameters:
                | 
                |         iType
                |             Type of the geometries to get. 
                |         oListGeometries
                |             Returned geometric references list. 
                |         oListProducts
                |             Returned products list corresponding to geometric references.

        :param str i_type:
        :param tuple o_list_geometries:
        :param tuple o_list_products:
        :return: None
        """
        return self.com_object.GetGeometricReferences2(i_type, o_list_geometries, o_list_products)

    def remove_geometries(self, i_type: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveGeometries(CATBSTR iType)
                |     Remove geometries of the given type.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of the geometries to remove.

        :param str i_type:
        :return: None
        """
        return self.com_object.RemoveGeometries(i_type)

    def __repr__(self):
        return f'ManufacturingGeometryDefinition(name="{ self.name }")'
