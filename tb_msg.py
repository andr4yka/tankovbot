#Список воозжможных сообщений.
import asyncio


tb_not_found = "Команда или аргумент некорректны! Проверьте написание если уверены в наличии данного функционала."
startmsg = """Бот с функцией крутануть кок ✅
\nКанал с приколами если они будут: @tnkv_shitpost
Доступные команды:
<code>/кок</code>

Потом сделаю топы по кокам и напишу обязательно в щитпост если не забуду"""


async def tb_indev(command: str):
    return f"""Команда "{command}" находится в разработке, или отключена."""

def cockmsg(deystv: str, num = 0):
    if deystv == "otval":
        return "🤯 | Ваш кок оторвался и улетел вдаль, пиздец...\nЕго длина была равна: " + str(num) + " см."
    elif deystv == "x2":
        return "😎 | Ваш кок увеличился в два раза!\nТеперь его длина равна: " + str(num) + " см."
    elif deystv == "+":
        return "➕ | Ваш кок увеличился на " + str(num)+ " см."
    else:
        return "➖ | Ваш кок уменьшился на " + str(num)+ " см."