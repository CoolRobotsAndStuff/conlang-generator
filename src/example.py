from word_type import WordType
from characteristic import ComplexCharacteristic, Characteristic, CharacteristicStack
from characteristics.sufix import Sufix
from word import Word

gender = ComplexCharacteristic("masculino")
gender.add_variant("femenino", Sufix("a"))
gender.add_variant("masculino", Sufix("o"))

number = ComplexCharacteristic("plural")
number.add_variant("singular", Characteristic())
number.add_variant("plural", Sufix("s"))

noun = CharacteristicStack()
noun.insert_item(1, "gender", gender)
noun.insert_item(1, "number", number)

my_word = Word("gat", noun)

my_word.characteristics.insert_item(0, "aumentativo", Sufix("az"))

print(my_word)

#my_word.set_characteristic("gender", "masculino")

#print(my_word)

#my_word.set_characteristic("number", "plural")

#print(my_word)




