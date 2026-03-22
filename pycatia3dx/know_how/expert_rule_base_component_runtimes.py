"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.know_how.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime
from pycatia3dx.types.general import CATVariant


class ExpertRuleBaseComponentRuntimes(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ExpertRuleBaseComponentRuntimes
                | 
                | Represents the collection of ExpertRuleBase (ExpertChecks, ExpertRules, and
                | ExpertRuleSets) components.
                | This collection can be seen flattened (with Item/Count) or hierarchised (with
                | ShallowItem/ShallowCount).
                | 
                | Be careful : the flattened view can be misleading. For instance,
                | if there are two ExpertChecks with the same name, you will be
                | able to access only one of them (with the methods ExpertRuleBaseComponentRuntimes.Item
                | and ExpertRuleBaseComponentRuntimes.Remove )
                | 
                | See also:
                |     ExpertRuleSetRuntime.ExpertRuleBaseComponentRuntimes
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ExpertRuleBaseComponentRuntime)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> ExpertRuleBaseComponentRuntime:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As ExpertRuleBaseComponentRuntime
                |     Returns a RuleBase component using its index or its name from the entire
                |     RuleBase collection.
                | 
                |     If several Expert components have the same name, the use of name is
                |     unpredicted.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Rule Base component to retrieve from
                |             the collection of Rule Base Components. As a numerics, this index is the rank
                |             of the Rule Base Component in the collection. The index of the first component
                |             in the collection is 1, and the index of the last component is Count. As a
                |             string, it is the name you assigned to the component using the AnyObject.Name
                |             property or when creating the component. 
                | 
                |     Returns:
                |         The retrieved Rule base component. 
                | 
                | Example:
                |     This example retrieves the last component in a RuleSet
                |     collection.
                | 
                |       Dim lastRuleBaseComponent as
                |       ExpertRuleBaseComponentRuntime
                |       Set lastRuleBaseComponent = RuleSet.Item(RuleCollection.Count)

        :param CATVariant i_index:
        :return: ExpertRuleBaseComponentRuntime
        """
        return ExpertRuleBaseComponentRuntime(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes an Expert component from the Rule Base collection. If the expert
                |     component is a RuleSet all the rules, checks and rulesets embedded in the
                |     Ruleset will be also removed.
                | 
                |     If several Expert components have the same name, the use of name is
                |     unpredicted.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the component to retrieve from the
                |             collection. As a numerics, this index is the rank of the expert component in
                |             the collection. The index of the first component in the collection is 1, and
                |             the index of the last component is Count. As a string, it is the name you
                |             assigned to the component using the AnyObject.Name property or when creating
                |             the Expert component. 
                | 
                |     Example:
                |         This example removes the Expert component named density from the RB
                |         rule base.
                | 
                |          Dim RB As ExpertRuleBase
                |          Set RB = ...
                |          Set massCheck = RB.RuleSet.ExpertRuleBaseComponentRuntimes.Remove("density")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def shallow_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ShallowCount() As long
                |     Returns the number of first-level-depth objects in the collection. This is
                |     handy to scan the objects in a collection.
                | 
                |     Returns:
                |         The number of first-level-depth objects in the
                |         collection.
                | 
                |         Example:
                |             This example retrieves in ObjectNumber the number of objects
                |             currently gathered in MyCollection.
                | 
                |              ObjectNumber = MyCollection.ShallowCount

        :return: int
        """
        return self.com_object.ShallowCount()

    def shallow_item(self, i_index: CATVariant) -> ExpertRuleBaseComponentRuntime:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ShallowItem(CATVariant iIndex) As
                | ExpertRuleBaseComponentRuntime
                |     Returns a first-level-depth RuleBase component using its index or its name
                |     from the RuleBase collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Rule Base component to retrieve from
                |             the collection of Rule Base Components. As a numerics, this index is the rank
                |             of the Rule Base Component in the collection. The index of the first component
                |             in the collection is 1, and the index of the last component is ShallowCount. As
                |             a string, it is the name you assigned to the component using the AnyObject.Name
                |             property or when creating the component. 
                | 
                |     Returns:
                |         The retrieved Rule base component. 
                | 
                | Example:
                |     This example retrieves the last component in a RuleSet
                |     collection.
                | 
                |       Dim lastRuleBaseComponent as
                |       ExpertRuleBaseComponentRuntime
                |       Set lastRuleBaseComponent = RuleSet.ShallowItem(RuleCollection.ShallowCount)

        :param CATVariant i_index:
        :return: ExpertRuleBaseComponentRuntime
        """
        return ExpertRuleBaseComponentRuntime(self.com_object.ShallowItem(i_index))

    def shallow_remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ShallowRemove(CATVariant iIndex)
                |     Removes an first-level-depth Expert component from the Rule Base
                |     collection. If the expert component is a RuleSet all the rules, checks and
                |     rulesets embedded in the Ruleset will be also removed.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the component to retrieve from the
                |             collection. As a numerics, this index is the rank of the expert component in
                |             the collection. The index of the first component in the collection is 1, and
                |             the index of the last component is ShallowCount. As a string, it is the name
                |             you assigned to the component using the AnyObject.Name property or when
                |             creating the Expert component. 
                | 
                |     Example:
                |         This example removes the Expert component named density from the
                |         relations collection.
                | 
                |          Dim RB As ExpertRuleBase
                |          Set RB = ...
                |          Set massCheck = RB.RuleSet.ExpertRuleBaseComponentRuntimes.ShallowRemove("density")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.ShallowRemove(i_index)

    def __repr__(self):
        return f'ExpertRuleBaseComponentRuntimes(name="{self.name}")'
