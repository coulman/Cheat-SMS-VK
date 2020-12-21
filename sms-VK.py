import vk_api
import random
from time import sleep

token_ = input("Введите свой токен ВК: ")
vk_session = vk_api.VkApi(token=token_)
vk = vk_session.get_api()
sender = ["Привет!", "Всмысле?", "Воуу это ты??", "Разве?", "Что??", "Ты кто?", "Знакомы?"]
time = int(input("Введите задержку (Defult 30 Sek): "))
print("Запуск скрипта!")
print()
sleep(4)
print("Скрипт успешно запущен!")

while True:
    try:

            idr = random.randint(600000000, 700000000)
            proverka = vk.users.get(user_ids=idr)

            print(idr)
            print(proverka)

            if "DELETE" in proverka:
                continue

            vk.messages.send(user_id=idr, message=random.choice(sender), random_id=0)
            print("Байтанул")
            sleep(time)

    except:
        No = None
