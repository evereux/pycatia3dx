"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Measure(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Measure
                | 
                | Represents a Measure.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def minimum_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MinimumDistance() As double (Read Only)
                |     Returns or sets the minimum distance value for the computation of Measure
                |     Between.
                | 
                |     The minimum distance value must be greater than 0.
                | 
                |     Example:
                | 
                |             The example retrieves the minimum distance value of NewMeasure
                |             Distance.
                |             
                | 
                |             Dim MinimumValue As double
                |             MinimumValue = NewMeasure.MinimumDistance

        :return: float
        """

        return self.com_object.MinimumDistance

    def __repr__(self):
        return f'Measure(name="{self.name}")'
