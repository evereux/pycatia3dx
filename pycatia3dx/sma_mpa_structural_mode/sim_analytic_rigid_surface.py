"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_point import SimPoint
from pycatia3dx.system.any_object import AnyObject


class SimAnalyticRigidSurface(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAnalyticRigidSurface
                | 
                | Represents the Analytic Rigid Surface object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimAnalyticRigidSurface as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyAnalyticRigidSurface As SimAnalyticRigidSurface
                |      Set MyAnalyticRigidSurface = MyAbstractions.Add("SimAnalyticRigidSurface")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimAnalyticRigidSurface
                |     named "Analytic Rigid Surface.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyAnalyticRigidSurface As SimAnalyticRigidSurface
                |      Set MyAnalyticRigidSurface = MyAbstractions.Item("Analytic Rigid Surface.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimAnalyticRigidSurface as following:
                | 
                |      ...
                |      myAnalyticRigidSurface = myAbstractions.Add("SimAnalyticRigidSurface")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimAnalyticRigidSurface named "Analytic Rigid Surface.1" as
                |     following:
                | 
                |      ...
                |      myAnalyticRigidSurface = myAbstractions.Item("Analytic Rigid Surface.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def reference_point(self) -> SimPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferencePoint() As SimPoint (Read Only)
                |     Returns the reference point.

        :return: SimPoint
        """

        return SimPoint(self.com_object.ReferencePoint)

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. Possible values are:
                | 
                |         Abstractions
                |         Amplitudes
                |         Controls
                |         Connections
                |         Damping
                |         ElementTypeAssignments
                |         Envelopes
                |         FieldPlots
                |         FlowConditions
                |         HistoryPlots
                |         InitialConditions
                |         Interactions
                |         LinearLoadCases
                |         Loads
                |         LoadSets
                |         OutputRequests
                |         PredefinedFields
                |         Properties
                |         Restraints
                |         Sensors
                |         Streams
                |         ThermalConditions
                |         NotDefined

        :return: str
        """

        return self.com_object.SpecTreeCategory

    @property
    def surface_side_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SurfaceSideFlag() As boolean
                |     Returns or sets the flag that determines if the analytic rigid surface
                |     orientation is flipped with respect to the selected
                |     support.
                | 
                |     TRUE: the analytic rigid surface orientation is flipped with respect to the
                |     selected support.
                | 
                |     FALSE: the analytic rigid surface orientation is not flipped with respect
                |     to the selected support. 

        :return: bool
        """

        return self.com_object.SurfaceSideFlag

    @surface_side_flag.setter
    def surface_side_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SurfaceSideFlag = value

    def __repr__(self):
        return f'SimAnalyticRigidSurface(name="{ self.name }")'
