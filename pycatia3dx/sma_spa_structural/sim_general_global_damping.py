"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimGeneralGlobalDamping(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGeneralGlobalDamping
                | 
                | Represents the General Global Damping object.
                | 
                | Example:
                |     This example demonstrates how to retrieve the SimGeneralGlobalDamping
                |     object from a SimDirectHarmonicResponseStep. The same pattern applies to all
                |     supported steps.
                | 
                |      Dim MyDirectHarmonicResponseStep As
                |      SimDirectHarmonicResponseStep
                |      ...
                |      Dim MyGeneralGlobalDamping As SimGeneralGlobalDamping
                |      Set MyGeneralGlobalDamping = MyDirectHarmonicResponseStep.GlobalDamping
                |      
                | 
                | Example in Python:
                | 
                |      myGeneralGlobalDamping = myDirectHarmonicResponseStep.GlobalDamping
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def mass_proportional_damping(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MassProportionalDamping() As double
                |     Returns or sets the global mass proportional damping value. Quantity:
                |     DAMPINGCOEFFICIENT, units: _s

        :return: float
        """

        return self.com_object.MassProportionalDamping

    @mass_proportional_damping.setter
    def mass_proportional_damping(self, value: float):
        """
        :param float value:
        """

        self.com_object.MassProportionalDamping = value

    @property
    def modes_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModesType() As SimGeneralGlobalDampingModesType
                |     Returns or sets the modes type.

        :return: SimGeneralGlobalDampingModesType
        """

        return self.com_object.ModesType

    @modes_type.setter
    def modes_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ModesType = value

    @property
    def stiffness_proportional_damping(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StiffnessProportionalDamping() As double
                |     Returns or sets the global stiffness proportional damping value. Quantity:
                |     TIME, units: s

        :return: float
        """

        return self.com_object.StiffnessProportionalDamping

    @stiffness_proportional_damping.setter
    def stiffness_proportional_damping(self, value: float):
        """
        :param float value:
        """

        self.com_object.StiffnessProportionalDamping = value

    @property
    def structural_damping(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StructuralDamping() As double
                |     Returns or sets the global structural damping value. Quantity:
                |     DIMENSIONLESS, units: None 

        :return: float
        """

        return self.com_object.StructuralDamping

    @structural_damping.setter
    def structural_damping(self, value: float):
        """
        :param float value:
        """

        self.com_object.StructuralDamping = value

    def __repr__(self):
        return f'SimGeneralGlobalDamping(name="{ self.name }")'
