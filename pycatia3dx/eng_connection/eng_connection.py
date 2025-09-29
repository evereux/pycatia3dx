"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.eng_connection.assembly_constraints import AssemblyConstraints
from pycatia3dx.system.any_object import AnyObject


class EngConnection(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     EngConnection
                | 
                | Interface representing an Engineering Connection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activity() As boolean
                |     Returns/Sets the Engineering Connection Activity.

        :return: bool
        """

        return self.com_object.Activity

    @activity.setter
    def activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activity = value

    @property
    def assembly_constraints(self) -> AssemblyConstraints:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AssemblyConstraints() As AssemblyConstraints (Read
                | Only)
                |     Returns the list of Assembly contraints contained in the Engineering
                |     Connection.
                | 
                |     Parameters:
                | 
                |         oListAssemblyConstraints
                |             [out] the list of Assembly Constraints. The Assembly Constraint is
                |             identified by a CATIAAssemblyConstraint 
                | 
                |     Returns:
                | 
                |         an AssemblyConstraints
                |             if the operation is successful. 
                |         Nothing
                |             if the operation is failed.

        :return: int
        """

        return self.com_object.AssemblyConstraints

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CatEngConnectionType
                |     Returns/Sets the type of Engineering Connection.
                |     Role: The type can be "Undefined".

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def compute_equivalent_type(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeEquivalentType()
                |     Compute and set the equivalent type.

        :return: None
        """
        return self.com_object.ComputeEquivalentType()

    def get_direction(self, i_nbp: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDirection(short iNbp) As CatEngConnectionDirection
                |     Returns the direction of the Engineering Connection.
                |     Role: The direction specifies for each impacted if the instances can move
                |     .
                | 
                |     Parameters:
                | 
                |         inbp
                |             [in] Impacted instance identifier. 
                |         odir
                |             [out] the direction. 
                | 
                |     Returns:
                | 
                |         an CatEngConnectionDirection
                |             if the operation is successful. 
                |         Nothing
                |             if the operation is failed.

        :param int i_nbp:
        :return: int
        """
        return self.com_object.GetDirection(i_nbp)

    def get_impacted(self, inum_impacted: int, o_impacted: str, o_ctx_impacted: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetImpacted(short inumImpacted,CATBSTR oImpacted,CATBSTR
                | oCtxImpacted)
                |     Returns impacted.
                | 
                |     Parameters:
                | 
                |         inumImpacted
                |             [in] the impacted number. 
                |         oImpacted
                |             [out] the impacted as string:"Product.1\Product.2".
                |             
                |         oCtxImpacted
                |             [out] the context of the impacted as string.

        :param int inum_impacted:
        :param str o_impacted:
        :param str o_ctx_impacted:
        :return: None
        """
        return self.com_object.GetImpacted(inum_impacted, o_impacted, o_ctx_impacted)

    def get_nb_impacteds(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbImpacteds() As short
                |     Returns number of impacted.
                | 
                |     Parameters:
                | 
                |         onbImpacted
                |             [out] the number of impacted. 
                | 
                |     Returns:
                | 
                |         the number of impacted
                |             if the operation is successful. 
                |         Zero
                |             if the operation is failed.

        :return: int
        """
        return self.com_object.GetNbImpacteds()

    def set_direction(self, i_nbp: int, i_direction: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDirection(short iNbp,CatEngConnectionDirection
                | iDirection)
                |     Sets the direction in the Engineering Connection.
                |     Role: The direction specifies for each impacted if the instance can move.
                |     The default value is CATEngConnectionsTools::Can Move"
                | 
                |     Parameters:
                | 
                |         inbp
                |             [in] Impacted instance identifier. 
                |         odir
                |             [out] the CatEngConnectionDirection.

        :param int i_nbp:
        :param CatEngConnectionDirection i_direction:
        :return: None
        """
        return self.com_object.SetDirection(i_nbp, i_direction)

    def __repr__(self):
        return f'EngConnection(name="{self.name}")'
