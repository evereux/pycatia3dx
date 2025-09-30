"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class PLMPlay(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMPlay
                | 
                | Allows to manage the execution of a playable object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def play(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Play()
                |     Plays the animation

        :return: None
        """
        return self.com_object.Play()

    def stop(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Stop()
                |     Stops the animation

        :return: None
        """
        return self.com_object.Stop()

    def __repr__(self):
        return f'PlmPlay(name="{ self.name }")'
