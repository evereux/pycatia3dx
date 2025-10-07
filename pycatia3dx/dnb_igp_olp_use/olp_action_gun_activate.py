"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.dnb_igp_olp_use.olp_trigger_action import OLPTriggerAction


class OLPActionGunActivate(OLPTriggerAction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpTriggerAction
                |                         OlpActionGunActivate
                | 
                | A trigger action for setting the activation state of a gun.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def gun_state(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GunState() As DELOlpGunState
                |     Get/Set the gun state (on or off).

        :return: DELOlpGunState
        """

        return self.com_object.GunState

    @gun_state.setter
    def gun_state(self, value: int):
        """
        :param int value:
        """

        self.com_object.GunState = value

    @property
    def guns(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Guns() As CATSafeArrayVariant
                |     Get/Set a list of OlpGun objects this action refres to.

        :return: tuple
        """

        return self.com_object.Guns

    @guns.setter
    def guns(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.Guns = value

    @property
    def profile(self) -> OLPProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Profile() As OlpProfile
                |     Get/Set profile used for this action. 

        :return: OLPProfile
        """

        return OLPProfile(self.com_object.Profile)

    @profile.setter
    def profile(self, value: OLPProfile):
        """
        :param OLPProfile value:
        """

        self.com_object.Profile = value

    def __repr__(self):
        return f'OLPActionGunActivate(name="{ self.name }")'
