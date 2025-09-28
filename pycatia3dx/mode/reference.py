"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Reference(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Reference
                | 
                | Represents an object pointing to another object.
                | This other object can be either a wireframe GeometricElement object such as a
                | plane or a line, or a boundary representation object such as a face, a vertex
                | or an edge. It may be, in particular, a Boundary object. References are created
                | using appropriate methods for parts. They are then passed to an object to
                | enable associativity with the referenced object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def display_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property DisplayName() As CATBSTR (Read Only)
                |     Returns the name of the referenced object. The name of the referenced
                |     object is either the name displayed in the specification tree for a
                |     GeometricElement object or a character string defining the reference for a
                |     boundary object.
                | 
                |     Example:
                |         The following example returns in StrName the displayable name of
                |         reference FirstRef:
                | 
                |          StrName = FirstRef.DisplayName

        :return: str
        """

        return self.com_object.DisplayName

    def compose_with(self, i_reference: 'Reference') -> 'Reference':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func ComposeWith(Reference iReference) As Reference
                |     Composes a reference with another reference thus creating a new composite
                |     reference.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference to be composed with the current
                |             reference.
                | 
                |             Example:
                |                 The following example returns in CompositeRef the reference
                |                 resulting from the composition of the FirstRef and SecondRef
                |                 references.
                | 
                |                  Dim CompositeRef As Reference
                |                  Set CompositeRef = FirstRef.ComposeWith(SecondRef)

        :param Reference i_reference:
        :return: Reference
        """
        return Reference(self.com_object.ComposeWith(i_reference.com_object))

    def __repr__(self):
        return f'Reference(name="{self.name}")'
