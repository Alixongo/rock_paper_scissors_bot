from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Клавиатура через ReplyKeboardBuilder -------

# Создём кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом widht=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаём клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
	one_time_keyboard=True,
	resize_keyboard=True)


# ------- Создаём игровую клавиатуру без использования билдера -------

# Создаём кнопки игровой клавиатуры
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['paper'])
button_3 = KeyboardButton(text=LEXICON_RU['scissors'])

# Создаём игровую клавиатуру с кнопками КаНоБу как список списков
game_kb = ReplyKeyboardMarkup(
	keyboard=[[button_1],
				[button_2],
				[button_3]],
	resize_keyboard=True)