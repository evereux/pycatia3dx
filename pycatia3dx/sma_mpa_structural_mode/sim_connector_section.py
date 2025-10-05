"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_connector_behavior import SimConnectorBehavior


class SimConnectorSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimConnectorSection
                | 
                | Represents the Connector Section object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active_do_fs(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActiveDOFs() As CATSafeArrayVariant (Read Only)
                |     Returns the list of active DOFs. The list can contains the following values: 1 : the first translation DOF is active, 2 : the second translation DOF is active, 3 : the third translation DOF is active, 4 : the first rotation DOF is active, 5 : the second rotation DOF is active, 6 : the third rotation DOF is active.

        :return: tuple
        """

        return self.com_object.ActiveDOFs

    @property
    def assembled_connector_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AssembledConnectorType() As
                | SimConnectorSectionAssembledConnectorType
                |     Returns or sets the type of the Assembled connector.

        :return: int
        """

        return self.com_object.AssembledConnectorType

    @assembled_connector_type.setter
    def assembled_connector_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.AssembledConnectorType = value

    @property
    def connector_behavior(self) -> SimConnectorBehavior:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectorBehavior() As SimConnectorBehavior (Read
                | Only)
                |     Returns the connector behavior.

        :return: SimConnectorBehavior
        """

        return SimConnectorBehavior(self.com_object.ConnectorBehavior)

    @property
    def first_axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstAxisSystem() As SimAxisSystem (Read Only)
                |     Returns the first axis system.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.FirstAxisSystem)

    @property
    def rotational_connector_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RotationalConnectorType() As
                | SimConnectorSectionRotationalConnectorType
                |     Returns or sets the type of the Rotational connector.

        :return: int
        """

        return self.com_object.RotationalConnectorType

    @rotational_connector_type.setter
    def rotational_connector_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.RotationalConnectorType = value

    @property
    def second_axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondAxisSystem() As SimAxisSystem (Read Only)
                |     Returns the second axis system.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.SecondAxisSystem)

    @property
    def translational_connector_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TranslationalConnectorType() As
                | SimConnectorSectionTranslationalConnectorType
                |     Returns or sets the type of the Translational connector. 

        :return: int
        """

        return self.com_object.TranslationalConnectorType

    @translational_connector_type.setter
    def translational_connector_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TranslationalConnectorType = value

    def __repr__(self):
        return f'SimConnectorSection(name="{ self.name }")'
