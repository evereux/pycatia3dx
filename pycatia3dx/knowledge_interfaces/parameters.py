"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.bool_param import BoolParam
from pycatia3dx.knowledge_interfaces.dimension import Dimension
from pycatia3dx.knowledge_interfaces.int_param import IntParam
from pycatia3dx.knowledge_interfaces.list_parameter import ListParameter
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.knowledge_interfaces.parameter_set import ParameterSet
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.knowledge_interfaces.str_param import StrParam
from pycatia3dx.knowledge_interfaces.units import Units
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Parameters(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Parameters
                | 
                | Represents the Parameters collection of the part or the
                | product.
                | The following example shows how to retrieve it:
                | 
                |  Dim part1 As Part
                |  Set part1 = ...
                |  Dim parameterList As Parameters
                |  Set parameterList = part1.Parameters
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def root_parameter_set(self) -> ParameterSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property RootParameterSet() As ParameterSet (Read Only)
                |     Returns the root parameter set of a 3D Shape. If it doesn't exist, it is
                |     created.

        :return: ParameterSet
        """

        return ParameterSet(self.com_object.RootParameterSet)

    @property
    def units(self) -> Units:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Units() As Units (Read Only)
                |     Returns the collection of units.

        :return: Units
        """

        return Units(self.com_object.Units)

    def create_boolean(self, i_name: str, i_value: bool) -> BoolParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateBoolean(CATBSTR iName,boolean iValue) As BoolParam
                |     Creates a boolean parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Returns:
                |         The parameter created 
                | 
                | Example:
                |     This example creates the checked boolean parameter and adds it to the newly
                |     created part:
                | 
                |      Dim part1 as Part
                |      Set part1 = ...
                |      Dim chk As BooleanParam
                |      Set chk = part1.Parameters.CreateBoolean ("checked", False)

        :param str i_name:
        :param bool i_value:
        :return: BoolParam
        """
        return BoolParam(self.com_object.CreateBoolean(i_name, i_value))

    def create_dimension(self, i_name: str, i_magnitude: str, i_value: float) -> Dimension:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateDimension(CATBSTR iName,CATBSTR iMagnitude,double iValue) As
                | Dimension
                |     Creates a user dimension and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The dimension name. 
                |         iMagnitude
                |             The dimension magnitude. Units are those of the IS system. Valid
                |             magnitudes are:
                | 
                |                 "LENGTH": the unit is the meter.
                |                 "ANGLE": the unit is the radian. 
                | 
                |             The Dimension object provides the Dimension.ValuateFromString
                |             method with which you may express the value in any unit for a given dimension
                |             (see the example below). 
                |         iValue
                |             The dimension value provided as a real number. 
                | 
                |     Returns:
                |         The parameter created 
                |     Example:
                |         This example creates a LENGTH dimension and adds it to the newly
                |         created part. The initial value is expressed in meters. The new value is
                |         expressed in millimeters.
                | 
                |          Dim depth As Dimension
                |          Set depth = parameters.CreateDimension("depth", "LENGTH", 20)
                |          depth.ValuateFromString("300mm");

        :param str i_name:
        :param str i_magnitude:
        :param float i_value:
        :return: Dimension
        """
        return Dimension(self.com_object.CreateDimension(i_name, i_magnitude, i_value))

    def create_integer(self, i_name: str, i_value: int) -> IntParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateInteger(CATBSTR iName,long iValue) As IntParam
                |     Creates an integer parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Returns:
                |         The parameter created 
                | 
                | Example:
                |     This example creates the RevisionNumber integer parameter and adds it to
                |     the newly created part:
                | 
                |      Dim part1 as Part
                |      Set part1 = ...
                |      Dim revision As IntParam
                |      Set revision = part1.Parameters.CreateInteger ("RevisionNumber", 17)

        :param str i_name:
        :param int i_value:
        :return: IntParam
        """
        return IntParam(self.com_object.CreateInteger(i_name, i_value))

    def create_list(self, i_name: str) -> ListParameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateList(CATBSTR iName) As ListParameter
                |     Creates a list parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                | 
                |     Returns:
                |         The list created 
                | 
                | Example:
                |     This example creates the ListName list parameter and adds it to the newly
                |     created part:
                | 
                |      Dim part1 as Part
                |      Set part1 = ...
                |      Set list1 = part1.Parameters.CreateList ("ListName")

        :param str i_name:
        :return: ListParameter
        """
        return ListParameter(self.com_object.CreateList(i_name))

    def create_real(self, i_name: str, i_value: float) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateReal(CATBSTR iName,double iValue) As RealParam
                |     Creates a real parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Returns:
                |         the real parameter created 
                | 
                | Example:
                |     This example creates the ReliabilityRate real parameter and adds it to the
                |     newly created part:
                | 
                |      Dim part1 as Part
                |      Set part1 = ...
                |      Dim rate As RealParam
                |      Set rate = part1.Parameters.CreateReal ("ReliabilityRate", 2.5 )

        :param str i_name:
        :param float i_value:
        :return: RealParam
        """
        return RealParam(self.com_object.CreateReal(i_name, i_value))

    def create_set_of_parameters(self, i_father: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub CreateSetOfParameters(AnyObject iFather)
                |     Creates a set of parameters and appends it to argument
                |     iFather.
                | 
                |     Parameters:
                | 
                |         iFather
                |             The object to aggregate the set

        :param AnyObject i_father:
        :return: None
        """
        return self.com_object.CreateSetOfParameters(i_father.com_object)

    def create_string(self, i_name: str, i_value: str) -> StrParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateString(CATBSTR iName,CATBSTR iValue) As StrParam
                |     Creates a string parameter and adds it to the part's collection of
                |     parameters.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name 
                |         iValue
                |             The parameter value 
                | 
                |     Returns:
                |         the string parameter created 
                | 
                | Example:
                |     This example creates the responsible string parameter and adds it to the
                |     newly created part:
                | 
                |      Dim part1 as Part
                |      Set part1 = ...
                |      Set density = part1.Parameters.CreateString ("responsible", "The Boss")

        :param str i_name:
        :param str i_value:
        :return: StrParam
        """
        return StrParam(self.com_object.CreateString(i_name, i_value))

    def get_name_to_use_in_relation(self, i_object: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetNameToUseInRelation(AnyObject iObject) As CATBSTR
                |     Returns a correct name of a feature to use it in a
                |     relation.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The feature to use in relation 
                | 
                |     Returns:
                |         The name of the feature

        :param AnyObject i_object:
        :return: str
        """
        return self.com_object.GetNameToUseInRelation(i_object.com_object)

    def item(self, i_index: CATVariant) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As Parameter
                |     Retrieves a parameter using its index or its name from the
                |     Parameters collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the parameter to retrieve from the
                |             collection of parameters. As a numerics, this index is the rank of the
                |             parameter in the collection. The index of the first parameter in the collection
                |             is 1, and the index of the last parameter is Count. As a string, it is the name
                |             you assigned to the parameter using the AnyObject.Name property or when
                |             creating the parameter. 
                | 
                |     Returns:
                |         parameter retrieved 
                |     Example:
                |         This example retrieves the last parameter in the parameters
                |         collection:
                | 
                |          Set lastParameter = parameters.Item(parameters.Count)

        :param CATVariant i_index:
        :return: Parameter
        """
        return Parameter(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Remove(CATVariant iIndex)
                |     Removes a parameter from the Parameters collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the parameter to remove from the
                |             collection of parameters. As a numerics, this index is the rank of the
                |             parameter in the collection. The index of the first parameter in the collection
                |             is 1, and the index of the last parameter is Count. As a string, it is the name
                |             you assigned to the parameter using the AnyObject.Name property or when
                |             creating the parameter. 
                |         Example:
                |             This example removes the "depth" parameter from the parameters
                |             collection.
                | 
                |              parameters.Remove("depth")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def sub_list(self, i_object: AnyObject, i_recursively: bool) -> 'Parameters':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func SubList(AnyObject iObject,boolean iRecursively) As
                | Parameters
                |     Returns a sub-collection of parameters aggregated to an
                |     object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object used to filter the whole parameter collection to get the
                |             resulting sub-collection. 
                |         iRecursively
                |             A flag to specify if children parameters are to be searched for in
                |             the returned collection 
                | 
                |     Returns:
                |         the list of parameters 
                |     Example:
                |         This example shows how to retrieve a collection of parameters that are
                |         associated to a Pad.
                | 
                |          Dim part1 as Part
                |          Set part1 = ...
                |          Dim Parameters1 As Parameters
                |          Set Parameters1 = part1.Parameters ' gets the collection of parameters in the part
                |          Dim Body0 As AnyObject
                |          Set Body0 = part1.Bodies.Item  ( "MechanicalTool.1" ) 
                |          Dim Pad1 As AnyObject
                |          Set Pad1 = Body0.Shapes.Item  ( "Pad.1" ) ' gets the pad Pad.1
                |          Dim Parameters2 As Parameters
                |          Set Parameters2 = Parameters1.SubList(Pad1,TRUE) ' gets the collection of parameters that are under the pad Pad.1

        :param AnyObject i_object:
        :param bool i_recursively:
        :return: Parameters
        """
        return Parameters(self.com_object.SubList(i_object.com_object, i_recursively))

    def __repr__(self):
        return f'Parameters(name="{ self.name }")'
