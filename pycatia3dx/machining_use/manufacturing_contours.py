"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_machining_use.manufacturing_agregate import ManufacturingAgregate


class ManufacturingContours(ManufacturingAgregate):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MachiningUseItf.ManufacturingAgregate
                |                         ManufacturingContours
                | 
                | Interface to represent the features of type contour.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_element(self, i_member: AnyObject, i_notify: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddElement(AnyObject iMember,long iNotify)
                |     Adds an element in the aggregate.
                | 
                |     Parameters:
                | 
                |         iMember
                |             The element to add 
                |         iNotify
                |             The flag to indicate whether an event is sent.
                |             Legal values:
                | 
                |                 = 1 : an event is sent to notify the change
                |                 other value : no event sent

        :param AnyObject i_member:
        :param int i_notify:
        :return: None
        """
        return self.com_object.AddElement(i_member.com_object, i_notify)

    def __repr__(self):
        return f'ManufacturingContours(name="{ self.name }")'
