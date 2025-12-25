from enum import Enum


class CatImportFromDrawingOption(Enum):
    CatImportAll = 0


class CatView2DModeVisu(Enum):
    catView2DModeNotActivated = 0
    catView2DModeNoShow = 1


class CatViewSide(Enum):
    catTopSide = 0
    catBottomSide = 1
    catLeftSide = 2
    catRightSide = 3
    catTLCorner = 4
    catTRCorner = 5
    catBLCorner = 6
    catBRCorner = 7


class CatViewType(Enum):
    catAuxiliaryView = 0
    catSectionView = 1
    catSectionCutView = 2


class CatVisuBackgroundMode(Enum):
    catNoBackground = 0
    catPick = 1
    catNoPick = 2
    catLowIntPick = 3
    catLowIntNoPick = 4


class CatVisuIn3DMode(Enum):
    catShowAll = 0
    catHideAll = 1
