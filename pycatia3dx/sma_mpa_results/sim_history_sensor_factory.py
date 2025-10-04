"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_results.sim_history_sensor import SimHistorySensor


class SimHistorySensorFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimHistorySensorFactory
                | 
                | Represents the history sensor factory.
                | Role:Creates and returns the history sensor object.
                | Example:
                | 
                |  Given the SimResultsAnalysisCase, you can get the SimHistorySensorFactory as
                |  mentioned below.
                |  
                | 
                |  Dim oHistSensorFactory As SimHistorySensorFactory
                |  Set oHistSensorFactory = oResultsAnalysisCase.GetItem("SimHistorySensorFactory")
                |  Dim oHistSensor As SimHistorySensor
                |  oHistSensor = oHistSensorFactory.CreateSensor
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_sensor(self) -> SimHistorySensor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSensor() As SimHistorySensor
                |     Creates a history sensor.
                | 
                |     Returns:
                |         Creates and returns the history sensor object 

        :return: SimHistorySensor
        """
        return SimHistorySensor(self.com_object.CreateSensor())

    def __repr__(self):
        return f'SimHistorySensorFactory(name="{ self.name }")'
