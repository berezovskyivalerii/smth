import os

FILENAME = 'music_collection.txt'

def add_album():
    """Add a new album to the collection (music_collection.txt)."""

    title = input("Enter the album title: ")
    author = input("Enter the author name: ")
    year = input("Enter the year: ")

    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(f"{title} - {author} - {year}\n")
    print("Album added!\n")

def show_all_albums():
    """Display all albums in the collection (music_collection.txt)."""

    with open(FILENAME, 'r', encoding='utf-8') as file:
        albums = file.readlines()
        if not albums:
            print("collection is empty.\n")
        else:
            print("List of all songs:")
            for album in albums:
                print(album.strip())
            print()

def search_by_author():
    """Search for albums by a specific author."""

    author = input("Enter the author's name: ")
    found = False
    with open(FILENAME, 'r', encoding='utf-8') as file:
        for line in file:
            if author.lower() in line.lower():
                print(line.strip())
                found = True
    if not found:
        print("No albums found by that author.\n")

def delete_album():
    """Delete an album from the collection (music_collection.txt)."""

    #Функция добавляет все строки из файла в new_lines кроме той, которую мы хотим удалить,
    #затем new_lines перезаписывает в файл.
    title = input("Enter the title of the album to delete: ")
    new_lines = []
    is_deleted = False
    with open(FILENAME, 'r', encoding='utf-8') as file:
        for line in file:
            if line.lower().startswith(title.lower()):
                is_deleted = True
                continue
            new_lines.append(line)
    with open(FILENAME, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
    if is_deleted:
        print("Album deleted.\n")
    else:
        print("Album not found.\n")

while True:
    print("\nMenu:")
    print("1. Add a new album")
    print("2. View all albums")
    print("3. Search albums by author")
    print("4. Delete an album")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_album()
    elif choice == '2':
        show_all_albums()
    elif choice == '3':
        search_by_author()
    elif choice == '4':
        delete_album()
    elif choice == '5':
        break
    else:
        print("Retry.\n")