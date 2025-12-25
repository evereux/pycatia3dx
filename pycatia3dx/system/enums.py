from enum import Enum


class CATScriptLanguage(Enum):
    CATVBScriptLanguage = 0
    CATVBALanguage = 1
    CATBasicScriptLanguage = 2
    CATJavaLanguage = 3
    CATJScriptLanguage = 4
    CATCSharpLanguage = 5
    CATVBNetLanguage = 6


class CatScriptLibraryType(Enum):
    catScriptLibraryTypeDocument = 0
    catScriptLibraryTypeDirectory = 1
    catScriptLibraryTypeVBAProject = 2
    catScriptLibraryTypeVSTAProject = 3
