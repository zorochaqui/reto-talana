from module.keys.interfaces.keys import KeyManagerInterface
from constant.statics import COMBOS, KEYS
from module.keys.container.keys import KeyPress, KeyComboPress,\
                                        KeyAction, KeyCombo

class KeyManager(KeyManagerInterface, KeyAction, KeyCombo):
        
    def key_init_keys_list(self):
        for key in KEYS:
            key_pres = KeyPress()
            key_pres.key = key["key"].lower()
            key_pres.action = key["action"]
            self.key_press(key_pres)
    
    def key_init_combo_list(self):
        for combo in COMBOS:
            combo_pres = KeyComboPress()
            combo_pres.combo = combo["combo"].lower()
            combo_pres.energy = combo["energy"]
            combo_pres.name = combo["name"]
            self.Key_combo_action(combo_pres)
    
    def key_get_press(self, moves:str) ->list:
        
        key_action_map = {key_p.key: key_p.action for key_p in self.key_actions}
        data = [key_action_map.get(move, "") for move in moves]
        return data
    
    def key_get_combo_press(self, moves:str, punch:str) ->list:
        combo = moves + punch
        combo_info = {}  
        for key_p in self.key_combo_actions:
            combo_info[key_p.combo] = (key_p.name, key_p.energy)
        
        matching_combos = [combo_info[key] for key in combo_info if key in combo and 'p' != key and 'k' != key]
       
        
        if len(matching_combos) == 0:
          
            combo_data = combo_info.get(punch, ("", 0))
        else:
            combo_data = matching_combos[0]
        
        return combo_data
     
    def key_search_action(self, moves:str, punch:str) ->dict:
        moves = moves.lower()
        punch = punch.lower()
        key = self.key_get_press(moves)
        name_combo, energy = self.key_get_combo_press(moves, punch)
        
        return {
            "move": key,
            "name_combo": name_combo,
            "energy": energy
        }