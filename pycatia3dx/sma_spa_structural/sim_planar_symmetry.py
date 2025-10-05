"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_math_plane import SimMathPlane
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimPlanarSymmetry(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPlanarSymmetry
                | 
                | Represents the Planar Symmetry object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimPlanarSymmetry as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyPlanarSymmetry As SimPlanarSymmetry
                |      Set MyPlanarSymmetry = MyFeatures.Add("SimPlanarSymmetry")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimPlanarSymmetry named
                |     "Planar Symmetry.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyPlanarSymmetry As SimPlanarSymmetry
                |      Set MyPlanarSymmetry = MyFeatures.Item("Planar Symmetry.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimPlanarSymmetry
                |     as following:
                | 
                |      ...
                |      myPlanarSymmetry = myFeatures.Add("SimPlanarSymmetry")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimPlanarSymmetry
                |     named "Planar Symmetry.1" as following:
                | 
                |      ...
                |      myPlanarSymmetry = myFeatures.Item("Planar Symmetry.1")
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
    def plane(self) -> SimMathPlane:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Plane() As SimMathPlane (Read Only)
                |     Returns the plane of the planar symmetry restraint.

        :return: SimMathPlane
        """

        return SimMathPlane(self.com_object.Plane)

    @property
    def plane_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlaneSupport() As CATBaseDispatch (Read Only)
                |     Returns the plane support of the planar symmetry restraint.
                |     
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :return: AnyObject
        """

        return AnyObject(self.com_object.PlaneSupport)

    def __repr__(self):
        return f'SimPlanarSymmetry(name="{ self.name }")'
