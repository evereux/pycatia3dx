"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimEulerianMaterialAssignment(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimEulerianMaterialAssignment
                | 
                | Represents the Eulerian Material Assignment object.
                | 
                | Example:
                |     Given a SimEulerianProperty object, you can create a
                |     SimEulerianMaterialAssignment as following:
                | 
                |      Dim MyEulerianProperty As SimEulerianProperty
                |      ...
                |      Dim MyMaterialAssignments As
                |      SimEulerianMaterialAssignments
                |      Set MyMaterialAssignments = MyEulerianProperty.MaterialAssignments
                |      ...
                |      Dim MyMaterialAssignment As SimEulerianMaterialAssignment
                |      Set MyMaterialAssignment = MyMaterialAssignments.Add
                |      
                | 
                |     Given a SimEulerianProperty object, you can retrieve a
                |     SimEulerianMaterialAssignment named "Eulerian Material Assignment.1" as
                |     following:
                | 
                |      Dim MyEulerianProperty As SimEulerianProperty
                |      ...
                |      Dim MyMaterialAssignments As
                |      SimEulerianMaterialAssignments
                |      Set MyMaterialAssignments = MyEulerianProperty.MaterialAssignments
                |      ...
                |      Dim MyMaterialAssignment As SimEulerianMaterialAssignment
                |      Set MyMaterialAssignment = MyMaterialAssignments.Item("Eulerian Material Assignment.1")
                |      
                | 
                | Example in Python:
                |     Given a SimEulerianProperty object myEulerianProperty, you can create a
                |     SimEulerianMaterialAssignment as following:
                | 
                |      ...
                |      myMaterialAssignments = myEulerianProperty.MaterialAssignments
                |      ...
                |      myMaterialAssignment = myMaterialAssignments.Add
                |      
                | 
                |     Given a SimEulerianProperty object myEulerianProperty, you can retrieve a
                |     SimEulerianMaterialAssignment named "Eulerian Material Assignment.1" as
                |     following:
                | 
                |      ...
                |      myMaterialAssignments = myEulerianProperty.MaterialAssignments
                |      ...
                |      myMaterialAssignment = myMaterialAssignments.Item("Eulerian Material Assignment.1")
                |      
                | 
                | See also:
                |     SMAIAMpaEulerianMaterialAssignments
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def material_behavior(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehavior() As CATBaseDispatch
                |     Returns or sets the simulation material behavior.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MaterialBehavior)

    @material_behavior.setter
    def material_behavior(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.MaterialBehavior = value

    @property
    def material_behavior_by_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialBehaviorByName() As CATBSTR
                |     Returns or sets the simulation material behavior by name.

        :return: str
        """

        return self.com_object.MaterialBehaviorByName

    @material_behavior_by_name.setter
    def material_behavior_by_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.MaterialBehaviorByName = value

    @property
    def material_location(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialLocation() As SimEulerianMaterialLocation
                |     Returns or Sets the Material Location used for the Eulerian Material
                |     Assignment (only for Computed Volume Fraction Type).

        :return: SimEulerianMaterialLocation
        """

        return self.com_object.MaterialLocation

    @material_location.setter
    def material_location(self, value: int):
        """
        :param int value:
        """

        self.com_object.MaterialLocation = value

    @property
    def volume_fraction_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VolumeFractionType() As SimEulerianVolumeFractionType
                |     Returns or Sets the Volume Fraction Type used for the Eulerian Material
                |     Assignment. 

        :return: SimEulerianVolumeFractionType
        """

        return self.com_object.VolumeFractionType

    @volume_fraction_type.setter
    def volume_fraction_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VolumeFractionType = value

    def __repr__(self):
        return f'SimEulerianMaterialAssignment(name="{ self.name }")'
