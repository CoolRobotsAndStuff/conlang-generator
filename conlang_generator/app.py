from collections import UserString

from backend.word_type import WordType
from backend.characteristic.complex_characteristic import ComplexCharacteristicBuilder
from backend.characteristic.simple_characteristic import SimpleCharacteristicBuilder
from backend.characteristic.characteristic_stack import CharacteristicStackBuilder

from backend.assets.characteristics.sufix import SufixBuilder

from backend.word import WordBuilder
from backend.project import Project

spanish = Project()

complex_builder = ComplexCharacteristicBuilder()
simple_builder = SimpleCharacteristicBuilder()
sufix_builder = SufixBuilder()
stack_builder = CharacteristicStackBuilder()

sufix_builder.set_argument("sufix", UserString("a"))
complex_builder.add_variant("femenino", sufix_builder.get_characteristic())

sufix_builder.set_argument("sufix", UserString("o"))
complex_builder.add_variant("masculino", sufix_builder.get_characteristic())

stack_builder.add_characteristic("gender", complex_builder.get_complex_characteristic())


complex_builder.add_variant("singular", simple_builder.get_characteristic())

sufix_builder.set_argument("sufix", UserString("s"))
complex_builder.add_variant("plural", sufix_builder.get_characteristic())

complex_builder.set_default_value("singular")

stack_builder.add_characteristic("number", complex_builder.get_complex_characteristic())
               
spanish.characteristic_stacks["noun"] = stack_builder.get_stack()



word_builder = WordBuilder()

word_builder.set_base(UserString("gat")) \
            .add_word_type(spanish.characteristic_stacks["noun"])

spanish.words["cat"] = word_builder.get_word()

spanish.words["cat"].set_characteristic_value("gender", "masculino")
spanish.words["cat"].set_characteristic_value("number", "plural")

spanish.words["cat"].apply_characteristics()

print(spanish.words["cat"].get_string_representation())
