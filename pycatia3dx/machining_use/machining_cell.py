"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class MachiningCell(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MachiningCell
                | 
                | Interface to manage the machining cell.
                | Role: This interface offers services to manage the machining
                | cell.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def set_current(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCurrent()
                |     Set the machining cell current.

        :return: None
        """
        return self.com_object.SetCurrent()

    def set_current_machine(self, i_machine: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCurrentMachine(AnyObject iMachine)
                |     Set the given machine as current.

        :param AnyObject i_machine:
        :return: None
        """
        return self.com_object.SetCurrentMachine(i_machine.com_object)

    def __repr__(self):
        return f'MachiningCell(name="{ self.name }")'
