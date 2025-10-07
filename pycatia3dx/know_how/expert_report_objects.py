"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.know_how.expert_report_object import ExpertReportObject
from pycatia3dx.types.general import CATVariant


class ExpertReportObjects(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ExpertReportObjects
                | 
                | Represents the collection of (succeeded or failed) report
                | objects.
                | 
                | See also:
                |     ExpertCheckRuntime.Succeeds, ExpertCheckRuntime.Failures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def count_fail(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CountFail() As long (Read Only)
                |     Returns the number of failed tuples in the failed tuples collection. It is
                |     redundant with Collection.Count for ExpertCheckRuntime.Failures collection. For
                |     ExpertCheckRuntime.Succeeds collection, it will fail.
                | 
                |     Example:
                |         This example retrieves in ObjectNumber the number of tuples currently
                |         gathered in MyCollection.
                | 
                |          ObjectNumber = MyCollection.CountFail

        :return: int
        """

        return self.com_object.CountFail

    @property
    def count_succeed(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CountSucceed() As long (Read Only)
                |     Returns the number of succeeded tuples in the succeeded tuples collection.
                |     It is redundant with Collection.Count for ExpertCheckRuntime.Succeeds
                |     collection. For ExpertCheckRuntime.Failures collection, it will
                |     fail.
                | 
                |     Example:
                |         This example retrieves in ObjectNumber the number of tuples currently
                |         gathered in MyCollection.
                | 
                |          ObjectNumber = MyCollection.CountSucceed

        :return: int
        """

        return self.com_object.CountSucceed

    def fail_item(self, i_index: CATVariant) -> ExpertReportObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FailItem(CATVariant iIndex) As ExpertReportObject
                |     Retrieves a report failed component from a failed tuples collection, using
                |     its index or its name from the Check collection. It is redundant with
                |     ExpertReportObjects.Item for ExpertCheckRuntime.Failures collections. For
                |     ExpertCheckRuntime.Succeeds collections, it will fail.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Report component to retrieve from the
                |             collection of Report Components. As a numerics, this index is the rank of the
                |             Report component in the collection. The index of the first component in the
                |             collection is 1, and the index of the last component is Count. As a string, it
                |             is the name you assigned to the component using the AnyObject.Name property or
                |             when creating the component. 
                | 
                |     Returns:
                |         The retrieved Report component

        :param CATVariant i_index:
        :return: ExpertReportObject
        """
        return ExpertReportObject(self.com_object.FailItem(i_index))

    def item(self, i_index: CATVariant) -> ExpertReportObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As ExpertReportObject
                |     Retrieves a Report component using its index or its name from the Check
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                | 
                |             The index or the name of the Report component to retrieve from the
                |             collection of Report Components. As a numerics, this index is the rank of the
                |             Report component in the collection. The index of the first component in the
                |             collection is 1, and the index of the last component is Count. As a string, it
                |             is the name you assigned to the component using the AnyObject.Name property or
                |             when creating the component.
                | 
                |     Returns:
                |         The retrieved Report component

        :param CATVariant i_index:
        :return: ExpertReportObject
        """
        return ExpertReportObject(self.com_object.Item(i_index))

    def succeed_item(self, i_index: CATVariant) -> ExpertReportObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SucceedItem(CATVariant iIndex) As ExpertReportObject
                |     Retrieves a report component from a succeeded tuples collection, using its
                |     index or its name from the Check collection. It is redundant with
                |     ExpertReportObjects.Item for ExpertCheckRuntime.Succeeds collections. For
                |     ExpertCheckRuntime.Failures collections, it will fail.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Report component to retrieve from the
                |             collection of Report Components. As a numerics, this index is the rank of the
                |             Report component in the collection. The index of the first component in the
                |             collection is 1, and the index of the last component is Count. As a string, it
                |             is the name you assigned to the component using the AnyObject.Name property or
                |             when creating the component. 
                | 
                |     Returns:
                |         The retrieved Report component

        :param CATVariant i_index:
        :return: ExpertReportObject
        """
        return ExpertReportObject(self.com_object.SucceedItem(i_index))

    def __repr__(self):
        return f'ExpertReportObjects(name="{ self.name }")'
