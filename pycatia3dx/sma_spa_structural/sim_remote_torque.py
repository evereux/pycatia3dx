"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimRemoteTorque(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimRemoteTorque
                | 
                | Represents the Remote Torque object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimRemoteTorque as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyRemoteTorque As SimRemoteTorque
                |      Set MyRemoteTorque = MyFeatures.Add("SimRemoteTorque")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimRemoteTorque named
                |     "Remote Torque.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyRemoteTorque As SimRemoteTorque
                |      Set MyRemoteTorque = MyFeatures.Item("Remote Torque.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimRemoteTorque as
                |     following:
                | 
                |      ...
                |      myRemoteTorque = myFeatures.Add("SimRemoteTorque")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimRemoteTorque
                |     named "Remote Torque.1" as following:
                | 
                |      ...
                |      myRemoteTorque = myFeatures.Item("Remote Torque.1")
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
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system used for the remote torque.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def feature_history(self) -> SimFeatureHistory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeatureHistory() As SimFeatureHistory (Read Only)
                |     Returns the feature history.

        :return: SimFeatureHistory
        """

        return SimFeatureHistory(self.com_object.FeatureHistory)

    @property
    def follower_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FollowerFlag() As boolean
                |     Returns or sets the flag that determines if the remote torque remains
                |     normal to the support as it deforms.
                | 
                |     TRUE: the remote torque remains normal to the support as it
                |     deforms.
                | 
                |     FALSE: the remote torque remains in its original orientation as the support
                |     deforms.

        :return: bool
        """

        return self.com_object.FollowerFlag

    @follower_flag.setter
    def follower_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FollowerFlag = value

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. See SimFeatures.GetSpecTreeCategory for usage.

        :return: str
        """

        return self.com_object.SpecTreeCategory

    def get_magnitude(self, o_fx: float, o_fy: float, o_fz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMagnitude(double oFx,double oFy,double oFz)
                |     Retrieves the magnitude.
                | 
                |     Parameters:
                | 
                |         oFx[out]
                |             X component of the remote torque. Quantity: MOMENT, units: N_m
                |             
                |         oFy[out]
                |             Y component of the remote torque. Quantity: MOMENT, units: N_m
                |             
                |         oFz[out]
                |             Z component of the remote torque. Quantity: MOMENT, units: N_m

        :param float o_fx:
        :param float o_fy:
        :param float o_fz:
        :return: None
        """
        return self.com_object.GetMagnitude(o_fx, o_fy, o_fz)

    def set_magnitude(self, i_fx: float, i_fy: float, i_fz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMagnitude(double iFx,double iFy,double iFz)
                |     Sets the magnitude.
                | 
                |     Parameters:
                | 
                |         iFx[in]
                |             X component of the remote torque. Quantity: MOMENT, units: N_m
                |             
                |         iFy[in]
                |             Y component of the remote torque. Quantity: MOMENT, units: N_m
                |             
                |         iFz[in]
                |             Z component of the remote torque. Quantity: MOMENT, units: N_m

        :param float i_fx:
        :param float i_fy:
        :param float i_fz:
        :return: None
        """
        return self.com_object.SetMagnitude(i_fx, i_fy, i_fz)

    def __repr__(self):
        return f'SimRemoteTorque(name="{ self.name }")'
