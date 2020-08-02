# -*- coding: utf-8 -*-
from collections import OrderedDict
from nodeeditor.node_serializable import Serializable
from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget, Serializable):

    def __init__(self, node: 'Node', parent: QWidget = None):
        self.node = node
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel("Some Title")
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QDMTextEdit("foo"))

    def setEditingFlag(self, value: bool):
        self.node.scene.getView().editingFlag = value

    def serialize(self) -> OrderedDict:
        return OrderedDict([
        ])

    def deserialize(self, data: dict, hashmap: dict = {}, restore_id: bool = True) -> bool:
        return True


class QDMTextEdit(QTextEdit):
    def focusInEvent(self, event: 'QFocusEvent'):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event: 'QFocusEvent'):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
