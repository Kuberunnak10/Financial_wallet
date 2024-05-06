class Transaction:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"Дата: {self.date}\nКатегория: {self.category}\nСумма: {self.amount}\nОписание: {self.description}"


class Wallet:
    def __init__(self, file_name):
        self.file_name = file_name

    # Метод Добавления записи
    def add_record(self, record):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(str(record) + '\n\n')

    # Метод прочтения записи
    def read_records(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            return file.read()

    # Метод изменения записи
    def replace_record(self, old_date, old_category, old_amount, old_description, new_record):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        replaced = False

        with open(self.file_name, 'w', encoding='utf-8') as file:
            i = 0
            while i < len(lines):
                if (f"Дата: {old_date}\n" == lines[i] and
                        f"Категория: {old_category}\n" == lines[i + 1] and
                        f"Сумма: {old_amount}\n" == lines[i + 2] and
                        f"Описание: {old_description}\n" == lines[i + 3]):
                    file.write(str(new_record) + '\n\n')
                    replaced = True
                    i += 4
                else:
                    file.write(lines[i])
                    i += 1

        if not replaced:
            print("Запись не найдена.")

    # Метод нахождения запили или записей
    def find_records(self, category=None, date=None, amount=None):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            records = file.read().split('\n\n')
            found_records = []
            for record in records:
                if category and f"Категория: {category}" not in record:
                    continue
                if date and f"Дата: {date}" not in record:
                    continue
                if amount and f"Сумма: {amount}" not in record:
                    continue
                found_records.append(record)
            return "\n\n".join(found_records)


# Функция подсчета доходов и расходов
def calculate_balance(records):
    incomes = 0
    expenses = 0
    for record in records.split('\n\n'):
        lines = record.strip().split('\n')
        if len(lines) >= 3:
            category = lines[1].split(': ')[1]
            amount = int(lines[2].split(': ')[1])
            if category == 'Доход':
                incomes += amount
            elif category == 'Расход':
                expenses += amount
    return incomes, expenses, incomes - expenses
