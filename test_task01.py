from task01 import AddressBook, Record

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print("All records in the address book:")
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
assert john is not None
john.edit_phone("1234567890", "1112223333")

print("\nUpdated John record:")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
if found_phone:
    print(f"\nFound phone in John's record: {found_phone}")  # Виведення: 5555555555
else:
    print("\nPhone not found.")

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів після видалення Jane
print("\nAll records after deleting Jane:")
for name, record in book.data.items():
    print(record)