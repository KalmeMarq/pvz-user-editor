import os
import struct
import pathlib
from PySide6 import QtWidgets
import ui.ui_select_dialog
from utils import *

class SelectUserDialog(QtWidgets.QDialog, ui.ui_select_dialog.Ui_SelectUserDialog):
  def __init__(self):
    super().__init__()

    self.setupUi(self)
    self.setWindowTitle("Select a User")

    self.settings_path = pathlib.Path("pvz_user_editor_settings.dat")

    self.add_btn.setVisible(False)
    self.del_btn.setVisible(False)
    self.dup_btn.setVisible(False)
    self.rel_btn.setEnabled(False)

    self.browse_btn.clicked.connect(self.__browse_folder)
    self.rel_btn.clicked.connect(self.__load)
    self.sel_btn.clicked.connect(self.__select_user)

    self.__load_saved_path()

  def __select_user(self):
    self.user = self.user_list[self.listWidget.currentRow()]
    self.accept()

  def __browse_folder(self):
    file_dialog = QtWidgets.QFileDialog()
    file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
    if file_dialog.exec():
      self.userdata_lineedit.setText(file_dialog.selectedFiles()[0])
      self.settings_path.write_text(file_dialog.selectedFiles()[0])
      self.__load()

  def __load_saved_path(self):
    if self.settings_path.exists() and self.settings_path.is_file():
      self.userdata_lineedit.setText(self.settings_path.read_text())
      self.__load()
      return
    
    userdata_path = None
    
    if os.name == 'nt':
      userdata_path = pathlib.Path("C:/ProgramData/PopCap Games/PlantsVsZombies/userdata")

      if not userdata_path.exists() or not userdata_path.is_dir():
        userdata_path = pathlib.Path("C:/ProgramData/Steam/PlantsVsZombies/userdata_backup")
      
      if not userdata_path.exists() or not userdata_path.is_dir():
        userdata_path = None

    elif os.name == "darwin":
      userdata_path = pathlib.Path("~/Library/Application Support/PopCap/PlantsVsZombiesMac/userdata")
      if not userdata_path.exists() or not userdata_path.is_dir():
        userdata_path = None

    if userdata_path is None:
      self.sel_btn.setEnabled(False)
      self.rel_btn.setEnabled(False)
    else:
      self.userdata_lineedit.setText(userdata_path.__str__())
      self.settings_path.write_text(userdata_path.__str__())
      self.__load()
      return

  def __load_user_list(self, filebytes, userdata_path):
    self.user_list = []
    reader = FileBinaryReader(filebytes)

    if reader.read_uint32() != 0x0E:
      return

    count = reader.read_uint16()
    for _ in range(count):
      name = reader.read_string()
      unknown0 = reader.read_uint32()
      user_index = reader.read_uint32()
      self.user_list.append({ 'name': name, 'user_index': user_index, 'unknown0': unknown0, 'filepath': userdata_path.joinpath(f"user{user_index}.dat") })

  def __load(self):
    userdata_path = pathlib.Path(self.userdata_lineedit.text())
    users_path = userdata_path.joinpath("users.dat")

    if users_path.exists() and users_path.is_file():
      filebytes = users_path.read_bytes()
      
      self.__load_user_list(filebytes, userdata_path)

      self.listWidget.clear()
        
      for user in self.user_list:
        self.listWidget.addItem(f"{user['name']}")

      if len(self.user_list) > 0:
        self.listWidget.setCurrentItem(self.listWidget.item(0))
        self.sel_btn.setEnabled(True)
        self.rel_btn.setEnabled(True)