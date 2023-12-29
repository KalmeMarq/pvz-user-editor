import struct

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

def read_number(file_bytes, format, offset, size):
  return struct.unpack(format, file_bytes[offset:(offset + size)])[0]

def load_user(name, user_index, filepath):
  file_bytes = filepath.read_bytes()

  achiev_offset = 0x334 + (struct.unpack("<I", file_bytes[0x330:0x334])[0] * 0x58) 

  user = {
    'index': user_index,
    'data': {
      'general': {
        'name': name,
        'level': read_number(file_bytes, "<I", 0x004, 4),
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
        'marigold1_date': read_number(file_bytes, "<I", 0x1C8, 4),
        'marigold2_date': read_number(file_bytes, "<I", 0x1CC, 4),
        'marigold3_date': read_number(file_bytes, "<I", 0x1D0, 4),
        'golden_can': read_number(file_bytes, "<I", 0x1D4, 4) == 1,
        'phonograph': read_number(file_bytes, "<I", 0x1E0, 4) == 1,
        'glove': read_number(file_bytes, "<I", 0x1E4, 4) == 1,
        'fertilizer': read_number(file_bytes, "<I", 0x1D8, 4),
        'bug_spray': read_number(file_bytes, "<I", 0x1DC, 4),
        'mushroom_garden': read_number(file_bytes, "<I", 0x1E8, 4) == 1,
        'aquarium_garden': read_number(file_bytes, "<I", 0x204, 4) == 1,
        'wheel_barrow': read_number(file_bytes, "<I", 0x1EC, 4) == 1,
        'snail': {
          'last_awoken': read_number(file_bytes, "<I", 0x1F0, 4),
          'last_chocolate': read_number(file_bytes, "<I", 0x2F4, 4),
          'x': read_number(file_bytes, "<I", 0x2F8, 4),
          'y': read_number(file_bytes, "<I", 0x2FC, 4),
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
            'day': read_number(file_bytes, "<I", 0x010, 4),
            'night': read_number(file_bytes, "<I", 0x014, 4),
            'pool': read_number(file_bytes, "<I", 0x018, 4),
            'fog': read_number(file_bytes, "<I", 0x01C, 4),
            'roof': read_number(file_bytes, "<I", 0x020, 4),
          },
          'hard': {
            'day': read_number(file_bytes, "<I", 0x024, 4),
            'night': read_number(file_bytes, "<I", 0x028, 4),
            'pool': read_number(file_bytes, "<I", 0x02C, 4),
            'fog': read_number(file_bytes, "<I", 0x030, 4),
            'roof': read_number(file_bytes, "<I", 0x034, 4),
          },
          'endless': read_number(file_bytes, "<I", 0x040, 4)
        },
        'minigames': {
          'zombotany': read_number(file_bytes, "<I", 0x04C, 4) != 0,
          'wallnut_bowling': read_number(file_bytes, "<I", 0x050, 4) != 0,
          'slot_machine': read_number(file_bytes, "<I", 0x054, 4) != 0,
          'its_raining_seeds': read_number(file_bytes, "<I", 0x058, 4) != 0,
          'beghouled': read_number(file_bytes, "<I", 0x05C, 4) != 0,
          'invisighoul': read_number(file_bytes, "<I", 0x060, 4) != 0,
          'seeing_stars': read_number(file_bytes, "<I", 0x064, 4) != 0,
          'zombiquarium': read_number(file_bytes, "<I", 0x068, 4) != 0,
          'beghouled_twist': read_number(file_bytes, "<I", 0x06C, 4) != 0,
          'big_trouble_little_zombie': read_number(file_bytes, "<I", 0x070, 4) != 0,
          'portal_combat': read_number(file_bytes, "<I", 0x074, 4) != 0,
          'column_like_you_see_em': read_number(file_bytes, "<I", 0x078, 4) != 0,
          'bobsled_bonanza': read_number(file_bytes, "<I", 0x07C, 4) != 0,
          'zombie_n_zombie_q': read_number(file_bytes, "<I", 0x080, 4) != 0,
          'whack_a_zombie': read_number(file_bytes, "<I", 0x084, 4) != 0,
          'last_stand': read_number(file_bytes, "<I", 0x088, 4) != 0,
          'zombotany2': read_number(file_bytes, "<I", 0x08C, 4) != 0,
          'wallnut_bowling2': read_number(file_bytes, "<I", 0x090, 4) != 0,
          'pogo_party': read_number(file_bytes, "<I", 0x094, 4) != 0,
          'dr_zomboss_revenge': read_number(file_bytes, "<I", 0x098, 4) != 0,
        },
        'puzzles': {
          'vasebreaker': read_number(file_bytes, "<I", 0x0D8, 4) != 0,
          'to_the_left': read_number(file_bytes, "<I", 0x0DC, 4) != 0,
          'third_vase': read_number(file_bytes, "<I", 0x0E0, 4) != 0,
          'chain_reaction': read_number(file_bytes, "<I", 0x0E4, 4) != 0,
          'm_is_for_metal': read_number(file_bytes, "<I", 0x0E8, 4) != 0,
          'scary_potter': read_number(file_bytes, "<I", 0x0EC, 4) != 0,
          'hokey_pokey': read_number(file_bytes, "<I", 0x0F0, 4) != 0,
          'another_chain_reaction': read_number(file_bytes, "<I", 0x0F4, 4) != 0,
          'ace_of_vases': read_number(file_bytes, "<I", 0x0F8, 4) != 0,
          'vasebreaker_endless': read_number(file_bytes, "<I", 0x0FC, 4),
          'izombie': read_number(file_bytes, "<I", 0x100, 4) != 0,
          'izombie_too': read_number(file_bytes, "<I", 0x104, 4) != 0,
          'can_you_dig_it': read_number(file_bytes, "<I", 0x108, 4) != 0,
          'totally_nuts': read_number(file_bytes, "<I", 0x10C, 4) != 0,
          'dead_zeppelin': read_number(file_bytes, "<I", 0x110, 4) != 0,
          'me_smash': read_number(file_bytes, "<I", 0x114, 4) != 0,
          'zomboggie': read_number(file_bytes, "<I", 0x118, 4) != 0,
          'tree_hit_wonder': read_number(file_bytes, "<I", 0x11C, 4) != 0,
          'all_your_brainz': read_number(file_bytes, "<I", 0x120, 4) != 0,
          'izombie_endless': read_number(file_bytes, "<I", 0x124, 4),
        }
      },
      'limbo': {
        'survival_endless': {
          'day': read_number(file_bytes, "<I", 0x038, 4) != 0,
          'night': read_number(file_bytes, "<I", 0x03C, 4) != 0,
          'fog': read_number(file_bytes, "<I", 0x044, 4) != 0,
          'roof': read_number(file_bytes, "<I", 0x048, 4) != 0,
        },
        'minigames': {
          'art_wallnut': read_number(file_bytes, "<I", 0x09C, 4) != 0,
          'sunny_day': read_number(file_bytes, "<I", 0x0A0, 4) != 0,
          'unsodded': read_number(file_bytes, "<I", 0x0A4, 4) != 0,
          'buy_time': read_number(file_bytes, "<I", 0x0A8, 4) != 0,
          'art_sunflower': read_number(file_bytes, "<I", 0x0AC, 4) != 0,
          'air_raid': read_number(file_bytes, "<I", 0x0B0, 4) != 0,
          'ice_level': read_number(file_bytes, "<I", 0x0B4, 4) != 0,
          'zen_garden': read_number(file_bytes, "<I", 0x0B8, 4) != 0,
          'high_gravity': read_number(file_bytes, "<I", 0x0BC, 4) != 0,
          'grave_danger': read_number(file_bytes, "<I", 0x0C0, 4) != 0,
          'can_you_dig_it': read_number(file_bytes, "<I", 0x0C4, 4) != 0,
          'dark_night': read_number(file_bytes, "<I", 0x0C8, 4) != 0,
          'bungee_blitz': read_number(file_bytes, "<I", 0x0CC, 4) != 0,
          'intro': read_number(file_bytes, "<I", 0x0D0, 4) != 0,
          'tree': read_number(file_bytes, "<I", 0x0D4, 4) != 0,
          'upsell': read_number(file_bytes, "<I", 0x0D8, 4) != 0,
        }
      },
      'zombatar': {
        'license': read_number(file_bytes, "<I", 0x334 + read_number(file_bytes, "<I", 0x330, 4) * 0x58 + 0x28, 4) == 1,
        'created_before': read_number(file_bytes, "<I", 0x365 + read_number(file_bytes, "<I", 0x330, 4) * 0x58 +  + 0x28, 4) == 1,
        'zombatars': [],
      }
    }
  }

  plant_count = read_number(file_bytes, "<I", 0x330, 4)

  for i in range(plant_count):
    base_offset = 0x334 + i * 88
    plant_type = read_number(file_bytes, "<I", base_offset + 0x00, 4)
    location = read_number(file_bytes, "<I", base_offset + 0x04, 4)
    column = read_number(file_bytes, "<I", base_offset + 0x08, 4)
    row = read_number(file_bytes, "<I", base_offset + 0x0C, 4)
    direction = read_number(file_bytes, "<I", base_offset + 0x10, 4)
    last_watered = read_number(file_bytes, "<I", base_offset + 0x18, 4)
    color = read_number(file_bytes, "<I", base_offset + 0x20, 4)
    fertilized_amount = read_number(file_bytes, "<I", base_offset + 0x24, 4)
    watered_amount = read_number(file_bytes, "<I", base_offset + 0x28, 4)
    watered_need_amount = read_number(file_bytes, "<I", base_offset + 0x2C, 4)
    happiness_need = read_number(file_bytes, "<I", base_offset + 0x30, 4)
    last_phono = read_number(file_bytes, "<I", base_offset + 0x38, 4)
    last_fertilized = read_number(file_bytes, "<I", base_offset + 0x40, 4)
    last_choco = read_number(file_bytes, "<I", base_offset + 0x48, 4)

    user['data']['zen_garden']['plants'].append({
      'type': plant_type,
      'location': location,
      'pos': (column, row),
      'dir': direction,
      'last_watered': last_watered,
      'color': color,
      'fertilized_amount': fertilized_amount,
      'watered_amount': watered_amount,
      'watered_need_amount': watered_need_amount,
      'happiness_need': happiness_need,
      'last_phono': last_phono,
      'last_fertilized': last_fertilized,
      'last_choco': last_choco,
    })

  return user

