"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrManufacturingFastenerFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrManufacturingFastenerFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_dr_manufacturing_fastener(self, oh_mfg_fastener: AnyObject, i_origin: tuple, i_axis: tuple, i_reference: str, i_diameter: float, i_length: float, i_min_stack: float, i_max_stack: float, i_list_of_user_name: tuple, i_list_of_user_value: tuple, i_list_of_user_type: tuple, ih_geometry: AnyObject, ih_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateDRManufacturingFastener(AnyObject ohMfgFastener,CATSafeArrayVariant
                | iOrigin,CATSafeArrayVariant iAxis,CATBSTR iReference,double iDiameter,double
                | iLength,double iMinStack,double iMaxStack,CATSafeArrayVariant
                | iListOfUserName,CATSafeArrayVariant iListOfUserValue,CATSafeArrayVariant
                | iListOfUserType,AnyObject ihGeometry,AnyObject ihProduct)
                |     Creates a manufacturing fastener.
                | 
                |     Parameters:
                | 
                |         ohMfgFastener
                |             The newly created manufacturing fastener. 
                |         iOrigin
                |             Coordinates of local origin(Array of 3 double). 
                |         iAxis
                |             Coordinates of local Z direction(Array of 3 double).
                |             
                |         iReference
                |             Reference name of fastener. 
                |         iDiameter
                |             Diameter of fastener (mm). 
                |         iLength
                |             Length of fastener (mm). 
                |         iMinStack
                |             Min stack depth of fastener (mm). 
                |         iMaxStack
                |             Max stack depth of fastener (mm). 
                |         iListOfUserName
                |             List of user parameter names. It is Array of CATBSTR pointers
                |             
                |         iListOfUserValue
                |             List of user parameter values. It is Array of CATBSTR pointers
                |             
                |         iListOfUserType
                |             List of user parameter types (0: CATBSTR, 1: integer, 2: length in
                |             mm). 
                |         ihGeometry
                |             Geometry pointed by the fastener. It can be a design point or a PLM
                |             fastener object. 
                |         ihProduct
                |             Product containing the geometry. May be NULL_var in case of PLM
                |             fastener object.

        :param AnyObject oh_mfg_fastener:
        :param tuple i_origin:
        :param tuple i_axis:
        :param str i_reference:
        :param float i_diameter:
        :param float i_length:
        :param float i_min_stack:
        :param float i_max_stack:
        :param tuple i_list_of_user_name:
        :param tuple i_list_of_user_value:
        :param tuple i_list_of_user_type:
        :param AnyObject ih_geometry:
        :param AnyObject ih_product:
        :return: None
        """
        return self.com_object.CreateDRManufacturingFastener(oh_mfg_fastener.com_object, i_origin, i_axis, i_reference, i_diameter, i_length, i_min_stack, i_max_stack, i_list_of_user_name, i_list_of_user_value, i_list_of_user_type, ih_geometry.com_object, ih_product.com_object)

    def delete_dr_manufacturing_fastener(self, ih_mfg_fastener: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteDRManufacturingFastener(AnyObject ihMfgFastener)
                |     Deletes a DR Manufacturing fastener.
                | 
                |     Parameters:
                | 
                |         ihMfgFastener
                |             fastener to be deleted. 

        :param AnyObject ih_mfg_fastener:
        :return: None
        """
        return self.com_object.DeleteDRManufacturingFastener(ih_mfg_fastener.com_object)

    def __repr__(self):
        return f'SpotDrManufacturingFastenerFactory(name="{ self.name }")'
