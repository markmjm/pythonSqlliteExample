import utils.database as db
import json

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to listt all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit
Your Choice: 
"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input.lower() != 'q':
        if user_input.strip().lower() == 'a':
            prompt_add_book()
        elif user_input.strip().lower() == 'l':
            list_books()
        elif user_input.strip().lower() == 'r':
            prompt_read_book()
        elif user_input.strip().lower() == 'd':
            prompt_delete_book()
        else:
            print('Unknown input, please try again')
        user_input = input(USER_CHOICE)
    print('Done!')


def prompt_add_book():
    name = input("Book name please: ")
    author = input("Book author please: ")
    if len(name.strip()) > 0 and len(author.strip()) > 0:
        db.add_book(name,author)
    else:
        print(f'Invalid book name or author')


def list_books():
    bks = db.get_all_books()
    for bk in bks:
        bk['read'] = 'YES' if bk['read'] else 'NO'
        print(bk)


def prompt_read_book():
    name = input("Book name please: ")
    db.update_read_book(name)


def prompt_delete_book():
    name = input("Book name please: ")
    db.delete_book(name)


db.create_book_table()
menu()
print('Done')
