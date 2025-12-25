from enum import Enum


class CATScriptLanguage(Enum):
    CATJScriptLanguage = 0
    CATVBScriptLanguage = 1
    CATJavaLanguage = 2
    CATVBNetLanguage = 3
    CATVBALanguage = 4
    CATBasicScriptLanguage = 5
    CATCSharpLanguage = 6


class CatScriptLibraryType(Enum):
    catScriptLibraryTypeDirectory = 0
    catScriptLibraryTypeDocument = 1
    catScriptLibraryTypeVBAProject = 2
    catScriptLibraryTypeVSTAProject = 3


