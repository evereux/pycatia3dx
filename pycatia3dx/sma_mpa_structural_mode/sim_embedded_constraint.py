"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimEmbeddedConstraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimEmbeddedConstraint
                | 
                | Represents the EmbeddedConstraint object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimEmbeddedConstraint as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyEmbeddedConstraint As SimEmbeddedConstraint
                |      Set MyEmbeddedConstraint = MyMCXProperties.Add("SimEmbeddedConstraint")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimEmbeddedConstraint
                |     named "EmbeddedConstraint.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyEmbeddedConstraint As SimEmbeddedConstraint
                |      Set MyEmbeddedConstraint = MyMCXProperties.Item("EmbeddedConstraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimEmbeddedConstraint as following:
                | 
                |      ...
                |      myEmbeddedConstraint = myMCXProperties.Add("SimEmbeddedConstraint")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimEmbeddedConstraint named "EmbeddedConstraint.1" as
                |     following:
                | 
                |      ...
                |      myEmbeddedConstraint = myMCXProperties.Item("EmbeddedConstraint.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def abs_exterior_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AbsExteriorTolerance() As double
                |     Returns or sets the absolute exterior tolerance. Quantity: LENGTH, units:
                |     m. This values equals to the absolute value by which nodes in the embedded
                |     element region may lie outside the host element region.

        :return: float
        """

        return self.com_object.AbsExteriorTolerance

    @abs_exterior_tolerance.setter
    def abs_exterior_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.AbsExteriorTolerance = value

    @property
    def exterior_size_fraction(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExteriorSizeFraction() As double
                |     Returns or sets the exterior size fraction. Quantity: DIMENSIONLESS, units:
                |     None This value equals to the fraction of the average size of all the
                |     non-embedded elements in the model by which embedded nodes may lie outside the
                |     host region.

        :return: float
        """

        return self.com_object.ExteriorSizeFraction

    @exterior_size_fraction.setter
    def exterior_size_fraction(self, value: float):
        """
        :param float value:
        """

        self.com_object.ExteriorSizeFraction = value

    @property
    def partial_embed_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PartialEmbedFlag() As boolean
                |     Returns or sets the flag that determines if partial embed is
                |     allowed.
                |     TRUE: Partial embed is applied.
                | 
                |     FALSE: Partial embed is not applied.

        :return: bool
        """

        return self.com_object.PartialEmbedFlag

    @partial_embed_flag.setter
    def partial_embed_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PartialEmbedFlag = value

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
    def weight_factor_roundoff(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WeightFactorRoundoff() As double
                |     Returns or sets the weight factor tolerance round off. Quantity:
                |     DIMENSIONLESS, units: None This value equal to a small value below which the
                |     weight factors of the nodes on a host element will be zeroed out. Below this
                |     value, embedded nodes are adjusted so that they lie precisely on the edge or
                |     face of the host element. 

        :return: float
        """

        return self.com_object.WeightFactorRoundoff

    @weight_factor_roundoff.setter
    def weight_factor_roundoff(self, value: float):
        """
        :param float value:
        """

        self.com_object.WeightFactorRoundoff = value

    def __repr__(self):
        return f'SimEmbeddedConstraint(name="{ self.name }")'
