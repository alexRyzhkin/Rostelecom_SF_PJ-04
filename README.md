 Итоговый проект по автоматизации тестирования курса "тестировщик-автоматизатор на Python". 
         Были поставленны следующие задачи:
 - изучить бриф от заказчика;
 - протестировать требования;
 - разработать тест-кейсы (не менее 15);
 - провести автоматизированное тестирование продукта;
 - описать обнаруженные дефекты.

В ходе выполнения проекта были применены различные инструменты и техники тест-дизайна.
         Инструменты:
1. PyCharm -среда программирования для автоматизации тестирования.
2. DevTools - набор инструментов разработчика в браузере, для создания, отладки и анализа работы элементов страницы.
3. Elements locator - это свойства элементов в HTML, которые сообщают инструменту тестирования (например, Selenium) о веб-элементе, с которым нужно взаимодействовать.
         Техники тест-дизайна:
1. Метод «черного ящика» - этот метод использовался для всех тест-кейсов. 
2. Классы эквивалентности и анализа граничных значений - применялся при тестировании полей ввода формы регистрации.
3. Позитивное и негативное тестирование - метод применялся для тестирования полей ввода формы авторизации и регистрации.
4. Тестирование состояний и переходов - метод использовался для проверки корректного перехода между страницами.
   Тестовою документацию можно посмотреть по ссылке: https://docs.google.com/spreadsheets/d/1yO8sZbw1VRz1lRpLTt7uI6BhhTNx6sSjgy2TqvaBD4c/edit?usp=sharing

   Шаги по запуску тестов:
1.Установить requirements (Python3, библиотеки: PyTest , PyTest - Selenium; PageObject, Smart Page Object): pip3 install -r requirements.txt
2.Скачать драйвер для вашей версии браузера
3.Запустить тесты: python -m pytest -v —driver Chrome —driver-path
