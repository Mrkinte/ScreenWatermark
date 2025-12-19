from PySide6.QtWidgets import QDialog

from design.Ui_UpdateWidget import Ui_UpdateWidget
from utils.app_config import VERSION


class UpdateWidget(QDialog):
    def __init__(self, newVersion, downloadUrl, updateContent):
        super().__init__()
        self.ui = Ui_UpdateWidget()
        self.ui.setupUi(self)

        self.ui.versionLabel.setText(f"🍀发现新版本：{newVersion} （当前版本：{VERSION})")
        self.ui.contentLabel.setText(updateContent)
        self.ui.getUpdateBtn.setUrl(downloadUrl)
