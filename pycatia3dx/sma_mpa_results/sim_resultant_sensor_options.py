"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_results.sim_resultant_sensor import SimResultantSensor
from pycatia3dx.types.general import CATVariant


class SimResultantSensorOptions(SimResultantSensor):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaResultsIDLItf.SimSensorBase
                |                         SMAMpaResultsIDLItf.SimResultantSensor
                |                             SimResultantSensorOptions
                | 
                | Represents the resultant sensor additional options.
                | Example:
                | 
                |  Dim oResSensorOptions As SimResultantSensorOptions
                |  Set oResSensorOptions = oResSensor.GetItem("SimResultantSensorOptions")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def set_axis_info(self, i_enum_axis_type: int, icus_selected_axis: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisInfo(SimAxisType iEnumAxisType,CATVariant
                | icusSelectedAxis)
                |     Sets the Axis information used to transform the sensor
                |     output
                | 
                |     Parameters:
                | 
                |         iEnumAxisType
                |             Specify the axis type like SimNormalTangential, SimGlobal or any
                |             other type whose axis is specified in the next agruement
                |             
                |         icusSelectedAxis
                |             Selected axis to be used for computation (for SimNormalTangential,
                |             SimGlobal, SimAxialTransverse, it is not specified)
                |             Set AxisSystem = AxisSystems.Item(1)
                |             Dim eAxisType 'As SimSelectionType
                |             eAxisType = SimModelAxis
                |             oResSensorOptions.SetAxisInfo eAxisType, AxisSystem

        :param int i_enum_axis_type:
        :param CATVariant icus_selected_axis:
        :return: None
        """
        return self.com_object.SetAxisInfo(i_enum_axis_type, icus_selected_axis)

    def set_sim_elements_selection(self, i_enum_elements_type: int, ilscus_elements: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSimElementsSelection(SimSelectionType
                | iEnumElementsType,CATSafeArrayVariant ilscusElements)
                |     Sets one or more string based elements selection for the specified
                |     type
                | 
                |     Parameters:
                | 
                |         iEnumSupportType
                |             The support type like Display groups, Node sets 
                |         ilscusSupport
                |             List of support strings of specified type Dim eSelectionType 'As SimSelectionType eElementsType = SimDisplayGroups oResSensorOptions.SetSimElementsSelection eElementsType, MyElements

        :param int i_enum_elements_type:
        :param tuple ilscus_elements:
        :return: None
        """
        return self.com_object.SetSimElementsSelection(i_enum_elements_type, ilscus_elements)

    def set_sim_support(self, i_enum_support_type: int, ilscus_support: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSimSupport(SimSelectionType iEnumSupportType,CATSafeArrayVariant
                | ilscusSupport)
                |     Sets one or more string based supports for the specified
                |     type
                | 
                |     Parameters:
                | 
                |         iEnumSupportType
                |             The support type like Display groups, Node sets 
                |         ilscusSupport
                |             List of support strings of specified type Dim eSelectionType 'As SimSelectionType eSelectionType = SimDisplayGroups oResSensorOptions.SetSimSupport eSelectionType, MySupports 

        :param int i_enum_support_type:
        :param tuple ilscus_support:
        :return: None
        """
        return self.com_object.SetSimSupport(i_enum_support_type, ilscus_support)

    def __repr__(self):
        return f'SimResultantSensorOptions(name="{ self.name }")'
