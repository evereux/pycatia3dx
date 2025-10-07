"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ProjectedToleranceZone(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ProjectedToleranceZone
                | 
                | Interface for accessing projected tolerance zone information of a
                | TPS.
                | ========| Position Length / |<----------->|<----------->| Toleranced | | |
                | Surface - - - +-------> +=============+ \ |\ \ \ \ | Origin Direction Projected
                | Tolerance Zone ========
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def length(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Length() As double (Read Only)
                |     Retrieves length of the projected tolerance zone (in millimeters). The
                |     length defines the ending point of the tolerance zone. This point can be
                |     computed by using Origin and Direction of the axis.

        :return: float
        """

        return self.com_object.Length

    @property
    def position(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Position() As double (Read Only)
                |     Retrieves position of the projected tolerance zone (in millimeters). The
                |     position defines the starting point of the tolerance zone. This point can be
                |     computed by using Origin and Direction of the axis.

        :return: float
        """

        return self.com_object.Position

    def get_projected_tol_zone_reference(self, op_reference: tuple) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetProjectedTolZoneReference(CATSafeArrayVariant
                | opReference)
                |     Retrieves reference axis of the projected tolerance zone. The returned
                |     point and vector define a axis system that is used to defined the 3D position
                |     of the tolerance zone.
                | 
                |     Parameters:
                | 
                |         opReference
                |             The first 3 values of opReference correspond to the X,Y and Z
                |             values of the origin point respectively and the next 3 values correspond to the
                |             X,Y and Z values of the direction respectively. 
                | 
                |     Example:
                | 
                |          This example gets the Projected Tolerance Zone reference in a VB
                |          Script
                |          Dim oTab(6) As CATSafeArrayVariant
                |          Set projTol = annotation.ProjectedToleranceZone
                |           projTol.GetProjectedTolZoneReference(oTab)
                |           oStream.Write "Projected Tol Zone Reference Point : " & oTab(0) & " " & oTab(1) & " " & oTab(2) & sLF
                |           oStream.Write "Projected Tol Zone Reference Vector : " & oTab(3) & " " & oTab(4) & " " & oTab(5) & sLF

        :param tuple op_reference:
        :return: tuple
        """
        return self.com_object.GetProjectedTolZoneReference(op_reference)

    def __repr__(self):
        return f'ProjectedToleranceZone(name="{ self.name }")'
