"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""


class IUnknown():
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | Role: All interfaces derive from IUnknown which replaces for UNIX the native
                | Microsoft(R) IUnknown interface. This interface supplies the three basic
                | methods QueryInterface, AddRef and Release to be COM (Microsoft(R) Component
                | Object Model) compliant. These methods cannot be used in a
                | macro.
    
    """

    def __init__(self, com_object):
        self.i_unknown = com_object

    def __repr__(self):
        return f'IUnknown(name="{self.name}")'
