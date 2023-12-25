import copy
import sys
import struct
import pathlib
from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QItemSelection, Qt
from PySide6.QtGui import QCloseEvent, QKeyEvent
from PySide6.QtWidgets import QWidget
import select_dialog
import edit_window

def deep_equals(value0, value1):
  if value0 is None or value1 is None:
    return False

  if isinstance(value0, dict) and isinstance(value1, dict):
    if len(value0) != len(value1):
      return False

    for key in value0:
      if key not in value1:
        return False
      if not deep_equals(value0[key], value1[key]):
        return False
      
    return True

  if (isinstance(value0, list) and isinstance(value1, list)) or (isinstance(value0, tuple) and isinstance(value1, tuple)):
    if len(value0) != len(value1):
      return False
    
    for i,item in enumerate(value0):
      if not deep_equals(item, value1[i]):
        return False

    return True

  return value0 == value1

class SelectUserDialog(QtWidgets.QDialog):
  def __init__(self):
    super().__init__()
    self.ui = select_dialog.Ui_Dialog()
    self.ui.setupUi(self)
    self.setWindowTitle("Select a user")
    self.ui.pushButton.clicked.connect(self.select_user)
    self.ui.pushButton_2.clicked.connect(self.browse_folder)

    self.list_model = QtCore.QStringListModel()
    self.ui.listView.setModel(self.list_model)
    self.ui.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    settings_path = pathlib.Path("settings")
    if settings_path.exists() and settings_path.is_file():
      self.ui.lineEdit.setText(settings_path.read_text())
      self.load()
    else:
      self.ui.pushButton.setEnabled(False)

  def load(self):
    userdata_path = pathlib.Path(self.ui.lineEdit.text())
    users_path = userdata_path.joinpath("users.dat")

    if users_path.exists() and users_path.is_file():
      filebytes = users_path.read_bytes()
      count = struct.unpack_from("<H", filebytes, 0x4)[0]
      self.list_model.removeRows(0, self.list_model.rowCount())
      if self.list_model.insertRows(0, count):
        self.user_list = []
        
        cur = 0x6
        for i in range(0, count):
          name_len = struct.unpack_from("<H", filebytes, cur)[0]
          cur += 2
          name = filebytes[cur:(cur + name_len)].decode('utf-8')
          cur += name_len
          cur += 4
          user_index = struct.unpack("<I", filebytes[cur:(cur + 4)])[0]
          self.user_list.append({ 'name': name, 'user_index': user_index, 'filepath': userdata_path.joinpath(f"user{user_index}.dat") })
          cur += 4
          self.list_model.setData(self.list_model.index(i, 0), f"{name}")
      if count > 0:
        self.ui.listView.setCurrentIndex(self.list_model.index(0))
        self.ui.pushButton.setEnabled(True)

  @QtCore.Slot()
  def select_user(self):
    self.user = self.user_list[self.ui.listView.selectedIndexes()[0].row()]
    self.accept()

  @QtCore.Slot()
  def browse_folder(self):
    print("bruh")
    file_dialog = QtWidgets.QFileDialog()
    file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
    if file_dialog.exec():
      self.ui.lineEdit.setText(file_dialog.selectedFiles()[0])
      pathlib.Path("settings").write_text(file_dialog.selectedFiles()[0])
      self.load()

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, user) -> None:
    super().__init__()
    self.user = user
    self.data = load_user(user['name'], user['user_index'], user['filepath'])
    self.original_data = copy.deepcopy(self.data)
    self.ui = edit_window.Ui_MainWindow()
    self.ui.setupUi(self)
    self.setWindowTitle("User File Editor")
    self.ui.tabWidget.setTabEnabled(4, False)
    self.ui.tabWidget.setTabVisible(4, False)

    self.uiAchievements = [
      self.ui.a_1,
      self.ui.a_2,
      self.ui.a_3,
      self.ui.a_4,
      self.ui.a_5,
      self.ui.a_6,
      self.ui.a_7,
      self.ui.a_8,
      self.ui.a_9,
      self.ui.a_10,
      self.ui.a_11,
      self.ui.a_12,
      self.ui.a_13,
      self.ui.a_14,
      self.ui.a_15,
      self.ui.a_16,
      self.ui.a_17,
      self.ui.a_18,
      self.ui.a_19,
      self.ui.a_20
    ]

    self.__load_data()
    self.__setup_callbacks()

  def __setup_callbacks(self):
    self.ui.a_all.clicked.connect(lambda : self.__change_achievements_selection(0))
    self.ui.a_invert.clicked.connect(lambda : self.__change_achievements_selection(1))
    self.ui.a_none.clicked.connect(lambda : self.__change_achievements_selection(2))

    self.ui.zg_mg1_never.stateChanged.connect(lambda state : self.ui.zg_mg1_date.setEnabled(state == 0))
    self.ui.zg_mg2_never.stateChanged.connect(lambda state : self.ui.zg_mg2_date.setEnabled(state == 0))
    self.ui.zg_mg3_never.stateChanged.connect(lambda state : self.ui.zg_mg3_date.setEnabled(state == 0))
    
    self.ui.zg_fertilizer_np.stateChanged.connect(lambda state : self.ui.zg_fertilizer.setEnabled(state == 0))
    self.ui.zg_bugspray_np.stateChanged.connect(lambda state : self.ui.zg_bugspray.setEnabled(state == 0))
    
    self.ui.zg_snail_lchoco_never.stateChanged.connect(lambda state : self.ui.zg_snail_lchoco.setEnabled(state == 0))
    self.ui.zg_snail_purchased.stateChanged.connect(lambda state : self.ui.zg_snail_lawoken.setEnabled(state == 2))
    self.ui.zg_food_purchased.stateChanged.connect(lambda state : self.ui.zg_tree_food.setEnabled(state == 2))

    self.ui.g_money.editingFinished.connect(lambda : self.ui.g_money.setValue(int(self.ui.g_money.value() / 10) * 10) if self.ui.g_money.value() % 10 != 0 else None)

    self.ui.save.clicked.connect(self.__save_btn)
    self.ui.reload.clicked.connect(self.__reload_btn)

  def __change_achievements_selection(self, action: int):
    for checkbox in self.uiAchievements:
      if action == 0:
        checkbox.setChecked(True)
      
      if action == 1:
        checkbox.toggle()
      
      if action == 2:
        checkbox.setChecked(False)

  def closeEvent(self, event: QCloseEvent):
    self.__update_data()
    if not deep_equals(self.original_data, self.data):
      event.ignore()
      message_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Warning, "Unsaved changes", "You have made changes but not saved them to the user file.\nAre you sure you want to quit without saving?")
      message_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
      message_box.setWindowFlags(QtCore.Qt.WindowType.Dialog | QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowTitleHint)

      if QtWidgets.QMessageBox.StandardButton.Yes == message_box.exec():
        event.accept()
    return super().closeEvent(event)

  def __save_btn(self):
    pass

  def __reload_btn(self):
    self.data = load_user(self.user['name'], self.user['user_index'], self.user['filepath'])
    self.original_data = copy.deepcopy(self.data)
    self.__load_data()

  def keyPressEvent(self, event: QKeyEvent) -> None:
    super().keyPressEvent(event)
    if not self.ui.tabWidget.isTabVisible(4) and event.key() == 76 and event.modifiers() & QtCore.Qt.KeyboardModifier.ControlModifier and event.modifiers() & QtCore.Qt.KeyboardModifier.ShiftModifier:
      self.ui.tabWidget.setTabEnabled(4, True)
      self.ui.tabWidget.setTabVisible(4, True)

  def __update_data(self):
    self.data['data']['general']['has_taco'] = self.ui.g_taco.isChecked()

  def __load_data(self):
    self.ui.g_name.setText(self.data['data']['general']['name'])
    level = self.data['data']['general']['level']
    self.ui.g_level.setCurrentIndex(((level % 10) - 1) + (int(level / 11) * 10))
    self.ui.g_completed.setValue(self.data['data']['general']['completed'])
    self.ui.g_money.setValue(self.data['data']['general']['money'])
    self.ui.g_minigames_unlocked.setChecked(self.data['data']['general']['minigames_unlocked'])
    self.ui.g_puzzle_unlocked.setChecked(self.data['data']['general']['puzzles_unlocked'])
    self.ui.g_taco.setChecked(self.data['data']['general']['has_taco'])
    self.ui.g_slots.setValue(self.data['data']['general']['shop']['slots'])
    self.ui.g_pool_cleaner.setChecked(self.data['data']['general']['shop']['pool_cleaner'])
    self.ui.g_roof_cleaner.setChecked(self.data['data']['general']['shop']['roof_cleaner'])
    self.ui.g_rake_uses.setValue(self.data['data']['general']['shop']['rake_uses'])

    self.ui.g_plants_1.setChecked(self.data['data']['general']['shop']['plants']['gatling_pea'])
    self.ui.g_plants_2.setChecked(self.data['data']['general']['shop']['plants']['twin_sunflower'])
    self.ui.g_plants_3.setChecked(self.data['data']['general']['shop']['plants']['gatling_pea'])
    self.ui.g_plants_4.setChecked(self.data['data']['general']['shop']['plants']['gloom_shroom'])
    self.ui.g_plants_5.setChecked(self.data['data']['general']['shop']['plants']['cattail'])
    self.ui.g_plants_6.setChecked(self.data['data']['general']['shop']['plants']['winter_melon'])
    self.ui.g_plants_7.setChecked(self.data['data']['general']['shop']['plants']['gold_magnet'])
    self.ui.g_plants_8.setChecked(self.data['data']['general']['shop']['plants']['spikerock'])
    self.ui.g_plants_9.setChecked(self.data['data']['general']['shop']['plants']['cob_cannon'])
    self.ui.g_plants_10.setChecked(self.data['data']['general']['shop']['plants']['imitater'])

    self.ui.zg_golden_can.setChecked(self.data['data']['zen_garden']['golden_can'])
    self.ui.zg_phonograph.setChecked(self.data['data']['zen_garden']['phonograph'])
    self.ui.zg_glove.setChecked(self.data['data']['zen_garden']['glove'])
    self.ui.zg_aquarium_g.setChecked(self.data['data']['zen_garden']['aquarium_garden'])
    self.ui.zg_mushroom_g.setChecked(self.data['data']['zen_garden']['mushroom_garden'])
    self.ui.zg_wheelbarrow.setChecked(self.data['data']['zen_garden']['wheel_barrow'])
    
    if self.data['data']['zen_garden']['fertilizer'] == 0:
      self.ui.zg_fertilizer.setValue(0)
      self.ui.zg_fertilizer_np.setChecked(True)
      self.ui.zg_fertilizer.setEnabled(False)
    else:
      self.ui.zg_fertilizer.setValue(self.data['data']['zen_garden']['fertilizer'] - 1000)
      self.ui.zg_fertilizer_np.setChecked(True)
      self.ui.zg_fertilizer.setEnabled(True)

    if self.data['data']['zen_garden']['bug_spray'] == 0:
      self.ui.zg_bugspray.setValue(0)
      self.ui.zg_bugspray_np.setChecked(True)
      self.ui.zg_bugspray.setEnabled(False)
    else:
      self.ui.zg_bugspray.setValue(self.data['data']['zen_garden']['bug_spray'] - 1000)
      self.ui.zg_bugspray_np.setChecked(True)
      self.ui.zg_bugspray.setEnabled(True)

    self.ui.a_1.setChecked(self.data['data']['achievements']['home_lawn_security'])
    self.ui.a_2.setChecked(self.data['data']['achievements']['nobel_peas_prize'])
    self.ui.a_3.setChecked(self.data['data']['achievements']['better_off_dead'])
    self.ui.a_4.setChecked(self.data['data']['achievements']['china_shop'])
    self.ui.a_5.setChecked(self.data['data']['achievements']['spudow!'])
    self.ui.a_6.setChecked(self.data['data']['achievements']['explodonator'])
    self.ui.a_7.setChecked(self.data['data']['achievements']['morticulturalist'])
    self.ui.a_8.setChecked(self.data['data']['achievements']['dont_pea_in_the_pool'])
    self.ui.a_9.setChecked(self.data['data']['achievements']['roll_some_heads'])
    self.ui.a_10.setChecked(self.data['data']['achievements']['grounded'])
    self.ui.a_11.setChecked(self.data['data']['achievements']['zombologist'])
    self.ui.a_12.setChecked(self.data['data']['achievements']['penny_pitcher'])
    self.ui.a_13.setChecked(self.data['data']['achievements']['sunny_days'])
    self.ui.a_14.setChecked(self.data['data']['achievements']['popcorn_party'])
    self.ui.a_15.setChecked(self.data['data']['achievements']['good_morning'])
    self.ui.a_16.setChecked(self.data['data']['achievements']['no_fungus_among_us'])
    self.ui.a_17.setChecked(self.data['data']['achievements']['beyond_the_grave'])
    self.ui.a_18.setChecked(self.data['data']['achievements']['immortal'])
    self.ui.a_19.setChecked(self.data['data']['achievements']['towering_wisdom'])
    self.ui.a_20.setChecked(self.data['data']['achievements']['mustache_mode'])

    self.ui.c_surv_1.setValue(self.data['data']['challenges']['survivals']['normal']['day'])
    self.ui.c_surv_2.setValue(self.data['data']['challenges']['survivals']['normal']['night'])
    self.ui.c_surv_3.setValue(self.data['data']['challenges']['survivals']['normal']['pool'])
    self.ui.c_surv_4.setValue(self.data['data']['challenges']['survivals']['normal']['fog'])
    self.ui.c_surv_5.setValue(self.data['data']['challenges']['survivals']['normal']['roof'])
    self.ui.c_survhard_1.setValue(self.data['data']['challenges']['survivals']['hard']['day'])
    self.ui.c_survhard_2.setValue(self.data['data']['challenges']['survivals']['hard']['night'])
    self.ui.c_survhard_3.setValue(self.data['data']['challenges']['survivals']['hard']['pool'])
    self.ui.c_survhard_4.setValue(self.data['data']['challenges']['survivals']['hard']['fog'])
    self.ui.c_survhard_5.setValue(self.data['data']['challenges']['survivals']['hard']['roof'])
    self.ui.c_survend.setValue(self.data['data']['challenges']['survivals']['endless'])

    self.ui.c_mg_1.setChecked(self.data['data']['challenges']['minigames']['zombotany'])
    self.ui.c_mg_2.setChecked(self.data['data']['challenges']['minigames']['wallnut_bowling'])
    self.ui.c_mg_3.setChecked(self.data['data']['challenges']['minigames']['slot_machine'])
    self.ui.c_mg_4.setChecked(self.data['data']['challenges']['minigames']['its_raining_seeds'])
    self.ui.c_mg_5.setChecked(self.data['data']['challenges']['minigames']['beghouled'])
    self.ui.c_mg_6.setChecked(self.data['data']['challenges']['minigames']['invisighoul'])
    self.ui.c_mg_7.setChecked(self.data['data']['challenges']['minigames']['seeing_stars'])
    self.ui.c_mg_8.setChecked(self.data['data']['challenges']['minigames']['zombiquarium'])
    self.ui.c_mg_9.setChecked(self.data['data']['challenges']['minigames']['beghouled_twist'])
    self.ui.c_mg_10.setChecked(self.data['data']['challenges']['minigames']['big_trouble_little_zombie'])
    self.ui.c_mg_11.setChecked(self.data['data']['challenges']['minigames']['portal_combat'])
    self.ui.c_mg_12.setChecked(self.data['data']['challenges']['minigames']['column_like_you_see_em'])
    self.ui.c_mg_13.setChecked(self.data['data']['challenges']['minigames']['bobsled_bonanza'])
    self.ui.c_mg_14.setChecked(self.data['data']['challenges']['minigames']['zombie_n_zombie_q'])
    self.ui.c_mg_15.setChecked(self.data['data']['challenges']['minigames']['whack_a_zombie'])
    self.ui.c_mg_16.setChecked(self.data['data']['challenges']['minigames']['last_stand'])
    self.ui.c_mg_17.setChecked(self.data['data']['challenges']['minigames']['zombotany2'])
    self.ui.c_mg_18.setChecked(self.data['data']['challenges']['minigames']['wallnut_bowling2'])
    self.ui.c_mg_19.setChecked(self.data['data']['challenges']['minigames']['pogo_party'])
    self.ui.c_mg_20.setChecked(self.data['data']['challenges']['minigames']['dr_zomboss_revenge'])

    self.ui.c_pz_1.setChecked(self.data['data']['challenges']['puzzles']['vasebreaker'])
    self.ui.c_pz_2.setChecked(self.data['data']['challenges']['puzzles']['to_the_left'])
    self.ui.c_pz_3.setChecked(self.data['data']['challenges']['puzzles']['third_vase'])
    self.ui.c_pz_4.setChecked(self.data['data']['challenges']['puzzles']['chain_reaction'])
    self.ui.c_pz_5.setChecked(self.data['data']['challenges']['puzzles']['m_is_for_metal'])
    self.ui.c_pz_6.setChecked(self.data['data']['challenges']['puzzles']['scary_potter'])
    self.ui.c_pz_7.setChecked(self.data['data']['challenges']['puzzles']['hokey_pokey'])
    self.ui.c_pz_8.setChecked(self.data['data']['challenges']['puzzles']['another_chain_reaction'])
    self.ui.c_pz_9.setChecked(self.data['data']['challenges']['puzzles']['ace_of_vases'])
    self.ui.c_pz_10.setValue(self.data['data']['challenges']['puzzles']['vasebreaker_endless'])
    self.ui.c_pz_11.setChecked(self.data['data']['challenges']['puzzles']['izombie'])
    self.ui.c_pz_12.setChecked(self.data['data']['challenges']['puzzles']['izombie_too'])
    self.ui.c_pz_13.setChecked(self.data['data']['challenges']['puzzles']['can_you_dig_it'])
    self.ui.c_pz_14.setChecked(self.data['data']['challenges']['puzzles']['totally_nuts'])
    self.ui.c_pz_15.setChecked(self.data['data']['challenges']['puzzles']['dead_zeppelin'])
    self.ui.c_pz_16.setChecked(self.data['data']['challenges']['puzzles']['me_smash'])
    self.ui.c_pz_17.setChecked(self.data['data']['challenges']['puzzles']['zomboggie'])
    self.ui.c_pz_18.setChecked(self.data['data']['challenges']['puzzles']['tree_hit_wonder'])
    self.ui.c_pz_19.setChecked(self.data['data']['challenges']['puzzles']['all_your_brainz'])
    self.ui.c_pz_20.setValue(self.data['data']['challenges']['puzzles']['izombie_endless'])
    
    self.ui.l_survend_1.setValue(self.data['data']['limbo']['survival_endless']['day'])
    self.ui.l_survend_2.setValue(self.data['data']['limbo']['survival_endless']['night'])
    self.ui.l_survend_3.setValue(self.data['data']['limbo']['survival_endless']['fog'])
    self.ui.l_survend_4.setValue(self.data['data']['limbo']['survival_endless']['roof'])

    self.ui.l_mg_1.setChecked(self.data['data']['limbo']['minigames']['art_wallnut'])
    self.ui.l_mg_2.setChecked(self.data['data']['limbo']['minigames']['sunny_day'])
    self.ui.l_mg_3.setChecked(self.data['data']['limbo']['minigames']['unsodded'])
    self.ui.l_mg_4.setChecked(self.data['data']['limbo']['minigames']['buy_time'])
    self.ui.l_mg_5.setChecked(self.data['data']['limbo']['minigames']['art_sunflower'])
    self.ui.l_mg_6.setChecked(self.data['data']['limbo']['minigames']['air_raid'])
    self.ui.l_mg_7.setChecked(self.data['data']['limbo']['minigames']['ice_level'])
    self.ui.l_mg_8.setChecked(self.data['data']['limbo']['minigames']['zen_garden'])
    self.ui.l_mg_9.setChecked(self.data['data']['limbo']['minigames']['high_gravity'])
    self.ui.l_mg_10.setChecked(self.data['data']['limbo']['minigames']['grave_danger'])
    self.ui.l_mg_11.setChecked(self.data['data']['limbo']['minigames']['can_you_dig_it'])
    self.ui.l_mg_12.setChecked(self.data['data']['limbo']['minigames']['dark_night'])
    self.ui.l_mg_13.setChecked(self.data['data']['limbo']['minigames']['bungee_blitz'])
    self.ui.l_mg_14.setChecked(self.data['data']['limbo']['minigames']['intro'])
    self.ui.l_mg_15.setChecked(self.data['data']['limbo']['minigames']['tree'])
    self.ui.l_mg_16.setChecked(self.data['data']['limbo']['minigames']['upsell'])

    self.ui.z_license.setChecked(self.data['data']['zombatar']['license'])
    self.ui.z_created_before.setChecked(self.data['data']['zombatar']['created_before'])

