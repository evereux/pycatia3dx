"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class OLPChoreographyEvent(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpChoreographyEvent
                | 
                | Represents a choreography event added to a motion instruction in a
                | task.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def trace_mode_after(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TraceModeAfter() As boolean
                |     Trace mode.
                |     Indicates if the event starts before or after the instruction is executed.
                |     If False it starts before, if True it starts after.

        :return: bool
        """

        return self.com_object.TraceModeAfter

    @trace_mode_after.setter
    def trace_mode_after(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TraceModeAfter = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As DELOlpChoreographyEventType (Read Only)
                |     Get the event type.

        :return: DELOlpChoreographyEventType
        """

        return self.com_object.Type

    def __repr__(self):
        return f'OLPChoreographyEvent(name="{ self.name }")'
