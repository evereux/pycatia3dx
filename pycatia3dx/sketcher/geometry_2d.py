"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sketcher.geometric_element import GeometricElement


class Geometry2D(GeometricElement):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATSketcherIDLItf.GeometricElement
                |                         Geometry2D
                | 
                | 2D wireframe geometric element.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def construction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Construction() As boolean
                |     Returns or Sets the construction mode of the 2D geometry.
                | 
                |     Parameters:
                | 
                |         oConstruction
                |             The boolean to activate the construction mode.

        :return: bool
        """

        return self.com_object.Construction

    @construction.setter
    def construction(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Construction = value

    @property
    def report_name(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ReportName() As long
                |     Returns or Sets the report name of the 2D geometry.
                | 
                |     Parameters:
                | 
                |         oReportName
                |             The integer value of the report name

        :return: int
        """

        return self.com_object.ReportName

    @report_name.setter
    def report_name(self, value: int):
        """
        :param int value:
        """

        self.com_object.ReportName = value

    def __repr__(self):
        return f'Geometry2D(name="{ self.name }")'
