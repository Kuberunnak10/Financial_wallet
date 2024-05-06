from wallet import Wallet, calculate_balance, Transaction


def main():
    file_name = "data.txt"
    manager = Wallet(file_name)

    while True:
        print('_________________________')
        print("Личный финансовый кошелек\n")
        print("1. Вывести баланс")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            records = manager.read_records()
            incomes, expenses, balance = calculate_balance(records)
            print('_________________________')
            print(f"\nДоходы: {incomes} руб.")
            print(f"Расходы: {expenses} руб.")
            print(f"Баланс: {balance} руб.")

        elif choice == '2':
            date = input("Введите дату (гггг-мм-дд): ")
            category = input("Введите категорию (Доход/Расход): ")
            amount = int(input("Введите сумму: "))
            description = input("Введите описание: ")
            record = Transaction(date, category, amount, description)
            manager.add_record(record)
            print('_________________________')
            print("Запись добавлена.")

        elif choice == '3':
            old_date = input("Введите старую дату (гггг-мм-дд): ")
            old_category = input("Введите старую категорию (Доход/Расход): ")
            old_amount = int(input("Введите старую сумму: "))
            old_description = input("Введите старое описание: ")

            new_date = input("Введите новую дату (гггг-мм-дд): ")
            new_category = input("Введите новую категорию (Доход/Расход): ")
            new_amount = int(input("Введите новую сумму: "))
            new_description = input("Введите новое описание: ")

            new_record = Transaction(new_date, new_category, new_amount, new_description)

            manager.replace_record(old_date, old_category, old_amount, old_description, new_record)
            print('_________________________')
            print("Запись успешно изменена.")

        elif choice == '4':
            category = input("Введите категорию (Доход/Расход), или оставьте пустым: ")
            date = input("Введите дату (гггг-мм-дд), или оставьте пустым: ")
            amount = input("Введите сумму, или оставьте пустым: ")
            found_records = manager.find_records(category, date, amount)
            print('_________________________')
            print("\nНайденные записи:")
            print(found_records)

        elif choice == '5':
            print('_________________________')
            print("До свидания")
            break

        else:
            print('_________________________')
            print("Неверный ввод.")


if __name__ == "__main__":
    main()
