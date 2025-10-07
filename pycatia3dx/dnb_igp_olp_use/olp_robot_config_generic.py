"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class OLPRobotConfigGeneric(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpRobotConfigGeneric
                | 
                | A robot configuration.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A configuration is the robot posture and the turn numbers or turn signs used to
                | define a unique inverse kinematics solution for a Cartesian
                | position.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def nrl_config(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NRLConfig() As CATBSTR
                |     The native robot language config string.
                |     Property to temporarily store config information as a string during
                |     MacroUpload so that it is available during MacroSetConfigs.

        :return: str
        """

        return self.com_object.NRLConfig

    @nrl_config.setter
    def nrl_config(self, value: str):
        """
        :param str value:
        """

        self.com_object.NRLConfig = value

    @property
    def posture(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Posture() As CATBSTR
                |     The robot posture.
                |     This defines the relationship between links. You can retrieve a list of all
                |     valid postures from OlpController.Postures.

        :return: str
        """

        return self.com_object.Posture

    @posture.setter
    def posture(self, value: str):
        """
        :param str value:
        """

        self.com_object.Posture = value

    def get_posture_flag(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPostureFlag() As CATBSTR
                |     Get the posture flag based on current configuration and
                |     turns
                | 
                |     Parameters:
                | 
                |         oPostureFlag
                |             Four digit hexadecimal posture flag.

        :return: str
        """
        return self.com_object.GetPostureFlag()

    def get_turn_number(self, i_joint: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTurnNumber(short iJoint) As short
                |     Get the number of turns for a joint.
                |     This is valid only if the robot uses turn numbers.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             The joint number. The first joint is 1. The last joint is
                |             OlpController.NumJoints 
                | 
                |     Returns:
                |         The number of turns.

        :param int i_joint:
        :return: int
        """
        return self.com_object.GetTurnNumber(i_joint)

    def get_turn_sign(self, i_joint: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTurnSign(short iJoint) As DELOlpTurnSignType
                |     Get the turn sign for a joint.
                |     This is valid only if the robot uses turn signs.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             The joint number. The first joint is 1. The last joint is
                |             OlpController.NumJoints 
                | 
                |     Returns:
                |         The turn sign.

        :param int i_joint:
        :return: DELOlpTurnSignType
        """
        return self.com_object.GetTurnSign(i_joint)

    def set_posture_flag(self, i_posture_flag: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPostureFlag(CATBSTR iPostureFlag)
                |     Set the configuration and turns based on the posture flag.
                | 
                |     Parameters:
                | 
                |         iPostureFlag
                |             Four digit hexadecimal posture flag.

        :param str i_posture_flag:
        :return: None
        """
        return self.com_object.SetPostureFlag(i_posture_flag)

    def set_turn_number(self, i_joint: int, i_turns: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTurnNumber(short iJoint,short iTurns)
                |     Set the number of turns for a joint.
                |     This is valid only if the robot uses turn numbers.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             The joint number. The first joint is 1. The last joint is
                |             OlpController.NumJoints 
                |         iTurns
                |             The number of turns.

        :param int i_joint:
        :param int i_turns:
        :return: None
        """
        return self.com_object.SetTurnNumber(i_joint, i_turns)

    def set_turn_sign(self, i_joint: int, i_turns: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTurnSign(short iJoint,DELOlpTurnSignType iTurns)
                |     Set the turn sign for a joint.
                |     This is valid only if the robot uses turn signs.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             The joint number. The first joint is 1. The last joint is
                |             OlpController.NumJoints 
                |         iTurns
                |             The turn sign. 

        :param int i_joint:
        :param int i_turns:
        :return: None
        """
        return self.com_object.SetTurnSign(i_joint, i_turns)

    def __repr__(self):
        return f'OLPRobotConfigGeneric(name="{ self.name }")'