PLANT_TYPE_NAMES = [
  'Peashooter',
  'Sunflower',
  'Cherry Bomb',
  'Wall-nut',
  'Potato Mine',
  'Snow Pea',
  'Chomper',
  'Repeater',
  'Puff-shroom',
  'Sun-shroom',
  'Fume-shroom',
  'Grave Buster',
  'Hypno-shroom',
  'Scaredy-shroom',
  'Ice-shroom',
  'Doom-shroom',
  'Lily Pad',
  'Squash',
  'Threepeater',
  'Tangle Kelp',
  'Jalapeno',
  'Spikeweed',
  'Torchwood',
  'Tall-nut',
  'Sea-shroom',
  'Plantern',
  'Cactus',
  'Blover',
  'Split Pea',
  'Starfruit',
  'Pumpkin',
  'Magnet-shroom',
  'Cabbage-pult',
  'Flower Pot',
  'Kernel-pult',
  'Coffee Bean',
  'Garlic',
  'Umbrella Leaf',
  'Marigold',
  'Melon-pult',
  'Gatling Pea',
  'Twin Sunflower',
  'Gloom-shroom',
  'Cattail',
  'Winter Melon',
  'Gold Magnet',
  'Spikerock',
  'Cob Cannon',
  'Imitater',
  'Explode-o-nut',
  'Giant Wall-nut',
  'Sprout',
  'Left-facing Repeater',
]

