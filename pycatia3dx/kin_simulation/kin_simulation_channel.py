"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class KinSimulationChannel(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinSimulationChannel
                | 
                | The interface to access a result channel.
                | It corresponds to a result column as it appears in the View Scenario Results
                | window in an interactive session. The KinSimulationChannel as AnyObject offers
                | the Name property giving the name of the channel as it appears in the View
                | Scenario Results window, page Specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def channel_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ChannelSize() As long (Read Only)
                |     Returns the number of numerical values inside the channel.
                | 
                |     Returns:
                |         oChannelSize

        :return: int
        """

        return self.com_object.ChannelSize

    @property
    def channel_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ChannelType() As CatKinSimuChannelType (Read Only)
                |     Returns the KinSimulationChannel, type of the channel.
                | 
                |     Returns:
                |         oChannelType
                |         Legal Types:
                | 
                |         TimeChannel,
                |         ExcitationChanel,
                |         ProbeChannel,
                |         JointParameterChannel

        :return: int
        """

        return self.com_object.ChannelType

    @property
    def channel_unit(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ChannelUnit() As CATBSTR (Read Only)
                |     Returns the unit of the numerical values. page Table.
                | 
                |     Returns:
                |         oChannelUnity

        :return: str
        """

        return self.com_object.ChannelUnit

    def get_channel_value(self, i_index: int, o_value: float, o_is_valuated: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetChannelValue(long iIndex,double oValue,boolean
                | oIsValuated)
                |     Returns a double as the value of the input index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The input index in the channel. It starts from 1. The maximum index
                |             is given by ResultChannelSize property 
                |         oValue
                |             The channel value for the given iIndex 
                |         oIsValuated
                |             The boolean about the value existence

        :param int i_index:
        :param float o_value:
        :param bool o_is_valuated:
        :return: None
        """
        return self.com_object.GetChannelValue(i_index, o_value, o_is_valuated)

    def __repr__(self):
        return f'KinSimulationChannel(name="{self.name}")'
