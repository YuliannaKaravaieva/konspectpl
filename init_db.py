import sqlite3


DATABASE_NAME = "konspect.db"


def create_database(connection):
	connection.execute(
		"""
		CREATE TABLE IF NOT EXISTS words (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			polish_word TEXT NOT NULL UNIQUE,
			translation TEXT NOT NULL,
			rule TEXT DEFAULT ''
		)
		"""
	)
	connection.commit()


def add_word(connection):
	polish_word = input("Польское слово: ").strip()
	translation = input("Перевод: ").strip()
	rule = input("Правило (можно оставить пустым): ").strip()

	if not polish_word or not translation:
		print("Слово и перевод обязательны.")
		return

	try:
		connection.execute(
			"INSERT INTO words (polish_word, translation, rule) VALUES (?, ?, ?)",
			(polish_word, translation, rule),
		)
		connection.commit()
		print("Запись сохранена.")
	except sqlite3.IntegrityError:
		print("Такое слово уже есть в базе.")


def list_words(connection):
	words = connection.execute(
		"SELECT id, polish_word, translation FROM words ORDER BY polish_word"
	).fetchall()

	if not words:
		print("База пока пустая.")
		return

	for word_id, polish_word, translation in words:
		print(f"{word_id}. {polish_word} — {translation}")


def find_word(connection):
	search = input("Искать слово: ").strip()
	words = connection.execute(
		"SELECT polish_word, translation, rule FROM words "
		"WHERE polish_word LIKE ? ORDER BY polish_word",
		(f"%{search}%",),
	).fetchall()

	if not words:
		print("Ничего не найдено.")
		return

	for polish_word, translation, rule in words:
		print(f"\n{polish_word} — {translation}")
		if rule:
			print(f"Правило: {rule}")


def main():
	connection = sqlite3.connect(DATABASE_NAME)
	create_database(connection)
	print(f"База данных готова: {DATABASE_NAME}")
	print("Команды: add — добавить, list — показать все, find — найти, exit — выйти")

	try:
		while True:
			command = input("\nВведите команду: ").strip().lower()
			if command == "add":
				add_word(connection)
			elif command == "list":
				list_words(connection)
			elif command == "find":
				find_word(connection)
			elif command in {"exit", "quit"}:
				break
			else:
				print("Неизвестная команда. Используйте add, list, find или exit.")
	finally:
		connection.close()


if __name__ == "__main__":
	main()
