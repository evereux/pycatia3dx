"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.kin_simulation.kin_simulation_channels import KinSimulationChannels
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class KinSimulationScenarioResult(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 KinSimulationScenarioResult
                | 
                | The interface to access a scenario result of a kinematics
                | simulation.
                | The following example shows how to get a KinSimulationScenarioResult from a
                | SimulationScenarioResult. It is done thanks to the GetItem
                | method.
                | 
                | Example:
                | 
                |      
                | 
                |      Dim KinSimuResult As SimulationScenarioResult
                |      Dim KinSimuResult As KinSimulationScenarioResult
                |      Set KinSimuResult = SimuResult.GetItem("KinSimulationScenarioResult")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Name() As CATBSTR (Read Only)
                |     Returns the name of the scenario
                | 
                |     Returns:
                |         oName

        :return: str
        """

        return self.com_object.Name

    def get_result_channels(self, i_name_filtering: str, i_type_filtering: int) -> KinSimulationChannels:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetResultChannels(CATBSTR iNameFiltering,CatKinSimuChannelType
                | iTypeFiltering) As KinSimulationChannels
                |     Returns a collection of KinSimulationChannel
                | 
                |     Parameters:
                | 
                |         iNameFiltering
                |             The iNameFiltering filters the channels with a name containing this
                |             string. An empty string means that the name filtering is not applied. It is
                |             also not applied when the iTypeFiltering is the catTimeChannel type.
                |             
                |         iTypeFiltering
                |             The iTypeFiltering filters the channels with its type. Each
                |             Scenario Result has always one single Channel Time. The catEmptyChannelType
                |             value means that the type filtering is not applied.
                |             
                |         oChannels
                |             the KinSimulationChannels collection of KinSimulationChannel
                |             
                | 
                |     Example:
                | 
                |          
                | 
                |          ' ----------------------------------------
                |          ' To have all the channels
                |          ' The first channel is the Time Channel
                |          ' ----------------------------------------
                |          Dim KinSimuResult As SimulationScenarioResult
                |          Dim Channels As KinSimulationChannels
                |          Set Channels = KinSimulationResult.GetResultChannels("", catEmptyChannelType )

        :param str i_name_filtering:
        :param int i_type_filtering:
        :return: KinSimulationChannels
        """
        return KinSimulationChannels(self.com_object.GetResultChannels(i_name_filtering, i_type_filtering))

    def __repr__(self):
        return f'KinSimulationScenarioResult(name="{self.name}")'
