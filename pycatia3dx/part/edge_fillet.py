"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.part.fillet import Fillet


class EdgeFillet(Fillet):

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
                |                                 EdgeFillet
                | 
                | Represents the edges-based fillet shape.
                | It is the base object for constant radius edge fillets and variable radius edge
                | fillets.
                | 
                | See also:
                |     ConstRadEdgeFillet, VarRadEdgeFillet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def edge_propagation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EdgePropagation() As CatFilletEdgePropagation
                |     Returns or sets the edge fillet propagation mode. This propagation mode is
                |     used when computing the edges to be filleted.
                | 
                |     Example:
                |         The following example returns in mode the edge fillet propagation mode
                |         of the firstEdgeFillet edge fillet, and then sets it to
                |         CATMinimalFilletEdgePropagation, so that a minimum numbers of edges will be
                |         filleted:
                | 
                |          Set mode = firstEdgeFillet.EdgePropagation
                |          Set firstEdgeFillet.EdgePropagation = CATMinimalFilletEdgePropagation

        :return: CatFilletEdgePropagation
        """

        return self.com_object.EdgePropagation

    @edge_propagation.setter
    def edge_propagation(self, value: int):
        """
        :param int value:
        """

        self.com_object.EdgePropagation = value

    @property
    def edges_to_keep(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EdgesToKeep() As References (Read Only)
                |     Returns the collection of edges to keep by the edge
                |     fillet.
                | 
                |     Example:
                |         The following example returns in edges the edges to keep of the
                |         constant radius edge fillet firstCstEdgeFillet:
                | 
                |          Set edges = firstCstEdgeFillet.EdgesToKeep

        :return: References
        """

        return References(self.com_object.EdgesToKeep)

    def add_edge_to_keep(self, i_edge_to_keep: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddEdgeToKeep(Reference iEdgeToKeep)
                |     Adds a new edge to keep by the filleting operation. The edge to keep is not
                |     modified by the fillet.
                | 
                |     Parameters:
                | 
                |         iEdgeToKeep
                |             The edge to keep by the filleting operation
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example adds the new edge edge to be kept from filleting
                |         by the constant radius edge fillet firstCstEdgeFillet:
                | 
                |          firstCstEdgeFillet.AddEdgeToKeep(edge)

        :param Reference i_edge_to_keep:
        :return: None
        """
        return self.com_object.AddEdgeToKeep(i_edge_to_keep.com_object)

    def withdraw_edge_to_keep(self, i_edge_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawEdgeToKeep(Reference iEdgeToWithdraw)
                |     Withdraws an edge from those kept by a filleting
                |     operation.
                | 
                |     Parameters:
                | 
                |         iEdgeToWithdraw
                |             The edge to withdraw
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example withdraws the edge edge from those kept from
                |         filleting by the constant radius edge fillet
                |         firstCstEdgeFillet:
                | 
                |          firstCstEdgeFillet.WithdrawEdgeToKeep(edge)

        :param Reference i_edge_to_withdraw:
        :return: None
        """
        return self.com_object.WithdrawEdgeToKeep(i_edge_to_withdraw.com_object)

    def __repr__(self):
        return f'EdgeFillet(name="{ self.name }")'
