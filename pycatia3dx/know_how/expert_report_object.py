"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ExpertReportObject(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ExpertReportObject
                | 
                | Represents the ExpertReportObject object.
                | 
                | See also:
                |     ExpertReportObjects.Item, ExpertReportObjects.SucceedItem,
                |     ExpertReportObjects.FailItem
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def validity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Validity() As boolean (Read Only)
                |     Returns the validity of a check for a given tuple. The result depends on
                |     the result of the check for a given tuple :
                | 
                |     "True" or "False" for the tuple.

        :return: bool
        """

        return self.com_object.Validity

    def get_tuple(self, o_safe_array: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub getTuple(CATSafeArrayVariant oSafeArray)
                |     Returns a tuple (a collection of objects) concerned by this report
                |     object.
                | 
                |     Example:
                | 
                |          Dim RuleBase1 As ExpertRuleBaseRuntime
                |          Set RuleBase1 = ...
                | 
                |          Dim ListComponents As ExpertRuleBaseComponentRuntimes
                |          Set ListComponents = RuleBase1.RuleSet.ExpertRuleBaseComponentRuntimes
                | 
                |          ' Let's get a check ..
                |          Dim AComponent As ExpertRuleBaseComponentRuntime
                |          Set AComponent = ListComponents.Item("CheckOnHoles")
                | 
                |          ' .. and let's see what makes it true
                |          Dim NupletsList As ExpertReportObjects
                |          Set NupletsList = AComponent.Succeeds
                | 
                |          Dim ANuplet As ExpertReportObject
                |          Dim anArray () as Object
                |          Dim anElementArray as Object
                | 
                |          For i = 1 to AComponent.Succeeds.CountSucceed
                |            Set ANuplet = AComponent.Succeeds.SucceedItem(i)
                |            NupletSize = ANuplet.getTupleSize()
                |            ReDim anArray (NupletSize)
                |            ANuplet.getTuple(anArray)
                |            For j = LBound(anArray) to UBound(anArray)
                |              Set anElementArray = anArray(j) ' a hole
                | 
                |              ' .. some action on the element of the array
                |            Next
                |          Next
                |          
                | 
                |     Parameters:
                | 
                |         oSafeArray
                |             The collection of objects.

        :param tuple o_safe_array:
        :return: None
        """
        return self.com_object.getTuple(o_safe_array)

    def get_tuple_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func getTupleSize() As long
                |     Returns the size of the tuple concerned by this report
                |     object.
                | 
                |     Returns:
                |         Size of the tuple

        :return: int
        """
        return self.com_object.getTupleSize()

    def __repr__(self):
        return f'ExpertReportObject(name="{ self.name }")'
