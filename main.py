from aiogram import Bot, executor, Dispatcher, types
from config import TOKEN_API
from keyboards import kb_main, kb_kinematic, kb_dinamic, kb_molecular, kb_optics, kb_relativity

bot =Bot(token=TOKEN_API)
dp =Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message) -> None:
    await bot.send_message(chat_id=msg.from_user.id,
                           text='Выбери интересующий раздел',
                           reply_markup=kb_main)

# kinematics
@dp.callback_query_handler(lambda c: c.data == 'kinematics')
async def call_kinematics(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id,
                           reply_markup=kb_kinematic,
                           text='Выбери интересующую тему')

@dp.callback_query_handler(lambda c: c.data == 'ucm')
async def call_ucm(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Kinematics/rpd.JPG"),
                         reply_markup=kb_kinematic)

@dp.callback_query_handler(lambda c: c.data == 'add_speeds')
async def call_add_speeds(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Kinematics/ЗСС.JPG"),
                         reply_markup=kb_kinematic)

@dp.callback_query_handler(lambda c: c.data == 'um')
async def call_um(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Kinematics/Неравномерное.JPG"),
                         reply_markup=kb_kinematic)

@dp.callback_query_handler(lambda c: c.data == 'acc_m')
async def call_acc_m(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Kinematics/РУД.JPG"),
                         reply_markup=kb_kinematic)

@dp.callback_query_handler(lambda c: c.data == 'fgm')
async def call_fgm(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Kinematics/Под действием СТ_1.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Kinematics/Под действием СТ_2.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Kinematics/Под действием СТ_3.JPG"),
                         reply_markup=kb_kinematic)
# dinamics
@dp.callback_query_handler(lambda c: c.data == 'dinamics')
async def call_dinamics(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id,
                           reply_markup=kb_dinamic,
                           text='Выбери интересующую тему')

@dp.callback_query_handler(lambda c: c.data == 'newtons')
async def call_newtons(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/Newtons_1.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/Newton_2.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/Newton_3.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/Newton_4.JPG"),
                         reply_markup=kb_dinamic)

@dp.callback_query_handler(lambda c: c.data == 'conservations')
async def call_conservations(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/cons_1.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/cons_2.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/cons_3.JPG"),
                         reply_markup=kb_dinamic)

@dp.callback_query_handler(lambda c: c.data == 'vaw')
async def call_vaw(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Dinamics/vaw.JPG"),
                         reply_markup=kb_dinamic)

# molecular
@dp.callback_query_handler(lambda c: c.data == 'molecular')
async def call_molecular(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id,
                           reply_markup=kb_molecular,
                           text='Выбери интересующую тему')

@dp.callback_query_handler(lambda c: c.data == 'mkt')
async def call_mkt(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Molecular/mkt_1.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Molecular/mkt_2.jpg"),
                         reply_markup=kb_molecular)

@dp.callback_query_handler(lambda c: c.data == 'gas_laws')
async def call_gas_laws(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Molecular/gas_laws_1.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Molecular/gas_laws_2.JPG"),
                         reply_markup=kb_molecular)

@dp.callback_query_handler(lambda c: c.data == 'thermodyn')
async def call_thermodyn(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Molecular/thermodyn_1.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Molecular/thermodyn_2.JPG"),
                         reply_markup=kb_molecular)

@dp.callback_query_handler(lambda c: c.data == 'main_menu')
async def start_main_menu(msg: types.Message) -> None:
    await bot.send_message(chat_id=msg.from_user.id,
                           text='Выбери интересующий раздел',
                           reply_markup=kb_main)

# electrostatics
@dp.callback_query_handler(lambda c: c.data == 'electrostatics')
async def call_electrostatics(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electrostatics/electrostatic_1.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electrostatics/electrostatic_2.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electrostatics/electrostatic_3.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electrostatics/electrostatic_4.jpg"),
                         reply_markup=kb_main)

# electricity
@dp.callback_query_handler(lambda c: c.data == 'electricity')
async def call_electricity(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electricity/electricity_1.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electricity/electricity_2.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electricity/electricity_3.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electricity/electricity_4.jpg"),
                         reply_markup=kb_main)

# electromagnetic
@dp.callback_query_handler(lambda c: c.data == 'electromagnetic')
async def call_electromagnetic(msg: types.Message):
     await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electromagnetic/electromagnetic_1.JPG"))
     await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electromagnetic/electromagnetic_2.JPG"),
                         reply_markup=kb_main)

# electromagnetic wafes
@dp.callback_query_handler(lambda c: c.data == 'el_waves')
async def call_el_waves(msg: types.Message):
     await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electromagnetic_waves/ElWaves_1.JPG"))
     await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Electromagnetic_waves/ElWaves_2.JPG"),
                         reply_markup=kb_main)

# optics
@dp.callback_query_handler(lambda c: c.data == 'optics')
async def call_optics(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id,
                           reply_markup=kb_optics,
                           text='Выбери интересующую тему')

@dp.callback_query_handler(lambda c: c.data == 'geooptics')
async def call_geooptics(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Optics/geooptics_1.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Optics/geooptics_2.jpg"),
                         reply_markup=kb_optics)

@dp.callback_query_handler(lambda c: c.data == 'waveoptics')
async def call_waveoptics(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Optics/waveoptics_1.jpg"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Optics/waveoptics_2.jpg"),
                         reply_markup=kb_optics)

# relativity
@dp.callback_query_handler(lambda c: c.data == 'relativity')
async def call_relativity(msg: types.Message):
    await bot.send_message(chat_id=msg.from_user.id,
                           reply_markup=kb_relativity,
                           text='Выбери интересующую тему')

@dp.callback_query_handler(lambda c: c.data == 'postulates')
async def call_postulates(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Relativity/postulates.JPG"),
                         reply_markup=kb_relativity)

@dp.callback_query_handler(lambda c: c.data == 'сonsequences')
async def call_сonsequences(msg: types.Message):
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Relativity/сonsequences_1.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Relativity/сonsequences_2.JPG"))
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Relativity/сonsequences_3.JPG"),
                         reply_markup=kb_relativity)

#atomic
@dp.callback_query_handler(lambda c: c.data == 'atomic')
async def call_atomic(msg: types.Message):
     await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Atomic/atomic_1.jpg"))
     await bot.send_photo(chat_id=msg.from_user.id,
                         photo=types.InputFile("img/Atomic/atomic_2.jpg"),
                         reply_markup=kb_main)

@dp.message_handler()
async def no_msg(msg: types.Message) -> None:
    await msg.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)