def get_plant_type_name(plant_type):
  return PLANT_TYPE_NAMES[plant_type]

PLANT_COLOR = [
  'Low saturation',
  'None',
  'Magenta',
  'Orange',
  'Pink',
  'Cyan',
  'Red',
  'Blue',
  'Purple',
  'Light purple',
  'Yellow',
  'Light green'
]

def get_plant_color_name(plant_color):
  return PLANT_COLOR[1] if plant_color == 0 else PLANT_COLOR[plant_color - 1]

PLANT_LOCATION = [
  'Zen Garden',
  'Mushroom Garden',
  'Wheel Barrow',
  'Aquarium Garden',
]

PLANT_DIR = [
  'Faces right',
  'Faces left',
]

class FileBinaryReader:
  def __init__(self, data) -> None:
    self.__data = data
    self.__cursor = 0

  @property
  def cursor(self):
    return self.__cursor
  
  @cursor.setter
  def cursor(self, value):
    self.__cursor = value

  def read_uint16(self, offset: int | None = None):
    if offset is not None:
      cur_bak = self.__cursor
      self.__cursor = offset

    res = struct.unpack_from("<H", self.__data, self.__cursor)[0]

    if offset is not None:
      self.__cursor = cur_bak
    else:
      self.__cursor += 2

    return res
  
  def read_uint32(self, offset: int | None = None):
    if offset is not None:
      cur_bak = self.__cursor
      self.__cursor = offset

    res = struct.unpack_from("<I", self.__data, self.__cursor)[0]

    if offset is not None:
      self.__cursor = cur_bak
    else:
      self.__cursor += 4

    return res
  
  def read_string(self, offset: int | None = None):
    if offset is not None:
      cur_bak = self.__cursor
      self.__cursor = offset

    str_len = self.read_uint16()

    res = self.__data[self.__cursor:(self.__cursor + str_len)].decode("utf-8")

    if offset is not None:
      self.__cursor = cur_bak
    else:
      self.__cursor += str_len

    return res
  
class FileBinaryWriter:
  def __init__(self, file) -> None:
    self.__file = file
    self.__buffer = bytearray([0x00]) * 4

  def write_uint16(self, value):
    struct.pack_into("<I", self.__buffer, 0, value)
    self.__file.write(self.__buffer[0:2])

  def write_uint32(self, value):
    struct.pack_into("<I", self.__buffer, 0, value)
    self.__file.write(self.__buffer[0:4])

  def write_string(self, value: str):
    str_bytes = value.encode('utf-8')
    self.write_uint16(len(str_bytes))
    self.__file.write(str_bytes)