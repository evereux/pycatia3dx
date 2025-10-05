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


class SimImportedForce(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimImportedForce
                | 
                | Represents the Imported Force object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimImportedForce as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyImportedForce As SimImportedForce
                |      Set MyImportedForce = MyFeatures.Add("SimImportedForce")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimImportedForce named
                |     "Imported Force.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyImportedForce As SimImportedForce
                |      Set MyImportedForce = MyFeatures.Item("Imported Force.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimImportedForce as
                |     following:
                | 
                |      ...
                |      myImportedForce = myFeatures.Add("SimImportedForce")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimImportedForce
                |     named "Imported Force.1" as following:
                | 
                |      ...
                |      myImportedForce = myFeatures.Item("Imported Force.1")
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
                |     Returns the axis system.

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
                |     Returns or sets the follower flag.
                |     TRUE: the load follows the deformation.
                |     FALSE: the load does not follows the deformation.

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

    @property
    def start_column(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartColumn() As long
                |     Returns or sets the start column.

        :return: int
        """

        return self.com_object.StartColumn

    @start_column.setter
    def start_column(self, value: int):
        """
        :param int value:
        """

        self.com_object.StartColumn = value

    @property
    def vpm_document(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VPMDocument() As CATBaseDispatch
                |     Returns or sets the VPM document. 

        :return: AnyObject
        """

        return AnyObject(self.com_object.VPMDocument)

    @vpm_document.setter
    def vpm_document(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.VPMDocument = value

    def __repr__(self):
        return f'SimImportedForce(name="{ self.name }")'
