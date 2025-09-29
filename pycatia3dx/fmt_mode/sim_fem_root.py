"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.parameters import Parameters
from pycatia3dx.knowledge_interfaces.relations import Relations
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.system.any_object import AnyObject


class SimFemRoot(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFemRoot
                | 
                | Represents the root feature of the FEM Representation.
                | Role: It aggregates all the objects making up the FEM
                | Representation.
                | 
                | Example:
                | 
                |      This example shows how to retrieve the FEM Representation's root feature
                |      from its Representation Reference:
                |      
                | 
                |      Dim MyRepRef As VPMRepReference
                |      Set MyRepRef = ...
                |      Dim MyFEMRoot As SimFemRoot
                |      Set MyFEMRoot = MyRepRef.GetItem("SimFemRoot")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def has_an_associated_rep(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HasAnAssociatedRep() As boolean (Read Only)
                |     Retrieves the flag that determines if the FEM root has an associated
                |     representation or not.

        :return: bool
        """

        return self.com_object.HasAnAssociatedRep

    @property
    def has_children_fem_rep(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HasChildrenFemRep() As boolean (Read Only)
                |     Retrieves the flag that determines if the FEM root has an associated
                |     representation or not.

        :return: bool
        """

        return self.com_object.HasChildrenFemRep

    @property
    def parameters(self) -> Parameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parameters() As Parameters (Read Only)
                |     Returns the collection containing the FEM Representation parameters. All
                |     the parameters that are defined in FEM Representation might be accessed thru
                |     that collection.
                | 
                |     Example:
                | 
                |          This example returns the parameters created in
                |          MyFEMRoot:
                |          
                | 
                |          Dim MyFEMRoot As SimulationFEMRoot
                |          Set MyFEMRoot = ...
                |          Dim params As Parameters
                |          Set params = MyFEMRoot.Parameters

        :return: Parameters
        """

        return Parameters(self.com_object.Parameters)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Relations() As Relations (Read Only)
                |     Returns the collection containing the FEM Representation relations. All the
                |     relations that are defined in FEM Representation might be accessed thru that
                |     collection.
                | 
                |     Example:
                | 
                |          This example returns in the relations created in
                |          MyFEMRoot:
                |          
                | 
                |          Dim MyFEMRoot As SimulationFEMRoot
                |          Set MyFEMRoot = ...
                |          Dim relation As Relations
                |          Set relation = MyFEMRoot.Relations

        :return: Relations
        """

        return Relations(self.com_object.Relations)

    @property
    def update_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpdateStatus() As boolean (Read Only)
                |     Returns the Update Status of a FEM root.

        :return: bool
        """

        return self.com_object.UpdateStatus

    def add_associated_rep(self, i_associated_rep: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddAssociatedRep(AnyObject iAssociatedRep)
                |     Associates a representation to the FEM Representation.
                | 
                |     Parameters:
                | 
                |         iAssociatedRep
                |             The link object that represents the representation to associate to
                |             the FEM Representation.
                |             PLMProductService.ComposeLink

        :param AnyObject i_associated_rep:
        :return: None
        """
        return self.com_object.AddAssociatedRep(i_associated_rep.com_object)

    def add_child(self, i_child_fem_rep: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddChild(AnyObject iChildFEMRep)
                |     Adds a child FEM Rep.
                | 
                |     Parameters:
                | 
                |         iChildFEMRep
                |             The link object that represents the child FEM representation to
                |             add.
                |             PLMProductService.ComposeLink

        :param AnyObject i_child_fem_rep:
        :return: None
        """
        return self.com_object.AddChild(i_child_fem_rep.com_object)

    def exclude_property_connection(self, i_occurrence: VPMOccurrence, i_connection_property: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExcludePropertyConnection(VPMOccurrence iOccurrence,AnyObject
                | iConnectionProperty)
                |     Excludes the connection proporty and deletes the connection mesh part in
                |     the FEM representation of the given product.
                | 
                |     Parameters:
                | 
                |         iOccurrence
                |             Product assembly containing the connection property.
                |             
                |         iConnectionProperty
                |             Connection property to exclude.

        :param VPMOccurrence i_occurrence:
        :param AnyObject i_connection_property:
        :return: None
        """
        return self.com_object.ExcludePropertyConnection(i_occurrence.com_object, i_connection_property.com_object)

    def get_associated_reps(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAssociatedReps() As CATSafeArrayVariant
                |     Retrieves all the associated representations.

        :return: tuple
        """
        return self.com_object.GetAssociatedReps()

    def get_children(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetChildren() As CATSafeArrayVariant
                |     Gets children FEM Rep.
                | 
                |     Parameters:
                | 
                |         oChildren
                |             A links array of all children FEM Reps.

        :return: tuple
        """
        return self.com_object.GetChildren()

    def get_nb_of_associated_rep(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbOfAssociatedRep() As long
                |     Retrieves the number of associated representation.

        :return: int
        """
        return self.com_object.GetNbOfAssociatedRep()

    def get_nb_of_children_fem_rep(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbOfChildrenFemRep() As long
                |     Retrieves the number of children FEM representation.

        :return: int
        """
        return self.com_object.GetNbOfChildrenFemRep()

    def get_numbering_labels(self, i_type: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberingLabels(SimMeshEntityType iType) As
                | CATSafeArrayVariant
                |     Retrieves all the numbering labels of current object
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of mesh entity: simMeshNodeEntity or simMeshElementEntity.

        :param int i_type:
        :return: tuple
        """
        return self.com_object.GetNumberingLabels(i_type)

    def get_numbering_labels_from_path(self, i_type: int, i_path: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberingLabelsFromPath(SimMeshEntityType iType,AnyObject iPath) As
                | CATSafeArrayVariant
                |     Retrieves all the numbering labels of current object
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of mesh entity: simMeshNodeEntity or simMeshElementEntity.
                |             
                |         iType
                |             Path to child FEM, mesh part or group.

        :param int i_type:
        :param AnyObject i_path:
        :return: tuple
        """
        return self.com_object.GetNumberingLabelsFromPath(i_type, i_path.com_object)

    def get_numbering_offset_value(self, i_type: int, i_child_fem_rep: AnyObject, o_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNumberingOffsetValue(SimMeshEntityType iType,AnyObject iChildFEMRep,long
                | oValue)
                |     Retrieves numbering offset value of a child FEM
                |     representation.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of mesh entity: simMeshNodeEntity or simMeshElementEntity.
                |             
                |         iChildFEMRep
                |             The CATIA base object that represent the child FEM representation.

        :param SimMeshEntityType i_type:
        :param AnyObject i_child_fem_rep:
        :param int o_value:
        :return: None
        """
        return self.com_object.GetNumberingOffsetValue(i_type, i_child_fem_rep.com_object, o_value)

    def get_set(self, i_set_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSet(CATBSTR iSetType) As CATBaseDispatch
                |     Retrieves or creates a set from its type.
                |     Role: To find a set inside the FEM Representation.
                | 
                |     Parameters:
                | 
                |         iSetType
                |             The searched set type.
                |             Legal values:
                | 
                |                 SimNodesElements
                |                 SimProperties
                |                 SimGroups
                |                 SimConnectionProperties
                |                 SimAbstractions
                |                 SimBehaviors
                |                 SimVisualization
                | 
                |     Returns:
                |         The retrieved or created set. 
                |     Example:
                | 
                |          This example returns in the Mesh Set created in
                |          MyFEMRoot:
                |          
                | 
                |          Dim MyFEMRoot As SimFemRoot
                |          Set MyFEMRoot = ...
                |          Dim MyMeshSet As SimMeshSet
                |          Set MyMeshSet = MyFEMRoot.GetSet("SimNodesElements")

        :param str i_set_type:
        :return: AnyObject
        """
        return self.com_object.GetSet(i_set_type)

    def include_property_connection(self, i_occurrence: VPMOccurrence, i_connection_property: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IncludePropertyConnection(VPMOccurrence iOccurrence,AnyObject
                | iConnectionProperty)
                |     Includes the connection property and creates the connection mesh part in
                |     the FEM representation of the given product.
                | 
                |     Parameters:
                | 
                |         iOccurrence
                |             The product occurrence containing the connection property.
                |             
                |         iConnectionProperty
                |             The connection property to include.

        :param VPMOccurrence i_occurrence:
        :param AnyObject i_connection_property:
        :return: None
        """
        return self.com_object.IncludePropertyConnection(i_occurrence.com_object, i_connection_property.com_object)

    def is_included_property_connection(self, i_occurrence: VPMOccurrence, i_connection_property: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsIncludedPropertyConnection(VPMOccurrence iOccurrence,AnyObject
                | iConnectionProperty) As boolean
                |     Tests whether a connection property is included in the FEM representation
                |     or not.
                | 
                |     Parameters:
                | 
                |         iOccurrence
                |             Product assembly containing the connection property.
                |             
                |         iConnectionProperty
                |             Connection property which inclusion is tested. 
                | 
                |     Returns:
                | 
                |             True: the connection property is included.
                |             False: the connection property is not included.

        :param VPMOccurrence i_occurrence:
        :param AnyObject i_connection_property:
        :return: bool
        """
        return self.com_object.IsIncludedPropertyConnection(i_occurrence.com_object, i_connection_property.com_object)

    def remove_associated_rep(self, i_associated_rep: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAssociatedRep(AnyObject iAssociatedRep)
                |     Removes a representation to the FEM Representation.
                | 
                |     Parameters:
                | 
                |         iAssociatedRep
                |             The link object that represents the representation to remove from
                |             the FEM Representation.
                |             PLMProductService.ComposeLink

        :param AnyObject i_associated_rep:
        :return: None
        """
        return self.com_object.RemoveAssociatedRep(i_associated_rep.com_object)

    def remove_child(self, i_child_fem_rep: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveChild(AnyObject iChildFEMRep)
                |     Removes a child FEM Rep.
                | 
                |     Parameters:
                | 
                |         iChildFEMRep
                |             The link object that represents the child FEM representation to
                |             remove.
                |             PLMProductService.ComposeLink

        :param AnyObject i_child_fem_rep:
        :return: None
        """
        return self.com_object.RemoveChild(i_child_fem_rep.com_object)

    def remove_numbering(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveNumbering()
                |     Removes numbering specification.

        :return: None
        """
        return self.com_object.RemoveNumbering()

    def set_numbering_offset_value(self, i_type: int, i_child_fem_rep: AnyObject, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetNumberingOffsetValue(SimMeshEntityType iType,AnyObject iChildFEMRep,long
                | iValue)
                |     Sets numbering offset value to a child FEM representation.
                | 
                |     Parameters:
                | 
                |         iType
                |             Type of mesh entity: simMeshNodeEntity or simMeshElementEntity.
                |             
                |         iChildFEMRep
                |             The CATIA base object that represent the child FEM representation.

        :param int i_type:
        :param AnyObject i_child_fem_rep:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetNumberingOffsetValue(i_type, i_child_fem_rep.com_object, i_value)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Launches the update of a FEM root.

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SimFemRoot(name="{self.name}")'
