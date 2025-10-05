"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimShellEdgeLoad(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimShellEdgeLoad
                | 
                | Represents the Shell Edge Load object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimShellEdgeLoad as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyShellEdgeLoad As SimShellEdgeLoad
                |      Set MyShellEdgeLoad = MyFeatures.Add("SimShellEdgeLoad")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimShellEdgeLoad named
                |     "Shell Edge Load.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyShellEdgeLoad As SimShellEdgeLoad
                |      Set MyShellEdgeLoad = MyFeatures.Item("Shell Edge Load.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimShellEdgeLoad as
                |     following:
                | 
                |      ...
                |      myShellEdgeLoad = myFeatures.Add("SimShellEdgeLoad")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimShellEdgeLoad
                |     named "Shell Edge Load.1" as following:
                | 
                |      ...
                |      myShellEdgeLoad = myFeatures.Item("Shell Edge Load.1")
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
    def force_per_length(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ForcePerLength() As double
                |     Returns or sets the force per length. Quantity: FORCE_PER_LENGTH, Units:
                |     kg_s2.

        :return: float
        """

        return self.com_object.ForcePerLength

    @force_per_length.setter
    def force_per_length(self, value: float):
        """
        :param float value:
        """

        self.com_object.ForcePerLength = value

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

    @property
    def traction_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TractionType() As SimShellEdgeLoadTractionType
                |     Returns or sets the traction type. 

        :return: SimShellEdgeLoadTractionType
        """

        return self.com_object.TractionType

    @traction_type.setter
    def traction_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TractionType = value

    def __repr__(self):
        return f'SimShellEdgeLoad(name="{ self.name }")'
