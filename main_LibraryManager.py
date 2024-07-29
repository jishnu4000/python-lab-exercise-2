from LibraryManager import LibraryManager

if __name__ == '__main__':
  lm = LibraryManager()

  print('Adding a new book')
  lm.add_book(
    isbn='978-9356061316',
    title='Computer Networking',
    author='James F. Kurose',
    publisher='Pearson Education',
    volume=8,
    year=2022
  )

  print()
  print('Check if newly added book is available.')
  lm.book_available(isbn='978-9356061316')

  print('--------------------------------------------')
  print('Delete the new added book.')
  lm.delete_book(isbn='978-9356061316')

  print()
  print('Check if newly added book is available.')
  lm.book_available(isbn='978-9356061316')

  print('--------------------------------------------')
  print('Retrieve a single book.')
  lm.get_book(isbn='978-0674278660')

  print('--------------------------------------------')
  print('Search for a book with different inputs.')
  print('Search by title.')
  search_res = lm.search_for_book(title='Python')
  for key, val in search_res.items():
    print(f'ISBN: {key}')
    lm.get_book(isbn=key)
    print()


  print('--------------------------------------------') 
  print('List all the books in the library')
  lm.get_all_books()

  print()
  print('--------------------------------------------')
  print('Updating a book')
  lm.add_book(
    isbn='978-9356061316',
    title='Computer Networking',
    author='James F. Kross',
    publisher='Pearson Education',
    volume=7,
    year=2021
  )
  print(f'Before update')
  lm.get_book(isbn='978-9356061316')
  
  print()
  lm.update_book(isbn='978-9356061316', author='James F. Kurose', volume=8, year=2022)
  print()

  print(f'After update')
  lm.get_book(isbn='978-9356061316')

  print('--------------------------------------------')
  print('Checking availability of a book.')
  lm.book_available(isbn='978-1680507225')
  print()
  lm.book_available(isbn='978-1234567890')