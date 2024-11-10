from os import PathLike, startfile
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass
from enum import Enum, auto
import csv

from PySide6 import QtWidgets
from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QListWidget,
                               QComboBox, QPushButton, QLabel, QListWidgetItem)
from PySide6.QtCore import Qt, Signal


class SortMode(Enum):
    Default = auto()
    Ascending = auto()
    Decending = auto()
    Priority = auto()


@dataclass
class Keyword:
    text: str
    category: str
    priority: int = 0

    def __hash__(self):
        return hash(self.text)


class KeywordManagerDialog(QDialog):
    KeywordAccepted = Signal(str)

    def __init__(self, csvPath: PathLike, parent=None):
        super().__init__(parent)

        self.csvPath = csvPath
        self.categories = set()
        self.keywordList: Set[Keyword] = set()

        self.setWindowTitle("Keyword Manager")
        self.setMinimumSize(300, 400)

        lo_main = QVBoxLayout(self)

        # 정렬 옵션
        lo_header = QHBoxLayout()
        lo_main.addLayout(lo_header)

        lb_sort = QLabel("Sort by:")
        self.combo_sort = QComboBox()
        self.combo_sort.addItems([e.name for e in SortMode])
        self.combo_sort.currentIndexChanged.connect(self.SortKeywords)
        bt_reloadCSV = QPushButton("Reload CSV")
        bt_reloadCSV.clicked.connect(self.LoadCSV)
        bt_openCSV = QPushButton("Open CSV")
        bt_openCSV.clicked.connect(self.OpenCSV)

        lo_header.addWidget(lb_sort)
        lo_header.addWidget(self.combo_sort)
        lo_header.addWidget(bt_openCSV)
        lo_header.addWidget(bt_reloadCSV)
        lo_header.addStretch()

        # 키워드 리스트
        self.list_keywords = QListWidget()
        self.list_keywords.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        lo_main.addWidget(self.list_keywords)
        self.LoadCSV()

        # 버튼
        lo_btns = QHBoxLayout()
        bt_accepted = QPushButton("Accept")
        bt_rejected = QPushButton("Reject")
        bt_accepted.clicked.connect(self.accept)
        bt_rejected.clicked.connect(self.reject)
        lo_btns.addStretch()
        lo_btns.addWidget(bt_accepted)
        lo_btns.addWidget(bt_rejected)
        lo_main.addLayout(lo_btns)

    def LoadCSV(self):
        self.keywordList.clear()
        self.categories.clear()
        with open(self.csvPath, newline='', encoding='utf-8') as csvfile:
            csvReader = csv.reader(csvfile)
            for cat, txt, priority in csvReader:
                self.categories.add(cat)
                self.keywordList.add(Keyword(txt, cat, int(priority)))
        self.SortKeywords()

    def OpenCSV(self):
        startfile(self.csvPath)

    def SortKeywords(self):
        prevKeywords = [item.data(Qt.ItemDataRole.UserRole).text for item in self.list_keywords.selectedItems()]
        self.list_keywords.clear()
        sortMode = SortMode[self.combo_sort.currentText()]

        default = lambda k: k.text

        sortKeys = {
            SortMode.Default: lambda k: (k.category, k.priority, k.text),
            SortMode.Priority: lambda k: k.priority
        }
        sortKey = sortKeys.get(sortMode, default)

        sortLabel = {
            SortMode.Default: lambda k: f"{k.category}: {k.text}",
            SortMode.Priority: lambda k: f"{k.text} ({k.priority})",
        }
        lbMaker = sortLabel.get(sortMode, default)
        reverseMode = {SortMode.Decending}

        sortedKeywords = sorted(self.keywordList, key=sortKey, reverse=sortMode in reverseMode)
        # 리스트 위젯에 추가
        for keyword in sortedKeywords:
            item = QListWidgetItem(lbMaker(keyword))
            item.setData(Qt.ItemDataRole.UserRole, keyword)
            self.list_keywords.addItem(item)
            item.setSelected(keyword.text in prevKeywords)

    def GetJoinedSelectedKeywords(self) -> str:
        selected = self.list_keywords.selectedItems()
        keywords = []
        for item in selected:
            keyword: Keyword = item.data(Qt.ItemDataRole.UserRole)
            keywords.append(keyword.text)

        return ", ".join(keywords)

    def accept(self):
        selectedKeywords = self.GetJoinedSelectedKeywords()
        self.KeywordAccepted.emit(selectedKeywords)
        super().accept()
