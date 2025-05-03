from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_works = ReplyKeyboardMarkup(keyboard=
[
 [
  KeyboardButton(text='ВПР'),
  KeyboardButton(text='ОГЭ'),
  KeyboardButton(text='ЕГЭ')
 ]
],resize_keyboard=True)

kb_works_vpr_only = ReplyKeyboardMarkup(keyboard=
[
 [
  KeyboardButton(text='ВПР')
 ]
],resize_keyboard=True)

kb_works_oge_vpr = ReplyKeyboardMarkup(keyboard=
[
 [
  KeyboardButton(text='ВПР'),
  KeyboardButton(text='ОГЭ')
 ]
],resize_keyboard=True)

kb_works_ege_vpr = ReplyKeyboardMarkup(keyboard=
[
 [
  KeyboardButton(text='ВПР'),
  KeyboardButton(text='ЕГЭ')
 ]
],resize_keyboard=True)

kb_lessons = ReplyKeyboardMarkup(keyboard=[
 [
  KeyboardButton(text='Алгебра'),
  KeyboardButton(text='Геометрия'),
  KeyboardButton(text='Физика'),
  KeyboardButton(text='Биология'),
  KeyboardButton(text='География'),
  KeyboardButton(text='История')
 ]
],resize_keyboard=True)

kb_classes = ReplyKeyboardMarkup(keyboard=[
 [
  KeyboardButton(text='7'),
  KeyboardButton(text='8'),
  KeyboardButton(text='9'),
  KeyboardButton(text='10'),
  KeyboardButton(text='11')
 ]
],resize_keyboard=True)
kb_var = ReplyKeyboardMarkup(keyboard=[
   [
      KeyboardButton(text='1 вариант '),
      KeyboardButton(text='2 вариант ')
   ]
],resize_keyboard=True)