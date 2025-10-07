"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.srs.srs_coordinate_converter import SrsCoordinateConverter


class SrsInstantiateService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SrsInstantiateService
                | 
                | Role: Allows using create Coordinate converter method.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_srs_coordinate_converter(self, op_srs_coordinate_converter: SrsCoordinateConverter) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateSrsCoordinateConverter(SrsCoordinateConverter
                | opSrsCoordinateConverter)
                |     Instantiate a SRS Coordinate Converter which can create converter absolute
                |     coordinates to SRS coordinates.
                |     Role: This method creates a new SRS Coordinate Converter.
                | 
                |         Parameters:
                | 
                |             opSrsCoordinateConverter
                |                 [out, CATBaseUnknown#Release] CATISrsCoordinateConverter. The
                |                 pointer on the SRS Coordinate Converter. 

        :param SrsCoordinateConverter op_srs_coordinate_converter:
        :return: None
        """
        return self.com_object.CreateSrsCoordinateConverter(op_srs_coordinate_converter.com_object)

    def __repr__(self):
        return f'SrsInstantiateService(name="{ self.name }")'
