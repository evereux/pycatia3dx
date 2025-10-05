"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimConnectorForce(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimConnectorForce
                | 
                | Represents the Connector Force object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimConnectorForce as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyConnectorForce As SimConnectorForce
                |      Set MyConnectorForce = MyFeatures.Add("SimConnectorForce")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimConnectorForce named
                |     "Connector Force.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyConnectorForce As SimConnectorForce
                |      Set MyConnectorForce = MyFeatures.Item("Connector Force.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimConnectorForce
                |     as following:
                | 
                |      ...
                |      myConnectorForce = myFeatures.Add("SimConnectorForce")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimConnectorForce
                |     named "Connector Force.1" as following:
                | 
                |      ...
                |      myConnectorForce = myFeatures.Item("Connector Force.1")
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
    def available_connector_components(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AvailableConnectorComponents() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of available connector components of relative
                |     motion. The list can contains the following values:
                |     1 : the first translation DOF is available,
                |     2 : the second translation DOF is available,
                |     3 : the third translation DOF is available.

        :return: tuple
        """

        return self.com_object.AvailableConnectorComponents

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
                |             X component of the force. Quantity: FORCE, units: N
                |             
                |         oFy[out]
                |             Y component of the force. Quantity: FORCE, units: N
                |             
                |         oFz[out]
                |             Z component of the force. Quantity: FORCE, units: N

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
                |             X component of the force. Quantity: FORCE, units: N
                |             
                |         iFy[in]
                |             Y component of the force. Quantity: FORCE, units: N
                |             
                |         iFz[in]
                |             Z component of the force. Quantity: FORCE, units: N

        :param float i_fx:
        :param float i_fy:
        :param float i_fz:
        :return: None
        """
        return self.com_object.SetMagnitude(i_fx, i_fy, i_fz)

    def __repr__(self):
        return f'SimConnectorForce(name="{ self.name }")'
