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
from pycatia3dx.part.const_rad_edge_fillet import ConstRadEdgeFillet
from pycatia3dx.part.edge_fillet import EdgeFillet


class VarRadEdgeFillet(EdgeFillet):

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
                |                                     VarRadEdgeFillet
                | 
                | Represents the edge fillet shape with a variable radius.
                | The resulting shape is made up of edges fillets controlled by couples of
                | radius/vertex.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def bitangency_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BitangencyType() As CatFilletBitangencyType
                |     Returns or set the fillet bitangency type.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type used to perform the fillet : catSphereBitangencyType or catCircleBitangencyType

        :return: CatFilletBitangencyType
        """

        return self.com_object.BitangencyType

    @bitangency_type.setter
    def bitangency_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.BitangencyType = value

    @property
    def edges_to_fillet(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EdgesToFillet() As References (Read Only)
                |     Returns the collection of edges to be filleted.
                | 
                |     Example:
                |         The following example returns in edges the edges to fillet of variable
                |         radius edge filletfirstVarEdgeFillet:
                | 
                |          Set edges = firstVarEdgeFillet.EdgesToFillet

        :return: References
        """

        return References(self.com_object.EdgesToFillet)

    @property
    def fillet_spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilletSpine() As Reference
                |     Returns or set the spine for circle bitangency fillet.
                | 
                |     Parameters:
                | 
                |         iSpin
                |             The spine to be used for a circle bitangency fillet

        :return: Reference
        """

        return Reference(self.com_object.FilletSpine)

    @fillet_spine.setter
    def fillet_spine(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FilletSpine = value

    @property
    def fillet_variation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilletVariation() As CatFilletVariation
                |     Returns or sets the edge fillet radius variation mode.
                | 
                |     Example:
                |         The following example returns in mode the radius variation mode of the
                |         variable radius edge filletfirstVarEdgeFillet, and then sets it to
                |         CATLinearFilletVariation so that the radius variation is linear between two
                |         control vertices:
                | 
                |          mode = firstVarEdgeFillet.FilletVariation
                |          firstVarEdgeFillet.FilletVariation = CATLinearFilletVariation

        :return: CatFilletVariation
        """

        return self.com_object.FilletVariation

    @fillet_variation.setter
    def fillet_variation(self, value: int):
        """
        :param int value:
        """

        self.com_object.FilletVariation = value

    @property
    def imposed_vertices(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ImposedVertices() As References (Read Only)
                |     Returns the collection of vertices where a radius has been
                |     imposed.
                | 
                |     Example:
                |         The following example returns in vertices the collection of imposed
                |         vertices of the variable radius edge
                |         filletfirstVarEdgeFillet:
                | 
                |          Set vertices = firstVarEdgeFillet.ImposedVertices

        :return: References
        """

        return References(self.com_object.ImposedVertices)

    @property
    def sharp_edge_removal_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SharpEdgeRemovalMode() As short
                |     Returns or set the sharp edge removal mode for variable edge
                |     fillet.
                | 
                |     Parameters:
                | 
                |         iMode
                |             The mode to be used for variable edge fillet

        :return: int
        """

        return self.com_object.SharpEdgeRemovalMode

    @sharp_edge_removal_mode.setter
    def sharp_edge_removal_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.SharpEdgeRemovalMode = value

    def add_edge_to_fillet(self, i_edge: Reference, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddEdgeToFillet(Reference iEdge,double iRadius)
                |     Adds a new edge to the variable radius edge fillet.
                | 
                |     Parameters:
                | 
                |         iEdge
                |             The edge to be filleted
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                |         iRadius
                |             The radius to impose along the edge. This radius is imposed at both
                |             end points of the edge. 
                | 
                |     Example:
                |         The following example adds the new edge to be filleted to the
                |         variable radius edge fillet firstVarEdgeFillet:
                | 
                |          call firstVarEdgeFillet.AddEdgeToFillet(edge, 5.)

        :param Reference i_edge:
        :param float i_radius:
        :return: None
        """
        return self.com_object.AddEdgeToFillet(i_edge.com_object, i_radius)

    def add_imposed_vertex(self, i_vertex: Reference, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddImposedVertex(Reference iVertex,double iRadius)
                |     Adds a new control couple. A control couple is made up of a vertex and a
                |     radius.
                | 
                |     Parameters:
                | 
                |         iVertex
                |             The vertex where to impose the radius 
                |         iRadius
                |             The radius to impose at the given vertex 
                | 
                |     Example:
                |         The following example adds a new control couple (vertex, radius) to the
                |         variable radius edge fillet firstVarEdgeFillet set with the vertex and a
                |         radius of 50.
                | 
                |          call firstVarEdgeFillet.AddImposedVertex(vertex, 50.)

        :param Reference i_vertex:
        :param float i_radius:
        :return: None
        """
        return self.com_object.AddImposedVertex(i_vertex.com_object, i_radius)

    def imposed_vertex_radius(self, i_imposed_vertex: Reference) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ImposedVertexRadius(Reference iImposedVertex) As Length
                |     Returns the fillet radius on an imposed vertex.
                | 
                |     Parameters:
                | 
                |         iImposedVertex
                |             The vertex where to retrieve the fillet radius 
                | 
                |     Returns:
                |         The fillet radius 
                |     Example:
                |         The following example returns in radius the fillet radius of the
                |         variable radius edge fillet firstVarEdgeFillet at the vertex
                |         vertex:
                | 
                |          Set radius = firstVarEdgeFillet.ImposedVertexRadius(vertex)

        :param Reference i_imposed_vertex:
        :return: Length
        """
        return Length(self.com_object.ImposedVertexRadius(i_imposed_vertex.com_object))

    def switch_to_const_fillet_type(self) -> ConstRadEdgeFillet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SwitchToConstFilletType() As ConstRadEdgeFillet
                |     Changes the type of EdgeFillet to constant EdgeFillet and return
                |     it.
                | 
                |     Parameters:
                | 
                |         opConstFillet
                |             The opConstFillet is the variable edge fillet

        :return: ConstRadEdgeFillet
        """
        return ConstRadEdgeFillet(self.com_object.SwitchToConstFilletType())

    def withdraw_edge_to_fillet(self, i_edge: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawEdgeToFillet(Reference iEdge)
                |     Withdraws an edge from the variable radius edge fillet.
                | 
                |     Parameters:
                | 
                |         iEdge
                |             The edge to be withdrawn
                |             The following Boundary object is supported: TriDimFeatEdge.
                |             
                | 
                |     Example:
                |         The following example withdraws the edge from those to be filleted
                |         of the variable radius edge fillet firstVarEdgeFillet:
                | 
                |          call firstVarEdgeFillet.WithdrawEdgeToFillet(edge)

        :param Reference i_edge:
        :return: None
        """
        return self.com_object.WithdrawEdgeToFillet(i_edge.com_object)

    def withdraw_imposed_vertex(self, i_vertex: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub WithdrawImposedVertex(Reference iVertex)
                |     Withdraws a control couple.
                | 
                |     Parameters:
                | 
                |         iVertex
                |             The vertex where the radius is imposed 
                | 
                |     Example:
                |         The following example withdraws the imposed radius on the vertex
                |         for the variable radius edge fillet
                |         firstVarEdgeFillet:
                | 
                |          call firstVarEdgeFillet.WithdrawImposedVertex(vertex)

        :param Reference i_vertex:
        :return: None
        """
        return self.com_object.WithdrawImposedVertex(i_vertex.com_object)

    def __repr__(self):
        return f'VarRadEdgeFillet(name="{ self.name }")'
