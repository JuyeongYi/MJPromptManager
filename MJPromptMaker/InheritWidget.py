from PySide6.QtWidgets import QTextEdit, QMenu
from PySide6.QtGui import QKeySequence, QAction, QShortcut, QTextCursor
from PySide6.QtCore import Qt
from functools import partial


class RemainSelection:
    def __init__(self, cursor: QTextCursor):
        self.cursor = cursor
        self.start = cursor.position()
        self.end = self.start

    def __enter__(self):
        pass


class PromptEditor(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        menu = self.createStandardContextMenu()
        menu.addSeparator()

        permuteAction = QAction("Permute Selection", self)
        permuteAction.setShortcut(QKeySequence("Ctrl+P"))
        permuteAction.triggered.connect(self.PermuteSelection)
        permuteAction.setShortcutContext(Qt.ShortcutContext.WidgetShortcut)
        menu.addAction(permuteAction)

        self.addAction(permuteAction)

        pwMenu = QMenu("Set Selection +W")
        nwMenu = QMenu("Set Selection -W")

        # manu, sign, mod

        iterSet = (
            (pwMenu, 1, "Ctrl"),
            (nwMenu, -1, "Alt")
        )

        for m, sign, mod in iterSet:
            for i in range(5):
                action = QAction(f"to {(i + 1) * 0.4 * sign:.1f}", self)
                action.setShortcut(QKeySequence(f"{mod}+{i + 1}"))
                action.setShortcutContext(Qt.ShortcutContext.WidgetShortcut)
                action.triggered.connect(partial(self.SetWeight, (i + 1) * 0.4 * sign))
                m.addAction(action)
                self.addAction(action)
            menu.addMenu(m)

        self.menu = menu

    def contextMenuEvent(self, e):
        self.menu.exec_(e.globalPos())

    def PermuteSelection(self):
        cursor = self.textCursor()
        if cursor.hasSelection():
            start = cursor.selectionStart()
            selected_text = cursor.selectedText()
            selected_text = selected_text.strip().replace("  ", ", ")
            toInsert = f"{{{selected_text}}}"
            cursor.insertText(toInsert)
            end = start + len(toInsert)

            cursor.setPosition(start)
            cursor.setPosition(end, QTextCursor.MoveMode.KeepAnchor)
            self.setTextCursor(cursor)
            self.setFocus()

    def SetWeight(self, value: float):
        cursor = self.textCursor()
        if cursor.hasSelection():
            start = cursor.selectionStart()

            selected_text = cursor.selectedText().strip()
            if "::" in selected_text:
                selected_text = selected_text.rsplit("::", 1)[0]

            toInsert = f"{selected_text}::{value:.1f}"
            cursor.insertText(toInsert)

            end = start + len(toInsert)

            cursor.setPosition(start)
            cursor.setPosition(end, QTextCursor.MoveMode.KeepAnchor)
            self.setTextCursor(cursor)
            self.setFocus()
