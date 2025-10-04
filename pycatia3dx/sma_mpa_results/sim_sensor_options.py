"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_results.sim_sensor import SimSensor


class SimSensorOptions(SimSensor):

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
                |                         SMAMpaResultsIDLItf.SimSensor
                |                             SimSensorOptions
                | 
                | Represents the sensor options to create various parameters.
                | Role:After creating the field sensor, one can set the various options provided
                | in this interface.
                | The SimSensorBase::Update method needs to be called at the end after setting
                | all the options.
                | Example:
                | 
                |  Given a sensor object, you can set the various options.
                |  
                | 
                |  Dim oSensorOptions As SimSensorOptions
                |  Set oSensorOptions = oSensor.GetItem("SimSensorOptions")
                |  oSensorOptions.SetSumParameter True
                |  oSensorOptions.SetAverageParameter True
                |  oSensorBase.Update
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def set_average_parameter(self, ib_average: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAverageParameter(boolean ibAverage)
                |     Creates the parameter with the average of all the nodes.

        :param bool ib_average:
        :return: None
        """
        return self.com_object.SetAverageParameter(ib_average)

    def set_sum_parameter(self, ib_sum: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSumParameter(boolean ibSum)
                |     Creates the parameter with sum of all the nodes. 

        :param bool ib_sum:
        :return: None
        """
        return self.com_object.SetSumParameter(ib_sum)

    def __repr__(self):
        return f'SimSensorOptions(name="{ self.name }")'
