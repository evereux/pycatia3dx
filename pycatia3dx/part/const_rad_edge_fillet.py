"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.part.edge_fillet import EdgeFillet
from pycatia3dx.part.var_rad_edge_fillet import VarRadEdgeFillet


class ConstRadEdgeFillet(EdgeFillet):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.DressUpShape
                |                             CATPartIDLItf.Fillet
                |                                 CATPartIDLItf.EdgeFillet
                |                                     ConstRadEdgeFillet
                | 
                | Represents the edge fillet shape with a constant radius.
                | The resulting shape is made up of edge fillets built with a constant
                | radius.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def objects_to_fillet(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ObjectsToFillet() As References (Read Only)
                |     Returns the collection of reference elements to be
                |     filleted.
                | 
                |     Example:
                |         The following example returns in elements the reference elements to be
                |         filleted of the constant radius edge fillet
                |         firstCstEdgeFillet:
                | 
                |          Set elements = firstCstEdgeFillet.ObjectsToFillet

        :return: References
        """

        return References(self.com_object.ObjectsToFillet)

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Radius() As Length (Read Only)
                |     Returns the edge fillet constant radius.
                | 
                |     Example:
                |         The following example returns in radius the radius of the constant
                |         radius edge fillet firstCstEdgeFillet:
                | 
                |          Set radius = firstCstEdgeFillet.Radius

        :return: Length
        """

        return Length(self.com_object.Radius)

    def add_object_to_fillet(self, i_object_to_fillet: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObjectToFillet(Reference iObjectToFillet)
                |     Adds a new sub-element to be filleted. This sub-element is usually an
                |     edge.
                | 
                |     Parameters:
                | 
                |         iObjectToFillet
                |             The sub-element to be filleted
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example adds a new geometrical element element to be
                |         filleted by the constant radius edge fillet
                |         firstCstEdgeFillet:
                | 
                |          firstCstEdgeFillet.AddObjectToFillet(element)

        :param Reference i_object_to_fillet:
        :return: None
        """
        return self.com_object.AddObjectToFillet(i_object_to_fillet.com_object)

    def switch_to_var_fillet_type(self) -> VarRadEdgeFillet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SwitchToVarFilletType() As VarRadEdgeFillet
                |     Changes the type of EdgeFillet to variable EdgeFillet and return
                |     it.
                | 
                |     Parameters:
                | 
                |         opVarFillet
                |             The opVarFillet is the variable edge fillet

        :return: VarRadEdgeFillet
        """
        return VarRadEdgeFillet(self.com_object.SwitchToVarFilletType())

    def withdraw_object_to_fillet(self, i_object_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawObjectToFillet(Reference iObjectToWithdraw)
                |     Withdraws a sub-element from those to be filleted. This sub-element is
                |     usually an edge.
                | 
                |     Parameters:
                | 
                |         iObjectToWithdraw
                |             The sub-element to withdraw
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example withdraws the geometrical element element from
                |         those to be filleted by the constant radius edge fillet
                |         firstCstEdgeFillet:
                | 
                |          firstCstEdgeFillet.WithdrawObjectToFillet(element)

        :param Reference i_object_to_withdraw:
        :return: None
        """
        return self.com_object.WithdrawObjectToFillet(i_object_to_withdraw.com_object)

    def __repr__(self):
        return f'ConstRadEdgeFillet(name="{ self.name }")'
