"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.kin_mechanism.kin_command import KinCommand
from pycatia3dx.sim_rep.sim_excitation import SimExcitation


class KinRecordedExcitation(SimExcitation):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATSimRepIDLItf.SimExcitation
                |                         KinRecordedExcitation
                | 
                | Interface representing a kinematics recorded excitation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def key_frames_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeyFramesSize() As long (Read Only)
                |     Returns the size of the key frames.
                | 
                |     Example:
                | 
                |      Dim KinScenario As KinScenarioSpec
                |      ...
                |      Dim Size As Double
                |      Size = KinScenario.KeyFramesSize

        :return: int
        """

        return self.com_object.KeyFramesSize

    def get_key_frames_times(self, o_times: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetKeyFramesTimes(CATSafeArrayVariant oTimes)
                |     Gets the key frames times
                | 
                |     Parameters:
                | 
                |         oTimes
                |             Key frames times values as double.
                | 
                |             Example:
                | 
                |              Dim KinExcitation As KinRecordedExcitation
                | 
                |              Dim Size As double
                |              Size = KinExcitation.KeyFrameSize
                |              Redim Times(Size-1) As Double
                |              KinExcitation.GetKeyFramesTimes(Times)

        :param tuple o_times:
        :return: tuple
        """
        return self.com_object.GetKeyFramesTimes(o_times)

    def get_key_frames_values(self, i_kin_cmd: KinCommand, o_values: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetKeyFramesValues(KinCommand iKinCmd,CATSafeArrayVariant
                | oValues)
                |     Gets the key frames values for a kinematics command.
                | 
                |     Parameters:
                | 
                |         iKinCmd
                |             The kinematics command for which the values are obtained.
                |             
                |         oValues
                |             Key frames values as double.
                | 
                |             Example:
                | 
                |              Dim KinExcitation As KinRecordedExcitation
                |              Dim KinCommand1 As KinCommand
                |              ...
                |              Dim Size As double
                |              Size = KinExcitation.KeyFrameSize
                |              Redim Times(Size-1) As Double
                |              Call KinExcitation.GetKeyFramesValues(KinCommand1 , CmdValues
                |              )
                | 
                |              
                | 
                |     Sub SetKeyFramesTimes(CATSafeArrayVariant iTimes)
                |         Sets the key frames times
                | 
                |         Parameters:
                | 
                |             iTimes
                |                 Key frames times values as double.
                |                 The values of the key frames times should follow an ascending
                |                 chronological order. The first and last times will be set as the start and end
                |                 times of the scenario.
                | 
                |                 Example:
                |                     Set the key frames times with 2 values : 0s and 100s
                | 
                |                      Dim KinExcitation As
                |                      KinRecordedExcitation
                | 
                |                      Dim Times(1) As Double
                |                      Times(0)=0
                |                      Times(0)=100
                |                      KinExcitation.SetKeyFramesTimes(Times)
                |                      
                | 
                |         Sub SetKeyFramesValues(KinCommand iKinCmd,CATSafeArrayVariant
                |         iValues)
                |             Sets the key frame values for a kinematics
                |             command.
                | 
                |             Parameters:
                | 
                |                 iKinCmd
                |                     The kinematics command for which the values are defined.
                |                     
                |                 iValues
                |                     Key frames values as double.
                |                     Depending of the command the unit of the value must be in
                |                     mm or in deg.
                | 
                |                     Example:
                |                         Set the key frames values for a kinematic command with 2 values : 0 mm and 100 mm
                | 
                |                          Dim KinExcitation As
                |                          KinRecordedExcitation
                |                          Dim KinCommand1 As KinCommand
                |                          ...
                |                          Dim CmdValues(1) As Double
                |                          CmdValues(0)=0
                |                          CmdValues(0)=100
                |                          KinExcitation.SetKeyFramesValues KinCommand1 ,
                |                          CmdValues

        :param KinCommand i_kin_cmd:
        :param tuple o_values:
        :return: tuple
        """
        return self.com_object.GetKeyFramesValues(i_kin_cmd.com_object, o_values)

    def __repr__(self):
        return f'KinRecordedExcitation(name="{self.name}")'
