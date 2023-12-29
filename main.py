import copy
import sys
import struct
import pathlib
from typing import Optional
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QItemSelection, Qt
from PySide6.QtGui import QCloseEvent, QKeyEvent
from PySide6.QtWidgets import QWidget
import ui.ui_select_dialog
import ui.ui_edit_window
from utils import *
from select_user_dialog import SelectUserDialog

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, user) -> None:
    super().__init__()
    self.user = user
    self.data = load_user(user['name'], user['user_index'], user['filepath'])
    self.original_data = copy.deepcopy(self.data)
    self.ui = ui.ui_edit_window.Ui_MainWindow()
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

    self.ui.zg_plant_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
    self.__setup_callbacks()
    self.__load_data()

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
    self.ui.zg_snail_purchased.stateChanged.connect(lambda state : self.__update_snail_widgets(state == 2))
    self.ui.zg_food_purchased.stateChanged.connect(lambda state : self.ui.zg_tree_food.setEnabled(state == 2))

    self.ui.g_money.editingFinished.connect(lambda : self.ui.g_money.setValue(int(self.ui.g_money.value() / 10) * 10) if self.ui.g_money.value() % 10 != 0 else None)

    self.ui.save.clicked.connect(self.__save_btn)
    self.ui.reload.clicked.connect(self.__reload_btn)

    self.ui.zg_plant_list.itemSelectionChanged.connect(self.__plant_list_selection_changed)
    self.ui.zg_del_plant.clicked.connect(self.__plant_delete)
    self.ui.zg_dup_plant.clicked.connect(self.__plant_duplicate)

  def __plant_duplicate(self):
    index = self.ui.zg_plant_list.selectedIndexes()[0].row()
    plant = copy.deepcopy(self.data['data']['zen_garden']['plants'][index])
    color = get_plant_color_name(plant['color']) 
    dup_index = index + 1

    self.data['data']['zen_garden']['plants'].insert(dup_index, plant)
    self.ui.zg_plants_label.setText(f"Plants ({len(self.data['data']['zen_garden']['plants'])})")
    self.ui.zg_plant_list.insertItem(dup_index,
                                     f"{get_plant_type_name(plant['type'])}{"" if color == 'None' else f' ({color})'}, {PLANT_DIR[plant['dir']]} [{plant['pos'][0]}, {plant['pos'][1]}] {PLANT_LOCATION[plant['location']]}")

    self.__update_plant_list()
    self.ui.zg_plant_list.setCurrentItem(self.ui.zg_plant_list.item(dup_index))

  def __update_plant_list(self):
    self.ui.zg_plant_list.clear()
    self.ui.zg_plants_label.setText(f"Plants ({len(self.data['data']['zen_garden']['plants'])})")
    for i in range(len(self.data['data']['zen_garden']['plants'])):
      plant = self.data['data']['zen_garden']['plants'][i]
      color = get_plant_color_name(plant['color'])
      self.ui.zg_plant_list.addItem(f"{get_plant_type_name(plant['type'])}{"" if color == 'None' else f' ({color})'}, {PLANT_DIR[plant['dir']]} [{plant['pos'][0]}, {plant['pos'][1]}] {PLANT_LOCATION[plant['location']]}")

  def __plant_delete(self):
    indices = []
    for m in self.ui.zg_plant_list.selectedIndexes():
      indices.append(m.row())

    indices.sort(reverse=True)

    for index in indices:
      self.data['data']['zen_garden']['plants'].pop(index)

    self.__update_plant_list()

  def __plant_list_selection_changed(self):
    sel_items = self.ui.zg_plant_list.selectedItems()

    self.ui.zg_del_plant.setEnabled(len(sel_items) >= 1)
    self.ui.zg_dup_plant.setEnabled(len(sel_items) == 1)

    self.ui.groupBox_11.setEnabled(len(sel_items) == 1)

    if len(sel_items) == 1:
      plant = self.data['data']['zen_garden']['plants'][self.ui.zg_plant_list.selectedIndexes()[0].row()]
      self.ui.zg_plant_type.setCurrentIndex(plant['type'])
      self.ui.zg_plant_loc.setCurrentIndex(plant['location'])
      self.ui.zg_plant_hn.setCurrentIndex(plant['happiness_need'])
      self.ui.zg_plant_color.setCurrentIndex(1 if plant['color'] == 0 else plant['color'] - 1)
      self.ui.zg_plant_row.setValue(plant['pos'][0])
      self.ui.zg_plant_col.setValue(plant['pos'][1])

  def __update_snail_widgets(self, is_purchased):
    self.ui.zg_snail_lawoken.setEnabled(is_purchased)
    self.ui.zg_snail_x.setEnabled(is_purchased)
    self.ui.zg_snail_y.setEnabled(is_purchased)

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

    self.ui.zg_mg1_date.setDate(QtCore.QDate(2000, 1, 1).addDays(self.data['data']['zen_garden']['marigold1_date']));
    self.ui.zg_mg2_date.setDate(QtCore.QDate(2000, 1, 1).addDays(self.data['data']['zen_garden']['marigold2_date']));
    self.ui.zg_mg3_date.setDate(QtCore.QDate(2000, 1, 1).addDays(self.data['data']['zen_garden']['marigold3_date']));

    if self.data['data']['zen_garden']['marigold1_date'] == 0:
      self.ui.zg_mg1_date.setEnabled(False)
      self.ui.zg_mg1_never.setChecked(True)
    else:
      self.ui.zg_mg1_date.setEnabled(True)
      self.ui.zg_mg1_never.setChecked(False)

    if self.data['data']['zen_garden']['marigold2_date'] == 0:
      self.ui.zg_mg2_date.setEnabled(False)
      self.ui.zg_mg2_never.setChecked(True)
    else:
      self.ui.zg_mg2_date.setEnabled(True)
      self.ui.zg_mg2_never.setChecked(False)

    if self.data['data']['zen_garden']['marigold3_date'] == 0:
      self.ui.zg_mg3_date.setEnabled(False)
      self.ui.zg_mg3_never.setChecked(True)
    else:
      self.ui.zg_mg3_date.setEnabled(True)
      self.ui.zg_mg3_never.setChecked(False)

    if self.data['data']['zen_garden']['fertilizer'] == 0:
      self.ui.zg_fertilizer.setValue(0)
      self.ui.zg_fertilizer_np.setChecked(True)
    else:
      self.ui.zg_fertilizer.setValue(self.data['data']['zen_garden']['fertilizer'] - 1000)
      self.ui.zg_fertilizer_np.setChecked(False)

    if self.data['data']['zen_garden']['bug_spray'] == 0:
      self.ui.zg_bugspray.setValue(0)
      self.ui.zg_bugspray_np.setChecked(True)
    else:
      self.ui.zg_bugspray.setValue(self.data['data']['zen_garden']['bug_spray'] - 1000)
      self.ui.zg_bugspray_np.setChecked(False)

    self.ui.zg_snail_purchased.setChecked(self.data['data']['zen_garden']['snail']['last_awoken'] != 0)

    self.ui.zg_snail_x.setValue(self.data['data']['zen_garden']['snail']['x'])
    self.ui.zg_snail_y.setValue(self.data['data']['zen_garden']['snail']['y'])

    self.ui.zg_plant_list.clear()
    self.ui.zg_plants_label.setText(f"Plants ({len(self.data['data']['zen_garden']['plants'])})")
    for i in range(len(self.data['data']['zen_garden']['plants'])):
      plant = self.data['data']['zen_garden']['plants'][i]
      color = get_plant_color_name(plant['color'])
      self.ui.zg_plant_list.addItem(f"{get_plant_type_name(plant['type'])}{"" if color == 'None' else f' ({color})'}, {PLANT_DIR[plant['dir']]} [{plant['pos'][0]}, {plant['pos'][1]}] {PLANT_LOCATION[plant['location']]}")

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

def main():
  app = QtWidgets.QApplication(sys.argv)
  app.setWindowIcon(QtGui.QIcon("icon.ico"))

  dialog = SelectUserDialog()
  if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
    win = MainWindow(dialog.user)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
  main()