def load_user(name, user_index, filepath):
  file_bytes = filepath.read_bytes()

  achiev_offset = 0x334 + (struct.unpack("<I", file_bytes[0x330:0x334])[0] * 0x58) 

  user = {
    'index': user_index,
    'data': {
      'general': {
        'name': name,
        'level': struct.unpack("<I", file_bytes[0x004:0x008])[0],
        'completed': struct.unpack("<I", file_bytes[0x00C:0x010])[0],
        'money': struct.unpack("<I", file_bytes[0x008:0x00C])[0] * 10,
        'minigames_unlocked': struct.unpack("<I", file_bytes[0x300:0x304])[0] == 1,
        'puzzles_unlocked': struct.unpack("<I", file_bytes[0x304:0x308])[0] == 1,
        'has_taco': struct.unpack("<I", file_bytes[0x320:0x324])[0] == 1,
        'shop': {
          'slots': struct.unpack("<I", file_bytes[0x1F4:0x1F8])[0] + 6,
          'pool_cleaner': struct.unpack("<I", file_bytes[0x1F8:0x1FC])[0] == 1,
          'roof_cleaner': struct.unpack("<I", file_bytes[0x1FC:0x200])[0] == 1,
          'rake_uses': struct.unpack("<I", file_bytes[0x200:0x204])[0],
          'plants': {
            'gatling_pea': struct.unpack("<I", file_bytes[0x1A0:0x1A4])[0] == 1,
            'twin_sunflower': struct.unpack("<I", file_bytes[0x1A4:0x1A8])[0] == 1,
            'gloom_shroom': struct.unpack("<I", file_bytes[0x1A8:0x1AC])[0] == 1,
            'cattail': struct.unpack("<I", file_bytes[0x1AC:0x1B0])[0] == 1,
            'winter_melon': struct.unpack("<I", file_bytes[0x1B0:0x1B4])[0] == 1,
            'gold_magnet': struct.unpack("<I", file_bytes[0x1B4:0x1B8])[0] == 1,
            'spikerock': struct.unpack("<I", file_bytes[0x1B8:0x1BC])[0] == 1,
            'cob_cannon': struct.unpack("<I", file_bytes[0x1BC:0x1C0])[0] == 1,
            'imitater': struct.unpack("<I", file_bytes[0x1C0:0x1C4])[0] == 1,
          }
        }
      },
      'zen_garden': {
        'golden_can': False,
        'phonograph': False,
        'glove': False,
        'fertilizer': 0,
        'bug_spray': 0,
        'mushroom_garden': 0,
        'aquarium_garden': 0,
        'wheel_barrow': 0,
        'snail': {
          'last_awoken': 0,
          'last_chocalte': 0,
          'x': 0,
          'y': 0,
        },
        'tree': {
          'purchased': False,
          'height': 0,
          'purchased_food': False,
          'food': 0,
        },
        'plants': []
      },
      'achievements': {
        'home_lawn_security': struct.unpack('<H', file_bytes[achiev_offset:(achiev_offset + 2)])[0] != 0,
        'nobel_peas_prize': struct.unpack('<H', file_bytes[(achiev_offset + 2):(achiev_offset + 4)])[0] != 0,
        'better_off_dead': struct.unpack('<H', file_bytes[(achiev_offset + 4):(achiev_offset + 6)])[0] != 0,
        'china_shop': struct.unpack('<H', file_bytes[(achiev_offset + 6):(achiev_offset + 8)])[0] != 0,
        'spudow!': struct.unpack('<H', file_bytes[(achiev_offset + 8):(achiev_offset + 10)])[0] != 0,
        'explodonator': struct.unpack('<H', file_bytes[(achiev_offset + 10):(achiev_offset + 12)])[0] != 0,
        'morticulturalist': struct.unpack('<H', file_bytes[(achiev_offset + 12):(achiev_offset + 14)])[0] != 0,
        'dont_pea_in_the_pool': struct.unpack('<H', file_bytes[(achiev_offset + 14):(achiev_offset + 16)])[0] != 0,
        'roll_some_heads': struct.unpack('<H', file_bytes[(achiev_offset + 16):(achiev_offset + 18)])[0] != 0,
        'grounded': struct.unpack('<H', file_bytes[(achiev_offset + 18):(achiev_offset + 20)])[0] != 0,
        'zombologist': struct.unpack('<H', file_bytes[(achiev_offset + 20):(achiev_offset + 22)])[0] != 0,
        'penny_pitcher': struct.unpack('<H', file_bytes[(achiev_offset + 22):(achiev_offset + 24)])[0] != 0,
        'sunny_days': struct.unpack('<H', file_bytes[(achiev_offset + 24):(achiev_offset + 26)])[0] != 0,
        'popcorn_party': struct.unpack('<H', file_bytes[(achiev_offset + 26):(achiev_offset + 28)])[0] != 0,
        'good_morning': struct.unpack('<H', file_bytes[(achiev_offset + 28):(achiev_offset + 30)])[0] != 0,
        'no_fungus_among_us': struct.unpack('<H', file_bytes[(achiev_offset + 30):(achiev_offset + 32)])[0] != 0,
        'beyond_the_grave': struct.unpack('<H', file_bytes[(achiev_offset + 32):(achiev_offset + 34)])[0] != 0,
        'immortal': struct.unpack('<H', file_bytes[(achiev_offset + 34):(achiev_offset + 36)])[0] != 0,
        'towering_wisdom': struct.unpack('<H', file_bytes[(achiev_offset + 36):(achiev_offset + 38)])[0] != 0,
        'mustache_mode': struct.unpack('<H', file_bytes[(achiev_offset + 38):(achiev_offset + 40)])[0] != 0,
      },
      'challenges': {
        'survivals': {
          'normal': {
            'day': 0,
            'night': 0,
            'pool': 0,
            'fog': 0,
            'roof': 0,
          },
          'hard': {
            'day': 0,
            'night': 0,
            'pool': 0,
            'fog': 0,
            'roof': 0,
          },
          'endless': 0
        },
        'minigames': {
          'zombotany': False,
          'wallnut_bowling': False,
          'slot_machine': False,
          'its_raining_seeds': False,
          'beghouled': False,
          'invisighoul': False,
          'seeing_stars': False,
          'zombiquarium': False,
          'beghouled_twist': False,
          'big_trouble_little_zombie': False,
          'portal_combat': False,
          'column_like_you_see_em': False,
          'bobsled_bonanza': False,
          'zombie_n_zombie_q': False,
          'whack_a_zombie': False,
          'last_stand': False,
          'zombotany2': False,
          'wallnut_bowling2': False,
          'pogo_party': False,
          'dr_zomboss_revenge': False,
        },
        'puzzles': {
          'vasebreaker': False,
          'to_the_left': False,
          'third_vase': False,
          'chain_reaction': False,
          'm_is_for_metal': False,
          'scary_potter': False,
          'hokey_pokey': False,
          'another_chain_reaction': False,
          'ace_of_vases': False,
          'vasebreaker_endless': 0,
          'izombie': False,
          'izombie_too': False,
          'can_you_dig_it': False,
          'totally_nuts': False,
          'dead_zeppelin': False,
          'me_smash': False,
          'zomboggie': False,
          'tree_hit_wonder': False,
          'all_your_brainz': False,
          'izombie_endless': 0,
        }
      },
      'limbo': {
        'survival_endless': {
          'day': 0,
          'night': 0,
          'fog': 10,
          'roof': 0,
        },
        'minigames': {
          'art_wallnut': False,
          'sunny_day': False,
          'unsodded': False,
          'buy_time': True,
          'art_sunflower': False,
          'air_raid': False,
          'ice_level': False,
          'zen_garden': False,
          'high_gravity': False,
          'grave_danger': False,
          'can_you_dig_it': False,
          'dark_night': False,
          'bungee_blitz': False,
          'intro': False,
          'tree': False,
          'upsell': False,
        }
      },
      'zombatar': {
        'license': False,
        'created_before': False,
        'zombatars': [],
      }
    }
  }

  return user

def main():
  app = QtWidgets.QApplication([])

  dialog = SelectUserDialog()
  if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
    win = MainWindow(dialog.user)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
  main()