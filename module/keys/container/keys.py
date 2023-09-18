from module.keys.interfaces.keys import KeyPressInterface, KeyComboPressInterface, \
                                        KeyActionInterface, KeyComboInterface, \
                                        KeyInitInterface

class KeyPress(KeyPressInterface):
    key:str
    action:str

class KeyComboPress(KeyComboPressInterface):
    combo:str
    energy:int
    name:str

class KeyAction(KeyActionInterface, KeyInitInterface):
    def key_press(self, key_press:KeyPressInterface) ->None:
        self.key_actions.append(key_press)

class KeyCombo(KeyComboInterface, KeyInitInterface):
    def Key_combo_action(self, combo_press:KeyComboPressInterface)->None:
        self.key_combo_actions.append(combo_press)