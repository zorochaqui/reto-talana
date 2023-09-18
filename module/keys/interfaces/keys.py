class KeyPressInterface:
    key:str
    action:str

class KeyComboPressInterface:
    combo:str
    energy:int
    name:str

class KeyInitInterface:
    key_actions:list = []
    key_combo_actions:list = []

class KeyActionInterface(KeyInitInterface):
    def key_press(self, key_press:KeyPressInterface) ->None:
        pass

class KeyComboInterface(KeyInitInterface):
    def Key_combo_action(self, combo_press:KeyComboPressInterface)->None:
        pass

class KeyManagerInterface(KeyActionInterface, KeyComboInterface):
    
    def key_init_keys_list(self) ->None:
        pass
    
    def key_init_combo_list(self) ->None:
        pass
    
    def key_get_press(self, moves:str) ->list:
        pass
    
    def key_get_combo_press(self, combo:str) ->list:
        pass
    
    def key_search_action(self, move:str, punch:str) ->dict:
        pass