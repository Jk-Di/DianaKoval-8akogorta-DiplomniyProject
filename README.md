﻿# Тесты на проверку получения данных о заказе по его треку после создания заказа в Яндекс Самокат с помощью API Яндекс Самокат.
- Для запуска теста должны быть установлены пакеты pytest и requests
- Запуск теста выполянется командой pytest
- Тест включает следующие шаги:
1) Выполнить запрос на создание заказа.
2) Сохранить номер трека заказа.
3) Выполнить запрос на получения заказа по треку заказа.
4) Проверить, что код ответа равен 200.
