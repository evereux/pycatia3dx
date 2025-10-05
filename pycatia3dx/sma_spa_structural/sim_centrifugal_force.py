"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis import SimAxis
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimCentrifugalForce(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCentrifugalForce
                | 
                | Represents the Centrifugal Force object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimCentrifugalForce as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyCentrifugalForce As SimCentrifugalForce
                |      Set MyCentrifugalForce = MyFeatures.Add("SimCentrifugalForce")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimCentrifugalForce named
                |     "Centrifugal Force.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyCentrifugalForce As SimCentrifugalForce
                |      Set MyCentrifugalForce = MyFeatures.Item("Centrifugal Force.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimCentrifugalForce
                |     as following:
                | 
                |      ...
                |      myCentrifugalForce = myFeatures.Add("SimCentrifugalForce")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimCentrifugalForce named "Centrifugal Force.1" as
                |     following:
                | 
                |      ...
                |      myCentrifugalForce = myFeatures.Item("Centrifugal Force.1")
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
    def line(self) -> SimAxis:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Line() As SimAxis (Read Only)
                |     Returns the line of the centrifugal force. The graphical user interface
                |     editor for this feature only supports geometric axis types. See SimAxisAxisType
                |     for additional information.

        :return: SimAxis
        """

        return SimAxis(self.com_object.Line)

    @property
    def rotational_velocity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RotationalVelocity() As double
                |     Rotational velocity of the centrifugal force. Quantity: ANGULAR_VELOCITY,
                |     units: turn_mn 

        :return: float
        """

        return self.com_object.RotationalVelocity

    @rotational_velocity.setter
    def rotational_velocity(self, value: float):
        """
        :param float value:
        """

        self.com_object.RotationalVelocity = value

    def __repr__(self):
        return f'SimCentrifugalForce(name="{ self.name }")'
