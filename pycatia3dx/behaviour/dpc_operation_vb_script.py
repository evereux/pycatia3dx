"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.behaviour.dpc_operation import DPCOperation
from pycatia3dx.system.any_object import AnyObject


class DPCOperationVbScript(DPCOperation):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATBehaviorIDLItf.DPCOperation
                |                         DPCOperationVBScript
                | 
                | Represents the VBScript DPC operation.
                | Role: The VB script operation is designed to run a VBScript (catvbs or
                | CATScript) or a VBA macro from a VBA project. This interface derives from
                | DPCOperation. It enables the manipulation of the variables of the VBScript
                | operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_input(self, p_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetInput(CATBSTR pName) As AnyObject
                |     Returns the value of one available input of the operation.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the input 
                | 
                |     Returns:
                |         the value of the input of the operation 
                | 
                | Example:
                |     This example retrieves in OpParameter the published input CATIAParameter
                |     Nb_Cylinder currently managed by an Operation Op.
                | 
                |      Dim OpParameter as Parameter
                |      Set OpParameter = Op.GetInput("Nb_Cylinder")

        :param str p_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetInput(p_name))

    def get_internal(self, p_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetInternal(CATBSTR pName) As AnyObject
                |     Returns one available io of the operation.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the internal 
                | 
                |     Returns:
                |         value of the internal The operation has to be in executing mode,
                |         otherwise it fails
                | 
                |         Example:
                |             This example retrieves in OpParameter the internal parameter
                |             CATIAReference XXX currently managed by an Operation
                |             Op.
                | 
                |              Dim OpParameter as Parameter
                |              Set OpParameter = Op.GetInternal("XXX")

        :param str p_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetInternal(p_name))

    def get_output(self, p_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetOutput(CATBSTR pName) As AnyObject
                |     Returns the value of one available output of the
                |     operation.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the output 
                | 
                |     Returns:
                |         the value of the output of the operation 
                | 
                | Example:
                |     This example retrieves in OpPower the published output CATIAParameter Power
                |     currently managed by an Operation Op.
                | 
                |      Dim OpPower as Parameter
                |      Set OpPower = Op.GetOutput("Power")

        :param str p_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetOutput(p_name))

    def put_internal(self, p_name: str, i_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub PutInternal(CATBSTR pName,AnyObject iValue)
                |     provide output of one available io of the operation.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the internal 
                |         iValue
                |             value of the internal The operation has to be in executing mode,
                |             otherwise it fails
                | 
                |             Example:
                |                 This example assign the OpParameter containing a CATIAReference
                |                 to the internal parameter XXX currently managed by an Operation
                |                 Op.
                | 
                |                  Dim OpPower as Parameter
                |                  Op.PutInternal "XXX", OpParameter

        :param str p_name:
        :param AnyObject i_value:
        :return: None
        """
        return self.com_object.PutInternal(p_name, i_value.com_object)

    def put_output(self, p_name: str, i_value: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub PutOutput(CATBSTR pName,AnyObject iValue)
                |     Valuates an available output of the operation. The operation must be in
                |     operating state, otherwise it fails.
                |     It is applicable from a CATIABehaviorVBScript Execution.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the output 
                |         iValue
                |             the value of the output 
                | 
                |     Example:
                |         This example assigns to the published CATIAParameter Power of an
                |         Operation Op. the value of OpPower
                | 
                |          Dim OpPower as Parameter
                |          ...
                |          Op.PutOutput "Power", OpPower

        :param str p_name:
        :param AnyObject i_value:
        :return: None
        """
        return self.com_object.PutOutput(p_name, i_value.com_object)

    def test_input(self, p_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func TestInput(CATBSTR pName) As long
                |     Tests if the operation's input is set or not.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the input 
                | 
                |     Returns:
                |         indicates if the input exists 
                | 
                | Example:
                |     This example tests the existence of the value of the published
                |     CATIAParameter Nb_Cylinder currently managed by an Operation
                |     Op.
                | 
                |      if (Op.TestInput("Nb_Cylinder"))

        :param str p_name:
        :return: int
        """
        return self.com_object.TestInput(p_name)

    def test_internal(self, p_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func TestInternal(CATBSTR pName) As long
                |     Test for one available output of the Operation.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the internal 
                | 
                |     Returns:
                |         indicates if the internal exists The operation has to be in executing
                |         mode, otherwise it fails
                | 
                |         Example:
                |             This example test for the value existance of an internal parameter
                |             XXX that may contain or not a CATIAReference currently managed by an Operation
                |             Op.
                | 
                |              if (Op.TestInternal("XXX"))

        :param str p_name:
        :return: int
        """
        return self.com_object.TestInternal(p_name)

    def test_output(self, p_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func TestOutput(CATBSTR pName) As long
                |     Tests if the operation's output is set or not.
                | 
                |     Parameters:
                | 
                |         pName
                |             the name of the output 
                | 
                |     Returns:
                |         indicates if the output exists 
                | 
                | Example:
                |     This example tests the existence of the value of the published
                |     CATIAParameter Power currently managed by an Operation Op.
                | 
                |      if (Op.TestOutput("Power"))

        :param str p_name:
        :return: int
        """
        return self.com_object.TestOutput(p_name)

    def __repr__(self):
        return f'DpcOperationVbScript(name="{self.name}")'
