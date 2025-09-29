"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_groups import SimGroups
from pycatia3dx.fmt_mode.sim_mesh_specifications import SimMeshSpecifications
from pycatia3dx.fmt_mode.sim_topology_specifications import SimTopologySpecifications
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class SimMeshPart(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMeshPart
                | 
                | Represents a Mesh Part.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def construction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Construction() As boolean
                |     Returns the construction status of an Mesh Part.

        :return: bool
        """

        return self.com_object.Construction

    @construction.setter
    def construction(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Construction = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Returns the Mesh Part type.

        :return: str
        """

        return self.com_object.Type

    @property
    def update_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpdateStatus() As boolean (Read Only)
                |     Returns the Update Status of a meshpart.

        :return: bool
        """

        return self.com_object.UpdateStatus

    def add_support(self, i_support: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddSupport(AnyObject iSupport)
                |     Creates a new support and add it to the support description of the Mesh
                |     Part.
                | 
                |     Parameters:
                | 
                |         iSupport:
                |             The link object that represents the geometry to
                |             mesh.
                |             PLMProductService.ComposeLink

        :param AnyObject i_support:
        :return: None
        """
        return self.com_object.AddSupport(i_support.com_object)

    def get_attribute_value(self, i_set_type: str, i_attribute: str, o_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAttributeValue(CATBSTR iSetType,CATBSTR iAttribute,CATVariant
                | oValue)
                |     Retrieves the value corresponding to the given attribute.
                | 
                |     Parameters:
                | 
                |         iSetType:
                |             The identifier of the set specification.
                |             Legal values: "Mesh" or "Topology". 
                |         iAttribute:
                |             The name of attribute. 
                | 
                |     Returns:
                |         The value of the global mesh attribute.

        :param str i_set_type:
        :param str i_attribute:
        :param CATVariant o_value:
        :return: None
        """
        return self.com_object.GetAttributeValue(i_set_type, i_attribute, o_value)

    def get_groups(self) -> SimGroups:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGroups() As SimGroups
                |     Returns the group collection from the Mesh Part.
                | 
                |     See also:
                |         SimGroups
                |     Returns:
                |         The associated collection of groups.

        :return: SimGroups
        """
        return SimGroups(self.com_object.GetGroups())

    def get_mesh_specifications(self) -> SimMeshSpecifications:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMeshSpecifications() As SimMeshSpecifications
                |     Returns the local mesh specification collection from the Mesh
                |     Part.
                | 
                |     See also:
                |         SimMeshSpecifications
                |     Returns:
                |         The associated collection of mesh specification.

        :return: SimMeshSpecifications
        """
        return SimMeshSpecifications(self.com_object.GetMeshSpecifications())

    def get_number_of_supports(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfSupports() As long
                |     Retrieves the number of Mesh Part supports.
                | 
                |     Parameters:
                | 
                |         oNbSupports
                |             Number of Mesh Part supports.

        :return: int
        """
        return self.com_object.GetNumberOfSupports()

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

    def get_parent_mesh_parts(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParentMeshParts() As CATSafeArrayVariant
                |     Retrieves the parent mesh parts.

        :return: tuple
        """
        return self.com_object.GetParentMeshParts()

    def get_rule_attribute(self, i_attr: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRuleAttribute(SimMeshingRuleAttr iAttr) As CATBSTR
                |     Retrieve meshing rule PLM attribute

        :param int i_attr:
        :return: str
        """
        return self.com_object.GetRuleAttribute(i_attr)

    def get_supports(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSupports() As CATSafeArrayVariant
                |     Retrieves all the Mesh Part supports from the support
                |     description.
                | 
                |     Parameters:
                | 
                |         oSupports
                |             The Mesh Part supports.

        :return: tuple
        """
        return self.com_object.GetSupports()

    def get_topology_specifications(self) -> SimTopologySpecifications:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTopologySpecifications() As SimTopologySpecifications
                |     Returns the local topology specification collection from the Mesh
                |     Part.
                | 
                |     See also:
                |         SimTopologySpecifications
                |     Returns:
                |         The associated collection of topology specifications.

        :return: SimTopologySpecifications
        """
        return SimTopologySpecifications(self.com_object.GetTopologySpecifications())

    def remove_external_reference(self, i_set_type: str, i_attribute: str, i_support: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveExternalReference(CATBSTR iSetType,CATBSTR iAttribute,AnyObject
                | iSupport)
                |     Removes an external reference corresponding to the given
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iSetType:
                |             The identifier of the set specification.
                |             Legal values: "Mesh" or "Topology". 
                |         iAttribute:
                |             The name of parameter. 
                |         iSupport:
                |             The link object that represents the geometry.
                |             PLMProductService.ComposeLink

        :param str i_set_type:
        :param str i_attribute:
        :param AnyObject i_support:
        :return: None
        """
        return self.com_object.RemoveExternalReference(i_set_type, i_attribute, i_support.com_object)

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

    def remove_support(self, i_support: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveSupport(AnyObject iSupport)
                |     Removes a support to the support description of the Mesh
                |     Part.
                | 
                |     Parameters:
                | 
                |         iSupport:
                |             The link object that represents the geometry to remove from support
                |             list.
                |             PLMProductService.ComposeLink

        :param AnyObject i_support:
        :return: None
        """
        return self.com_object.RemoveSupport(i_support.com_object)

    def set_attribute_value(self, i_set_type: str, i_attribute: str, i_value: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttributeValue(CATBSTR iSetType,CATBSTR iAttribute,CATVariant
                | iValue)
                |     Sets the value corresponding to the given parameter.
                | 
                |     Parameters:
                | 
                |         iSetType:
                |             The identifier of the set specification.
                |             Legal values: "Mesh" or "Topology". 
                |         iAttribute:
                |             The name of attribute. 
                |         iValue:
                |             The value of the global mesh attribute.

        :param str i_set_type:
        :param str i_attribute:
        :param CATVariant i_value:
        :return: None
        """
        return self.com_object.SetAttributeValue(i_set_type, i_attribute, i_value)

    def set_external_reference(self, i_set_type: str, i_attribute: str, i_support: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetExternalReference(CATBSTR iSetType,CATBSTR iAttribute,AnyObject
                | iSupport)
                |     Creates an external reference corresponding to the given
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iSetType:
                |             The identifier of the set specification.
                |             Legal values: "Mesh" or "Topology". 
                |         iAttribute:
                |             The name of parameter. 
                |         iSupport:
                |             The link object that represents the geometry.
                |             PLMProductService.ComposeLink

        :param str i_set_type:
        :param str i_attribute:
        :param AnyObject i_support:
        :return: None
        """
        return self.com_object.SetExternalReference(i_set_type, i_attribute, i_support.com_object)

    def set_mesh_parts_to_capture(self, i_mesh_parts: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMeshPartsToCapture(CATSafeArrayVariant iMeshParts)
                |     Sets the list of candidate Mesh Parts for capture.
                | 
                |     Parameters:
                | 
                |         iMeshParts:
                |             Safe array of Mesh Parts. 
                | 
                |     Example:
                | 
                |          This exemple sets the Mesh Part named "Surface Mesh.1" as Mesh Part to
                |          
                |          capture for the MyMeshPart Mesh Part:
                |          
                | 
                |          Dim captures1(0)
                |          Set captures1(0) = MyMeshParts.GetItem("Surface Mesh.1")
                |          MyMeshPart.SetMeshPartsToCapture captures1

        :param tuple i_mesh_parts:
        :return: None
        """
        return self.com_object.SetMeshPartsToCapture(i_mesh_parts)

    def set_rule(self, i_rule_name: str, i_extension: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRule(CATBSTR iRuleName,CATBSTR iExtension)
                |     Sets the Mesh Part rule.
                | 
                |     Parameters:
                | 
                |         iRuleName:
                |             The name of the rule. 
                |         iExtension:
                |             The extension of the rule.

        :param str i_rule_name:
        :param str i_extension:
        :return: None
        """
        return self.com_object.SetRule(i_rule_name, i_extension)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Launches the update of a Mesh Part.

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SimMeshPart(name="{self.name}")'
