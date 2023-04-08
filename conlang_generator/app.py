from backend.word_type import WordType
from backend.characteristic import ComplexCharacteristic, Characteristic, CharacteristicStack
from backend.characteristics.sufix import Sufix
from backend.word import Word

gender = ComplexCharacteristic("")
gender.add_variant("femenino", Sufix({"sufix":"a"}))
gender.add_variant("masculino", Sufix({"sufix":"o"}))

number = ComplexCharacteristic("singular")
number.add_variant("singular", Characteristic())
number.add_variant("plural", Sufix({"sufix":"s"}))

noun = CharacteristicStack()
noun.insert_item(1, "gender", gender)
noun.insert_item(1, "number", number)

my_word = Word("gat", noun)

my_word.characteristics.insert_item(0, "aumentativo", Sufix({"sufix":"az"}))


my_word.set_characteristic_value("gender", "masculino")
my_word.set_characteristic_value("number", "plural")

print(my_word.get_string_representation())

my_word.characteristics.move_item(0, 1)

print("moved")

print(my_word.get_string_representation())

my_word.characteristics.move_item("word_type", 1)
print("moved")

print(my_word.get_string_representation())
