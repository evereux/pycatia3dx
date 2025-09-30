"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_machining_use.manufacturing_part_operation import ManufacturingPartOperation


class ManufacturingPartOperationPosition(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingPartOperationPosition
                | 
                | Interface representing Part Operation Position
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_alias(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAlias() As CATBSTR
                |     Get the alias of the position

        :return: str
        """
        return self.com_object.GetAlias()

    def get_attach_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttachStatus() As boolean
                |     Returns if the position is attached/detached on the
                |     machine
                | 
                |     Parameters:
                | 
                |         isAttached
                | 
                |             Legal values: TRUE if the position is attached, FALSE else
                |             
                | 
                |     Returns:
                |         E_FAIL if the position is not mounted

        :return: bool
        """
        return self.com_object.GetAttachStatus()

    def get_part_operation(self) -> ManufacturingPartOperation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPartOperation() As ManufacturingPartOperation
                |     Associates a product to the Part Operation.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product to be associated. If iProduct is NULL_var, the
                |             previously associated product is removed.

        :return: ManufacturingPartOperation
        """
        return ManufacturingPartOperation(self.com_object.GetPartOperation())

    def get_product(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProduct() As AnyObject
                |     Retrieves the product associated to the Part Operation.
                | 
                |     Parameters:
                | 
                |         oProduct
                |             The associated product. If we are in File Based context, oProduct
                |             is a reference If we are in Manufacturing Hub context, oProduct is an instance

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetProduct())

    def get_product_occurrence(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProductOccurrence() As AnyObject
                |     Retrieves the product associated to the Part Operation.
                | 
                |     Parameters:
                | 
                |         oProduct
                |             The associated product. It is an Occurance

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetProductOccurrence())

    def get_rotary_planes(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRotaryPlanes() As AnyObject
                |     Retrieves the rotary planes associated to the Part
                |     Operation.
                | 
                |     Parameters:
                | 
                |         oRotaryPlanes
                |             The rotary planes. Use CATIMfgAgregate on oRotaryPlanes to access
                |             each plane. 
                | 
                |     Returns:
                |         E_FAIL if the rotary planes is not defined.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetRotaryPlanes())

    def get_safety_plane_so(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSafetyPlaneSO() As AnyObject
                |     Retrieves the safety plane associated to the Part
                |     Operation.
                | 
                |     Parameters:
                | 
                |         oSafetyPlane
                |             The safety plane. 
                | 
                |     Returns:
                |         E_FAIL if the safety plane is not defined.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetSafetyPlaneSO())

    def get_top_plane_direction_inversion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTopPlaneDirectionInversion() As long
                |     Gets the top plane direction inversion value.
                | 
                |     Parameters:
                | 
                |         oMode
                | 
                |             Legal values: 1 if the top plane direction has been inverted, 0
                |             otherwise

        :return: int
        """
        return self.com_object.GetTopPlaneDirectionInversion()

    def get_transition_planes(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTransitionPlanes() As AnyObject
                |     Retrieves the transition planes associated to the Part
                |     Operation.
                | 
                |     Parameters:
                | 
                |         oTransitionPlanes
                |             The transition planes. Use CATIMfgAgregate on oTransitionPlanes to
                |             access each plane. 
                | 
                |     Returns:
                |         E_FAIL if the transition planes is not defined.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetTransitionPlanes())

    def set_alias(self, i_new_alias: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAlias(CATBSTR iNewAlias)
                |     Set the alias of the position
                | 
                |     Parameters:
                | 
                |         iNewAlias
                |             Alias of the position

        :param str i_new_alias:
        :return: None
        """
        return self.com_object.SetAlias(i_new_alias)

    def set_product(self, i_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProduct(AnyObject iProduct)
                |     Associates a product to the Part Operation.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             The product to be associated. If iProduct is NULL_var, the
                |             previously associated product is removed.

        :param AnyObject i_product:
        :return: None
        """
        return self.com_object.SetProduct(i_product.com_object)

    def set_safety_plane_so(self, i_safety_plane: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSafetyPlaneSO(AnyObject iSafetyPlane)
                |     Set the safety plane associated to the Part Operation.
                | 
                |     Parameters:
                | 
                |         iSafetyPlane
                |             The safety plane. 
                | 
                |     Returns:
                |         E_FAIL if the safety plane is not defined.

        :param AnyObject i_safety_plane:
        :return: None
        """
        return self.com_object.SetSafetyPlaneSO(i_safety_plane.com_object)

    def set_top_plane_direction_inversion(self, i_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTopPlaneDirectionInversion(long iMode)
                |     Sets the top plane direction inversion value in order to determine the
                |     traverse box position relatively to the top plane.
                | 
                |     Parameters:
                | 
                |         iMode
                | 
                |             Legal values: 1 if the top plane direction is to be inverted, 0
                |             otherwise 
                | 
                |     Returns:
                |         E_INVALIDARG if iMode is different from 0 or 1.

        :param int i_mode:
        :return: None
        """
        return self.com_object.SetTopPlaneDirectionInversion(i_mode)

    def __repr__(self):
        return f'ManufacturingPartOperationPosition(name="{ self.name }")'
