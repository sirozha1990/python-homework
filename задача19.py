# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
import csv

# Функция для импорта данных из файла .txt
def import_data():
    with open('phonebook.txt', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        phonebook = list(reader)
    return phonebook

# Функция для экспорта данных в файл .txt
def export_data(phonebook):
    with open('phonebook.txt', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(phonebook)

# Функция для поиска записей по имени, фамилии или номеру телефона
def search_record(phonebook):
    search_criteria = input('Enter search criteria: ')
    for record in phonebook:
        if search_criteria in record:
            print(record)

# Функция для добавления новой записи
def add_record(phonebook):
    new_record = []
    new_record.append(input('Enter last name: '))
    new_record.append(input('Enter first name: '))
    new_record.append(input('Enter middle name: '))
    new_record.append(input('Enter phone number: '))

    phonebook.append(new_record)
    print('Record added successfully!')

# Функция для удаления записи
def delete_record(phonebook):
    search_criteria = input('Enter search criteria: ')
    for record in phonebook:
        if search_criteria in record:
            phonebook.remove(record)
            print('Record deleted successfully!')

            # Функция для изменения существующей записи
def edit_record(phonebook):
    search_criteria = input('Enter search criteria: ')
    for record in phonebook:
        if search_criteria in record:
            print('What do you want to edit?')
            print('1 - Last name')
            print('2 - First name')
            print('3 - Middle name')
            print('4 - Phone number')

            option = int(input('Enter option: '))

            if option == 1:
                record[0] = input('Enter new last name: ')
            elif option == 2:
                record[1] = input('Enter new first name: ')
            elif option == 3:
                record[2] = input('Enter new middle name: ')
            elif option == 4:
                record[3] = input('Enter new phone number: ')

            print('Record updated successfully!')

            # Основная функция программы    
def main():    
    phonebook = import_data()

    while True:
        print('1 - Search record')
        print('2 - Add record')
        print('3 - Delete record')
        print('4 - Edit record')
        print('5 - Exit')

        option = int(input('Enter option: '))

        if option == 1:
            search_record(phonebook)
        elif option == 2:
            add_record(phonebook)
        elif option == 3:
            delete_record(phonebook)
        elif option == 4:
            edit_record(phonebook)        
        else: # option == 5 
            export_data(phonebook)    
            break

    
if __name__ == '__main__':    
    main()