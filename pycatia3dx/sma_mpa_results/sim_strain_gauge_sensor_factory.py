"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_results.sim_strain_gauge_sensor import SimStrainGaugeSensor


class SimStrainGaugeSensorFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimStrainGaugeSensorFactory
                | 
                | Represents the virtual strain gauge sensor factory.
                | Role:Creates and returns the virtual strain gauge sensor
                | object.
                | Example:
                | 
                |  Given the SimResultsAnalysisCase, you can get the SimStrainGaugeSensorFactory
                |  as mentioned below.
                |  
                | 
                |  Dim oStrainGaugeSensorFactory As SimStrainGaugeSensorFactory
                |  Set oStrainGaugeSensorFactory = oResultsAnalysisCase.GetItem("SimStrainGaugeSensorFactory")
                |  Dim oStrainGaugeSensor As SimStrainGaugeSensor
                |  oStrainGaugeSensor = oStrainGaugeSensorFactory.CreateSensor
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_sensor(self) -> SimStrainGaugeSensor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSensor() As SimStrainGaugeSensor
                |     Creates a strain gauge sensor.
                | 
                |     Returns:
                |         Creates and returns the strain gauge sensor object 

        :return: SimStrainGaugeSensor
        """
        return SimStrainGaugeSensor(self.com_object.CreateSensor())

    def __repr__(self):
        return f'SimStrainGaugeSensorFactory(name="{ self.name }")'
