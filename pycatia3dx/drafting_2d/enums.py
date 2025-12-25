from enum import Enum


class CatImportFromDrawingOption(Enum):
    CatImportAll = 0


class CatView2DModeVisu(Enum):
    catView2DModeNoShow = 0
    catView2DModeNotActivated = 1


class CatViewSide(Enum):
    catRightSide = 0
    catBottomSide = 1
    catTRCorner = 2
    catLeftSide = 3
    catBLCorner = 4
    catBRCorner = 5
    catTLCorner = 6
    catTopSide = 7


class CatViewType(Enum):
    catAuxiliaryView = 0
    catSectionCutView = 1
    catSectionView = 2


class CatVisuBackgroundMode(Enum):
    catLowIntPick = 0
    catPick = 1
    catLowIntNoPick = 2
    catNoBackground = 3
    catNoPick = 4


class CatVisuIn3DMode(Enum):
    catHideAll = 0
    catShowAll = 1


