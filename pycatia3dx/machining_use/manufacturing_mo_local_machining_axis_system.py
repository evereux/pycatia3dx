"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingMoLocalMachiningAxisSystem(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMOLocalMachiningAxisSystem
                | 
                | Interface to set,retrieve and remove Local Machining Axis System from an
                | operation.
                | Before calling any function to get/set/remove Machining Axis System, its better
                | to check if operation supports Local Machining Axis System. It can be done
                | using function IsLocalAxisSystemSupported.
                | Role: DELMIAMfgMOLocalMachiningAxisSystem has methods to Set,retrieve and
                | remove Machining Axis System for a Machining Operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_local_axis_system(self, o_local_axis_system: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLocalAxisSystem(AnyObject oLocalAxisSystem)
                |     Returns the Machining Axis System assigned on Operation.
                | 
                |     Parameters:
                | 
                |         oLocalAxisSystem
                |             Machining Axis System assigned on Operation. It would support
                |             DELMIAMfgMachiningAxisSystem. 
                | 
                |     Returns:
                |         S_OK - if found, S_FALSE - if no axis system assigned, E_FAIL in case
                |         of error.

        :param AnyObject o_local_axis_system:
        :return: None
        """
        return self.com_object.GetLocalAxisSystem(o_local_axis_system.com_object)

    def is_local_axis_system_supported(self, o_is_supported: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsLocalAxisSystemSupported(boolean oIsSupported)
                |     Few operations support DELMIAMfgMOLocalMachiningAxisSystem but don't
                |     support Local Machining Axis System. This function checks if the operations
                |     supports Local Machining Axis System. This function must be called before
                |     Assigning/Retriving Machining Axis System.
                | 
                |     Parameters:
                | 
                |         oIsSupported
                |             TRUE - if operation supports Local Machining Axis System.
                |             
                | 
                |     Returns:
                |         S_OK - if operation supports Local Machining Axis System.

        :param bool o_is_supported:
        :return: None
        """
        return self.com_object.IsLocalAxisSystemSupported(o_is_supported)

    def remove_local_axis_system(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveLocalAxisSystem()
                |     Removes the Machining Axis System assigned on Operation. It just removes
                |     the link.
                | 
                |     Returns:
                |         S_OK in case of success

        :return: None
        """
        return self.com_object.RemoveLocalAxisSystem()

    def set_local_axis_system(self, i_local_axis_system: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLocalAxisSystem(AnyObject iLocalAxisSystem)
                |     Sets a Machining Axis System on Operation.
                | 
                |     Parameters:
                | 
                |         iLocalAxisSystem
                |             Machining Axis System to add. It should be MfgMachiningAxisSystem
                |             feature supporting DELMIAMfgMachiningAxisSystem interface.
                |             
                | 
                |     Returns:
                |         S_OK in case of success.

        :param AnyObject i_local_axis_system:
        :return: None
        """
        return self.com_object.SetLocalAxisSystem(i_local_axis_system.com_object)

    def __repr__(self):
        return f'ManufacturingMoLocalMachiningAxisSystem(name="{ self.name }")'
