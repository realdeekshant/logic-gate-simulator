from PyQt5.QtCore import *
from conf import *
from conf import register_node
from node_base import *
from nodeeditor.utils import dumpException


class GateInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("1", self)
        self.edit.setAlignment(Qt.AlignLeft)
        self.edit.setFont(QFont("Arial", 15))
        self.edit.setObjectName(self.node.content_label_objname)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


@register_node(OP_NODE_INPUT)
class GateNode_Input(GateNode):
    op_code = OP_NODE_INPUT
    op_title = "Input"
    content_label_objname = "node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[1])
        self.eval()

    def initInnerClasses(self):
        self.content = GateInputContent(self)
        self.grNode = GateGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        s_value = int(u_value)
        self.value = s_value
        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("")

        self.evalChildren()

        return self.value