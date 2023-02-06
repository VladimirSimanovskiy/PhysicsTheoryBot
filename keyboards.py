from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# main keyboard
kb_main = InlineKeyboardMarkup(row_width=2)

kinematics = InlineKeyboardButton(text='Кинематика', callback_data='kinematics')
dinamics = InlineKeyboardButton(text='Динамика', callback_data='dinamics')
molecular = InlineKeyboardButton(text='Молекулярная физика и термодинамика', callback_data='molecular')
electrostatics = InlineKeyboardButton(text='Электростатика', callback_data='electrostatics')
electricity = InlineKeyboardButton(text='Постоянный ток', callback_data='electricity')
electromagnetic = InlineKeyboardButton(text='Электромагнитные явления', callback_data='electromagnetic')
eosc_ewifes = InlineKeyboardButton(text='Электомагнитные колебания и волны', callback_data='el_waves')
optics = InlineKeyboardButton(text='Оптика', callback_data='optics')
theory_of_relativity = InlineKeyboardButton(text='Теория относительности', callback_data='relativity')
atomic = InlineKeyboardButton(text='Атомная физика', callback_data='atomic')


kb_main.add(kinematics, dinamics).add(molecular).add(electrostatics, electricity).add(electromagnetic).add(eosc_ewifes).add(optics).add(theory_of_relativity).add(atomic)

# kinematic keyboard
kb_kinematic = InlineKeyboardMarkup()

ucm = InlineKeyboardButton(text='Равномерное прямолинейное движение', callback_data='ucm')
add_speeds = InlineKeyboardButton(text='Закон сложения скоростей', callback_data='add_speeds')
um = InlineKeyboardButton(text='Неравномерное движение', callback_data='um')
acc_m = InlineKeyboardButton(text='Равноускоренное движение', callback_data='acc_m')
fgm = InlineKeyboardButton(text='Движение под действием силы тяжести', callback_data='fgm')
main_menu = InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')

kb_kinematic.add(ucm).add(add_speeds).add(um).add(acc_m).add(fgm).add(main_menu)

# dinamics keyboard
kb_dinamic = InlineKeyboardMarkup()

newtons = InlineKeyboardButton(text='Законы Ньютона, силы', callback_data='newtons')
conservations = InlineKeyboardButton(text='Законы сохранения в механике', callback_data='conservations')
vaw = InlineKeyboardButton(text='Механические колебания и волны', callback_data='vaw')
main_menu = InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')

kb_dinamic.add(newtons).add(conservations).add(vaw).add(main_menu)

# molecular keyboard
kb_molecular = InlineKeyboardMarkup()

mkt = InlineKeyboardButton(text='Основы молекулярно-кинетической теории', callback_data='mkt')
gas_laws = InlineKeyboardButton(text='Основное уравнение МКТ. Газовые законы', callback_data='gas_laws')
thermodyn = InlineKeyboardButton(text='Основы термодинамики', callback_data='thermodyn')
main_menu = InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')

kb_molecular.add(mkt).add(gas_laws).add(thermodyn).add(main_menu)

# optics keyboard
kb_optics = InlineKeyboardMarkup()

geometric_optics = InlineKeyboardButton(text='Геометрическая оптика', callback_data='geooptics')
wave_quantum_optics = InlineKeyboardButton(text='Волновая и квантовая оптика',callback_data='waveoptics')
main_menu = InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')

kb_optics.add(geometric_optics).add(wave_quantum_optics).add(main_menu)

# relativity
kb_relativity = InlineKeyboardMarkup()

postulates = InlineKeyboardButton(text='Постулаты специальной теории относительности', callback_data='postulates')
сonsequences = InlineKeyboardButton(text='Следствия из постулатов теории относительности', callback_data='сonsequences')

kb_relativity.add(postulates).add(сonsequences).add(main_menu)