"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimDesignImprovementFeatures(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimDesignImprovementFeatures
                | 
                | Represents the Optimization Feature Set Collection.
                | 
                | Example:
                |     Given a design improvement study SimDesignImprovementStudyCase object you
                |     can retrieve a SimDesignImprovementFeatures object as
                |     following:
                | 
                |      Dim MyOptimizationCase As SimTopologyOptimizationCase
                |      ...
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      Set MyFeatures = MyOptimizationCase.Features
                |      
                | 
                | Example in Python:
                |     Given a feature SimDesignImprovementStudyCase object you can retrieve a
                |     SimDesignImprovementFeatures object as following:
                | 
                |      ...
                |      MyFeatures = MyOptimizationCase.Features
                |      
                | 
                | See also:
                |     SimAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As CATBaseDispatch
                |     Creates a Feature object and returns it.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Feature Type to be created. Possible values for iType
                |             are:
                | 
                |                 For Design Variable Features :
                |                     SimDesignEnvelope : Creates a design space feature. It is of type SimDesignEnvelope.
                |                 For Objective Features :
                |                     SimNonParametricObjective : Creates a Objective feature. It is of type SimNonParametricObjective.
                |                 For Constraint Features :
                |                     SimFrequencyConstraint : Creates a frequency constraint feature. It is of type SimFrequencyControls.
                |                     SimDisplacementConstraint : Creates a displacement constraint feature. It is of type SimDisplacementConstraint.
                |                     SimStressConstraint : Creates a stress constraint feature. It is of type SimStressConstraint.
                |                     SimFastenerForceConstraint : Creates a fastener force constraint feature. It is of type SimFastenerForceConstraint.
                |                     SimCenterOfGravityConstraint : Creates a center of gravity constraint feature. It is of type SimCenterofGravityConstraint.
                |                     SimReactionForceConstraint : Creates a reaction force constraint feature. It is of type SimReactionForceConstraint.
                |                     SimGeneralConstraint : Creates a general constraint feature. It is of type SimGeneralConstraint.
                |                 For Shape Controls Features :
                |                     SimThicknessControl : Creates an thickness control feature. It is of type SimThicknessControl.
                |                     SimSymmetryControl : Creates an symmetry control feature. It is of type SimSymmetryControl.
                |                     SimCyclicSymmetryControl : Creates a cyclic symmetry control feature. It is of type SimCyclicSymmetryControl.
                |                     SimPenetrationCheck : Creates a penetration check feature. It is of type SimPenetartionCheck.
                |                 For Manufacturing Controls Features :
                |                     SimCastingControl : Creates an casting control feature. It is of type SimCastingControl.
                |                     SimExtrusionControl : Creates an extrusion control feature. It is of type SimExtrusionControl.
                |                     SimMillingControl : Creates a milling control feature. It is of type SimMillingControl.
                |                     SimOverhangControl : Creates a overhang control feature. It is of type SimOverhangControl.
                |                     SimRibControl : Creates a rib control feature. It is of type SimRibControl.
                |                 For Response Variable Features :
                |                     SimAbsoluteMassResponseVariable : Creates an absolute mass response variable feature. It is of type SimAbsoluteMassResponseVariable.
                |                     SimCalculatedResponseVariable : Creates an calculated response variable feature. It is of type SimCalculatedResponseVariable.
                |                     SimCenterOfGravityResponseVariable : Creates a center of gravity response variable feature. It is of type SimCenterOfGravityResponseVariable.
                |                     SimDisplacementResponseVariable : Creates a displacement response variable feature. It is of type SimDisplacementResponseVariable.
                |                     SimFastenerForceResponseVariable : Creates a fastener force response variable feature. It is of type SimFastenerForceResponseVariable.
                |                     SimFrequencyResponseVariable : Creates a frequency response variable feature. It is of type SimFrequencyResponseVariable.
                |                     SimMassResponseVariable : Creates a mass response variable feature. It is of type SimMassResponseVariable.
                |                     SimMomentOfInertiaResponseVariable : Creates a moment inertia response variable feature. It is of type SimMomentOfInertiaResponseVariable.
                |                     SimReactionForceResponseVariable : Creates a reaction force response variable feature. It is of type SimReactionForceResponseVariable.
                |                     SimReactionMomentResponseVariable : Creates a moment of inertia response variable feature. It is of type SimReactionMomentResponseVariable.
                |                     SimRotationResponseVariable : Creates a rotataion response variable feature. It is of type SimRotationResponseVariable.
                |                     SimComplianceResponseVariable : Creates a compliance response variable feature. It is of type SimComplianceResponseVariable.
                |                     SimStressResponseVariable : Creates a stress response variable feature. It is of type SimStressResponseVariable.
                | 
                |     Returns:
                |         The created feature object.

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.Add(i_type)

    def add_sub_feature(self, i_type: str, i_parent: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddSubFeature(CATBSTR iType,CATBaseDispatch iParent) As
                | CATBaseDispatch
                |     Creates a Topology and Shape Design Area Sub Feature object and returns
                |     it.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Feature Type to be created. Possible values for iType
                |             are:
                | 
                |                 For Topology and Shape Optimization Sub Features
                |                 :
                |                     SimPreservedRegion : Creates a frozen region feature and is applicable only to Topology Sequence. It is of type SimPreservedRegion.
                |                     SimLocalOptimizationArea : Creates a design local optimization area feature and is applicable only to Shape Sequence. It is of type SimLocalOptimizationArea.
                |                     SimInPlaneControl : Creates a in plane control feature and is applicable only to Shape Sequence. It is of type SimInPlaneControl.
                |                     SimTransitionControl : Creates a transition control feature and is applicable only to Shape Sequence. It is of type SimTransitionControl.
                |                     iParent
                |                         The Optimization feature under which the new feature
                |                         has to be created 
                | 
                |     Returns:
                |         The created feature object.

        :param str i_type:
        :param AnyObject i_parent:
        :return: AnyObject
        """
        return self.com_object.AddSubFeature(i_type, i_parent.com_object)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Feature from the collection of Optimization
                |     Features.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Feature Set. 
                | 
                |     Returns:
                |         The retrieved feature object.

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Feature from the collection of Optimization
                |     Features.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or name of the feature object.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimDesignImprovementFeatures(name="{ self.name }")'
