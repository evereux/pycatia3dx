"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeAssemble(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeAssemble
                | 
                | Represents the hybrid shape assemble feature object.
                | Role: To access the data of the hybrid shape assemble feature object. This data
                | includes:
                | 
                |     A list of the assembled elements
                |     Some methods to access this data
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAssemble
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def invert(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Invert() As boolean
                |     Returns or sets the invert mode.
                |     Legal values: True the result is inverted. False the result is not
                |     inverted.
                | 
                |     Example:
                | 
                |          This example sets the invert mode of
                |          the HybShpAssemble hybrid shape assemble feature to
                |          True.
                |          
                | 
                |          HybShpAssemble.Invert = True

        :return: bool
        """

        return self.com_object.Invert

    @invert.setter
    def invert(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Invert = value

    def add_element(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddElement(Reference iElement)
                |     Adds an element to the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iElement
                |             The element to add to the hybrid shape assemble feature
                |             object.
                |             Sub-element(s) supported (see Boundary object): Face,
                |             TriDimFeatEdge and BiDimFeatEdge. 
                | 
                |     Examples:
                |         The following example adds the iElement feature object to the
                |         HybridShapeAssemble object.
                | 
                |          HybridShapeAssemble.AddElement iElement

        :param Reference i_element:
        :return: None
        """
        return self.com_object.AddElement(i_element.com_object)

    def add_sub_element(self, i_sub_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddSubElement(Reference iSubElement)
                |     Adds a sub element to the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iSubElement
                |             The sub element to remove to the hybrid shape assemble feature
                |             object.

        :param Reference i_sub_element:
        :return: None
        """
        return self.com_object.AddSubElement(i_sub_element.com_object)

    def append_federated_element(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AppendFederatedElement(Reference iElement)
                |     Appends an init to the list of elements to federate.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Element to append. 
                | 
                |     See also:
                |         Reference

        :param Reference i_element:
        :return: None
        """
        return self.com_object.AppendFederatedElement(i_element.com_object)

    def get_angular_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAngularTolerance() As double
                |     Get the angular tolerance.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The angular tolerance.

        :return: float
        """
        return self.com_object.GetAngularTolerance()

    def get_angular_tolerance_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAngularToleranceMode() As boolean
                |     Get the angular tolerance mode.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The angular tolerance mode.

        :return: bool
        """
        return self.com_object.GetAngularToleranceMode()

    def get_connex(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetConnex() As boolean
                |     Get the connex checker flag.
                | 
                |     Parameters:
                | 
                |         oConnex

        :return: bool
        """
        return self.com_object.GetConnex()

    def get_deviation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetDeviation() As double
                |     Get the deviation value.
                | 
                |     Parameters:
                | 
                |         odeviation
                |             The deviation.

        :return: float
        """
        return self.com_object.GetDeviation()

    def get_element(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetElement(long iRank) As Reference
                |     Retrieves an element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to read. 
                | 
                |     Examples:
                |         The following example gets the oElement feature object of the
                |         HybridShapeAssemble object at the position iRank.
                | 
                |          Dim oElement As Reference
                |          Set oElement = HybridShapeAssemble.GetElement (iRank).

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetElement(i_rank))

    def get_elements_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetElementsSize() As long
                |     Returns the size of the list of elements to assemble in the hybrid shape
                |     assemble feature object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of elements in the Assemble.
                | 
                |             Example:
                |                 This example retrieves the number of elements in the
                |                 HybShpAssemble hybrid shape assemble.
                | 
                |                  Dim oSize As  long
                |                  oSize = HybShpAssemble.GetElementsSize

        :return: int
        """
        return self.com_object.GetElementsSize()

    def get_federated_element(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFederatedElement(long iRank) As Reference
                |     Retrieves an federated inits used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to read. 
                |         oElement
                |             The federated element. 
                | 
                |     See also:
                |         Reference

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetFederatedElement(i_rank))

    def get_federated_elements_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFederatedElementsSize() As long
                |     Gets the number of federated inits.
                | 
                |     Parameters:
                | 
                |         Size
                |             Number of elements.

        :return: int
        """
        return self.com_object.GetFederatedElementsSize()

    def get_federation_propagation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFederationPropagation() As long
                |     Gets the propagation mode of the federation.
                | 
                |     Parameters:
                | 
                |         i
                |             type of propagation (0: No, 1: All, 2: Continuity, 3:Tangency).

        :return: int
        """
        return self.com_object.GetFederationPropagation()

    def get_healing_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetHealingMode() As boolean
                |     Gets the healing mode for merged cells.
                | 
                |     Parameters:
                | 
                |         oHeal
                |             True = merged cells are healed, False = merged cells are not healed.

        :return: bool
        """
        return self.com_object.GetHealingMode()

    def get_manifold(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetManifold() As boolean
                |     Get the manifold checker flag.
                | 
                |     Parameters:
                | 
                |         oManifold

        :return: bool
        """
        return self.com_object.GetManifold()

    def get_simplify(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSimplify() As boolean
                |     Get the simplify flag.
                | 
                |     Parameters:
                | 
                |         oSimplify

        :return: bool
        """
        return self.com_object.GetSimplify()

    def get_sub_element(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSubElement(long iRank) As Reference
                |     Retrieves a sub element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the subelement to read.

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetSubElement(i_rank))

    def get_sub_elements_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSubElementsSize() As long
                |     Returns the size of the list of sub-elements to remove in the hybrid shape
                |     assemble feature object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of sub elements in the Assemble.
                | 
                |             Example:
                |                 This example retrieves the number of sub elements in the
                |                 HybShpAssemble hybrid shape assemble.
                | 
                |                  Dim oSize As  long
                |                  oSize = HybShpAssemble.GetSubElementsSize

        :return: int
        """
        return self.com_object.GetSubElementsSize()

    def get_suppress_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSuppressMode() As boolean
                |     Get the SuppressMode flag.
                | 
                |     Parameters:
                | 
                |         oSuppressMode

        :return: bool
        """
        return self.com_object.GetSuppressMode()

    def get_tangency_continuity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetTangencyContinuity() As boolean
                |     Get the tangency continuity checker flag.
                | 
                |     Parameters:
                | 
                |         oTangencyContinuity

        :return: bool
        """
        return self.com_object.GetTangencyContinuity()

    def remove_element(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveElement(long iRank)
                |     Removes an element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to remove. 
                | 
                |     Examples:
                |         The following example removes the feature object from the
                |         HybridShapeAssemble object at the position iRank.
                | 
                |          HybridShapeAssemble.RemoveElement iRank.

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveElement(i_rank)

    def remove_federated_element(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveFederatedElement(long iRank)
                |     Removes an element to the list of elements to federate.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Position of the element to remove.

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveFederatedElement(i_rank)

    def remove_sub_element(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSubElement(long iRank)
                |     Removes a sub element used by the hybrid shape assemble feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The rank of the element to remove.

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveSubElement(i_rank)

    def replace_element(self, i_pos: int, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ReplaceElement(long iPos,Reference iElement)
                |     Replaces the element at specified position in the hybrid shape assemble
                |     feature object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position at which the element should be replaced. 
                |         iElement
                |             Reference of the element to be inserted.
                | 
                |             Example:
                |                 This example replaces the element in the HybShpAssemble
                |                 assemble feature at specified position iPos
                | 
                |                  HybShpAssemble.ReplaceElement iPos,iElement

        :param int i_pos:
        :param Reference i_element:
        :return: None
        """
        return self.com_object.ReplaceElement(i_pos, i_element.com_object)

    def set_angular_tolerance(self, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngularTolerance(double iValue)
                |     Set the angular tolerance.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The angular tolerance.

        :param float i_value:
        :return: None
        """
        return self.com_object.SetAngularTolerance(i_value)

    def set_angular_tolerance_mode(self, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetAngularToleranceMode(boolean iValue)
                |     Set the angular tolerance mode.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The angular tolerance mode.

        :param bool i_value:
        :return: None
        """
        return self.com_object.SetAngularToleranceMode(i_value)

    def set_connex(self, i_connex: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetConnex(boolean iConnex)
                |     Set the connex checker flag.
                | 
                |     Parameters:
                | 
                |         iConnex

        :param bool i_connex:
        :return: None
        """
        return self.com_object.SetConnex(i_connex)

    def set_deviation(self, ideviation: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetDeviation(double ideviation)
                |     Set the deviation value.
                | 
                |     Parameters:
                | 
                |         ideviation
                |             The deviation.

        :param float ideviation:
        :return: None
        """
        return self.com_object.SetDeviation(ideviation)

    def set_federation_propagation(self, i_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetFederationPropagation(long iMode)
                |     Sets the propagation mode of federation.
                | 
                |     Parameters:
                | 
                |         i
                |             type of propagation (0: No, 1: All, 2: Continuity, 3:Tangency).

        :param int i_mode:
        :return: None
        """
        return self.com_object.SetFederationPropagation(i_mode)

    def set_healing_mode(self, i_heal: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetHealingMode(boolean iHeal)
                |     Sets the healing mode for merged cells.
                | 
                |     Parameters:
                | 
                |         iHeal
                |             True = merged cells are healed, False = merged cells are not healed.

        :param bool i_heal:
        :return: None
        """
        return self.com_object.SetHealingMode(i_heal)

    def set_manifold(self, i_manifold: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetManifold(boolean iManifold)
                |     Set the manifold checker flag.
                | 
                |     Parameters:
                | 
                |         iManifold

        :param bool i_manifold:
        :return: None
        """
        return self.com_object.SetManifold(i_manifold)

    def set_simplify(self, i_simplify: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSimplify(boolean iSimplify)
                |     Set the simplify flag.
                | 
                |     Parameters:
                | 
                |         iSimplify

        :param bool i_simplify:
        :return: None
        """
        return self.com_object.SetSimplify(i_simplify)

    def set_suppress_mode(self, i_suppress_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSuppressMode(boolean iSuppressMode)
                |     Set the SuppressMode flag.
                | 
                |     Parameters:
                | 
                |         iSuppressMode

        :param bool i_suppress_mode:
        :return: None
        """
        return self.com_object.SetSuppressMode(i_suppress_mode)

    def set_tangency_continuity(self, i_tangency_continuity: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetTangencyContinuity(boolean iTangencyContinuity)
                |     Set the tangency continuity checker flag.
                | 
                |     Parameters:
                | 
                |         iTangencyContinuity

        :param bool i_tangency_continuity:
        :return: None
        """
        return self.com_object.SetTangencyContinuity(i_tangency_continuity)

    def __repr__(self):
        return f'HybridShapeAssemble(name="{ self.name }")'
