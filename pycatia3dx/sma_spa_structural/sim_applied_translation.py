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


class SimAppliedTranslation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAppliedTranslation
                | 
                | Represents the Applied Translation object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimAppliedTranslation as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAppliedTranslation As SimAppliedTranslation
                |      Set MyAppliedTranslation = MyFeatures.Add("SimAppliedTranslation")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimAppliedTranslation named
                |     "Applied Translation.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAppliedTranslation As SimAppliedTranslation
                |      Set MyAppliedTranslation = MyFeatures.Item("Applied Translation.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimAppliedTranslation as following:
                | 
                |      ...
                |      myAppliedTranslation = myFeatures.Add("SimAppliedTranslation")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimAppliedTranslation named "Applied Translation.1" as
                |     following:
                | 
                |      ...
                |      myAppliedTranslation = myFeatures.Item("Applied Translation.1")
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
    def dof(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Dof() As SimDof
                |     Returns or sets the degree of freedom on which the translation is applied.

        :return: int
        """

        return self.com_object.Dof

    @dof.setter
    def dof(self, value: int):
        """
        :param int value:
        """

        self.com_object.Dof = value

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
    def magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Magnitude() As double
                |     Returns or sets the magnitude. Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.Magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.Magnitude = value

    @property
    def orthogonal_translations_fixed_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrthogonalTranslationsFixedFlag() As boolean
                |     Returns or sets the flag that determines if the other DOFs are
                |     restrained.
                | 
                |     TRUE: the other DOFs are restrained.
                | 
                |     FALSE: the other DOFs are free.

        :return: bool
        """

        return self.com_object.OrthogonalTranslationsFixedFlag

    @orthogonal_translations_fixed_flag.setter
    def orthogonal_translations_fixed_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OrthogonalTranslationsFixedFlag = value

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

    def __repr__(self):
        return f'SimAppliedTranslation(name="{ self.name }")'
