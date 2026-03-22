"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.behaviour.dpc_operation import DPCOperation
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DPCOperations(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DPCOperations
                | 
                | Represents the User Operations collection currently managed from a DPC
                | Technogical Object.
                | These operations belong to one object and can be reached by the GetItem method
                | of CATIABase. For Instance onto a Root Product using
                | Product.GetItem("CATGetDPCOperations") .
                | 
                | Example:
                | 
                |      Dim RootObj As Object
                |      Set RootObj = CATIA.ActiveEditor.ActiveObject
                |      Dim MyOperations As DPCOperations
                |      Set MyOperations = RootObj.GetItem("CATGetDPCOperations")
                |      ' Display the number of User Operations 
                |      MsgBox ("There are " & MyOperations.Count & " User Operations in  " &
                |      MyOperations.Name)
                |      ' Run "MyUserOperation" User Operation
                |      Dim MyUserOperation As DPCOperation
                |      Set MyUserOperation = MyOperations.Operate("MyUserOperation")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=DPCOperation)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> DPCOperation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As DPCOperation
                |     Returns an Operation using its index or its name from the Operations
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Operation to retrieve from the
                |             collection of Operations. As a numerics, this index is the rank of the
                |             Operation in the collection. The index of the first Operation in the collection
                |             is 1, and the index of the last Operation is Count. As a string, it is the name
                |             assigned to the Operation. 
                | 
                |     Returns:
                |         The retrieved Operation 
                |     Example:
                |         This example retrieves in ThisOp the fifth Operation in the collection
                |         and in ThatOp the Operation named MyOp.
                | 
                |          Dim ThisOp As DPCOperation
                |          Set ThisOp = listOperations.Item(5)
                |          Dim ThatOp As DPCOperation
                |          Set ThatOp = listOperations.Item("MyOp")

        :param CATVariant i_index:
        :return: DPCOperation
        """
        return DPCOperation(self.com_object.Item(i_index))

    def operate(self, operation_name: str) -> DPCOperation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Operate(CATBSTR OperationName) As DPCOperation
                |     Executes a user operation of the technological object. The wanted operation
                |     is specified by its name.
                | 
                |     Parameters:
                | 
                |         OperationName
                |             The name of the operation you want to launch. 
                | 
                |     Returns:
                |         the operation

        :param str operation_name:
        :return: DPCOperation
        """
        return DPCOperation(self.com_object.Operate(operation_name))

    def __repr__(self):
        return f'DpcOperations(name="{self.name}")'
