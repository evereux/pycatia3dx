"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_choreography_event import OLPChoreographyEvent


class OLPChoreographyEvents(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpChoreographyEvents
                | 
                | Object to manage the choreography events for a robot motion.
                | 
                | see OlpRobotMotionTarget.Choreography This interface can only be used by a
                | translator within the Robotics Off-line Programming (OLP) Download or Upload
                | command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_and_append_event(self, i_type: int) -> OLPChoreographyEvent:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateAndAppendEvent(DELOlpChoreographyEventType iType) As
                | OlpChoreographyEvent
                |     Create a choreography event.
                |     The new event is returned and is appended to the list of events for this
                |     move.

        :param int i_type:
        :return: OLPChoreographyEvent
        """
        return OLPChoreographyEvent(self.com_object.CreateAndAppendEvent(i_type))

    def delete_event(self, i_event: OLPChoreographyEvent) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteEvent(OlpChoreographyEvent iEvent)
                |     Delete a choreography event.

        :param OLPChoreographyEvent i_event:
        :return: None
        """
        return self.com_object.DeleteEvent(i_event.com_object)

    def item(self, i_index: int) -> OLPChoreographyEvent:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As OlpChoreographyEvent
                |     Get a choreography event.
                |     Index starts at 1. 

        :param int i_index:
        :return: OLPChoreographyEvent
        """
        return OLPChoreographyEvent(self.com_object.Item(i_index))

    def __repr__(self):
        return f'OLPChoreographyEvents(name="{ self.name }")'
