# Домашнее задание

## 3 месяц, модуль 21 - Работа с сетью II

Попрактиковаться в обработке http запросов через библиотеку socket
Цель: Закрепить знания полученные на занятии.
Написать сервер с использованием библиотеки socket, который будет получать http запрос и возвращать 
полученные заголовки в виде текста в ответе клиенту в формате json.

## Решение

1. Запустить сервер:
    ```bash
   python server.py
    ```
2. Открыть браузер и выполнить запрос:
    ```bash
    http://localhost:8889/
   ```
3. Закрыть подключение и остановить сервер, выполнив запрос:
    ```bash
    http://localhost:8889/close
   ```