"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_spa_structural.sim_global_damping import SimGlobalDamping
from pycatia3dx.sma_spa_structural.sim_modal_damping import SimModalDamping


class SimStructuralDamping(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimStructuralDamping
                | 
                | Represents the Structural Damping object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimStructuralDamping as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyStructuralDamping As SimStructuralDamping
                |      Set MyStructuralDamping = MyFeatures.Add("SimStructuralDamping")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimStructuralDamping named
                |     "Structural Damping.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyStructuralDamping As SimStructuralDamping
                |      Set MyStructuralDamping = MyFeatures.Item("Structural Damping.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimStructuralDamping as following:
                | 
                |      ...
                |      myStructuralDamping = myFeatures.Add("SimStructuralDamping")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimStructuralDamping named "Structural Damping.1" as
                |     following:
                | 
                |      ...
                |      myStructuralDamping = myFeatures.Item("Structural Damping.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def global_damping(self) -> SimGlobalDamping:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GlobalDamping() As SimGlobalDamping (Read Only)
                |     Returns the global damping.

        :return: SimGlobalDamping
        """

        return SimGlobalDamping(self.com_object.GlobalDamping)

    @property
    def modal_damping(self) -> SimModalDamping:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModalDamping() As SimModalDamping (Read Only)
                |     Returns the modal damping. 

        :return: SimModalDamping
        """

        return SimModalDamping(self.com_object.ModalDamping)

    def __repr__(self):
        return f'SimStructuralDamping(name="{ self.name }")'
