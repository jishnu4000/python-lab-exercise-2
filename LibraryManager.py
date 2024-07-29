# Question 4
books_library = {
  "978-9356061590": {
      "title": "Computer Organization & Architecture",
      "author": "William Stallings",
      "publisher": "Pearson Education",
      "volume": 11,
      "year": 2022,
  },
  "978-9811968990": {
      "title": "Operating Systems: Internals and Design Principles",
      "author": "Davide Pastorello",
      "publisher": "Springer Verlag",
      "volume": 1,
      "year": 2023,
  },
  "978-9355421982": {
      "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
      "author": "Aurélien Géron",
      "publisher": "O'Reilly Media",
      "volume": 3,
      "year": 2022,
  },
  "978-1801071109": {
      "title": "Expert Python Programming",
      "author": "Michal Jaworski",
      "publisher": "Packt Publishing",
      "volume": 4,
      "year": 2021,
  },
  "978-0262046305": {
      "title": "Introduction to Algorithms",
      "author": "Thomas H. Cormen",
      "publisher": "MIT Press",
      "volume": 4,
      "year": 2022,
  },
  "978-1718502086": {
      "title": "Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming",
      "author": "Matthes Eric",
      "publisher": "No Starch Press",
      "volume": 1,
      "year": 2023,
  },
  "978-1292459660": {
      "title": "Modern Operating Systems",
      "author": "Andrew S. Tanenbaum",
      "publisher": "Pearson Education",
      "volume": 5,
      "year": 2023,
  },
  "978-9355326478": {
      "title": "Java: The Complete Reference, Thirteenth Edition",
      "author": "Herbert Schildt",
      "publisher": "McGraw-Hill Education",
      "volume": 13,
      "year": 2024,
  },
  "978-9390457151": {
      "title": "Core Python Programming, 3ed: Covers fundamentals to advanced topics like OOPS, Exceptions, Data structures, Files, Threads, Net",
      "author": "R. Nageswara Rao",
      "publisher": "Dreamtech Press",
      "volume": 3,
      "year": 2021,
  },
  "978-9355420831": {
      "title": "Fluent Python: Clear, Concise, and Effective Programming",
      "author": "Luciano Ramalho",
      "publisher": "O'Reilly Media",
      "volume": 2,
      "year": 2022,
  },
  "978-1839217166": {
      "title": "Mastering Python for Networking and Security",
      "author": "José Manuel Ortega",
      "publisher": "Packt Publishing",
      "volume": 2,
      "year": 2021,
  },
  "978-1098114831": {
      "title": "Reinforcement Learning",
      "author": "Phil Winder",
      "publisher": "O'Reilly Media",
      "volume": 1,
      "year": 2020,
  },
  "978-9356063570": {
      "title": "Artificial Intelligence: A Modern Approach",
      "author": "Stuart Russell",
      "publisher": "Pearson Education",
      "volume": 4,
      "year": 2022,
  },
  "978-9361591754": {
      "title": "AI for Everyone: A Beginner's Handbook for Artificial Intelligence (AI)",
      "author": "Saptarsi Goswami",
      "publisher": "Pearson Education",
      "volume": 1,
      "year": 2024,
  },
  "978-1617295485": {
      "title": "Advanced Algorithms and Data Structures",
      "author": "Marcello La Rocca",
      "publisher": "Manning",
      "volume": 1,
      "year": 2021,
  },
  "978-1292374062": {
      "title": "Computer Networks",
      "author": "Andrew S. Tanenbaum",
      "publisher": "Pearson Education",
      "volume": 6,
      "year": 2021,
  },
  "978-8193245286": {
      "title": "Data Structures And Algorithms Made Easy: Data Structures And Algorithmic Puzzles",
      "author": "Narasimha Karumanchi",
      "publisher": "Careermonk Publications",
      "volume": 1,
      "year": 2023,
  },
  "978-1098115784": {
      "title": "Machine Learning Design Patterns: Solutions to Common Challenges in Data Preparation, Model Building, and MLOps",
      "author": "Valliappa Lakshmanan",
      "publisher": "O'Reilly Media",
      "volume": 1,
      "year": 2020,
  },
  "978-1119439257": {
      "title": "Operating System Concepts",
      "author": "Abraham Silberschatz",
      "publisher": "Wiley",
      "volume": 10,
      "year": 2022,
  },
  "978-1680507225": {
      "title": "A Common-Sense Guide to Data Structures and Algorithms, Second Edition: Level Up Your Core Programming Skills",
      "author": "Jay Wengrow",
      "publisher": "Pragmatic Bookshelf",
      "volume": 2,
      "year": 2020,
  },
  "978-0674278660": {
      "title": "The Myth of Artificial Intelligence: Why Computers Can’t Think the Way We Do",
      "author": "Erik J. Larson",
      "publisher": "Pearson",
      "volume": 1,
      "year": 2022,
  },
  "978-1492055020": {
      "title": "High Performance Python: Practical Performant Programming for Humans",
      "author": "Micha Gorelick",
      "publisher": "O'Reilly Media",
      "volume": 2,
      "year": 2020,
  },
  "978-1789955248": {
      "title": "Python Data Analysis",
      "author": "Avinash Navlani",
      "publisher": "Packt Publishing",
      "volume": 3,
      "year": 2021,
  },
  "978-9355420329": {
      "title": "Natural Language Processing with Transformers: Building Language Applications with Hugging Face",
      "author": "Lewis Tunstall",
      "publisher": "O'Reilly Media",
      "volume": 1,
      "year": 2022,
  },
  "978-1492054054": {
      "title": "Practical Natural Language Processing: A Comprehensive Guide to Building Real-World NLP Systems",
      "author": "Sowmya Vajjala",
      "publisher": "O'Reilly Media",
      "volume": 1,
      "year": 2020,
  }
}

class LibraryManager:
    def __init__(self) -> None:
        self.library = books_library
    
    def add_book(self, isbn:str, title:str, author:str, publisher:str, volume:int, year:int) -> None:
        """
        Adds a book to the library.

        Args:
            isbn (str): Book ISBN number
            title (str): Book title
            author (str): Book author
            publisher (str): Book publisher
            volume (int): Book volume number
            year (int): Book year of release
        
        Returns:
            None
        """
        if isbn not in self.library:
            self.library[isbn] = {
                "title": title,
                "author": author,
                "publisher": publisher,
                "volume": volume,
                "year": year,
            }
            print(f'Book with ISBN: {isbn} has been added to the library.')
        else:
            print(f'Book with ISBN: {isbn} is already exists in the library.')
    
    def delete_book(self, isbn:str) -> None:
        """
        Remove a book from the library by the ISBN number.

        Args:
            isbn (str): Book ISBN number
        
        Returns:
            None
        """
        if isbn in self.library:
            # dictionary comprehension
            self.library = { key: value for key, value in self.library.items() if key != isbn }
            print(f'Book with ISBN: {isbn} has been deleted to the library.')
        else:
            print(f'Book with ISBN: {isbn} does not exist in the library.')

    
    def get_book(self, isbn:str) -> dict:
        """
        Retrieve and display the details of a book using its ISBN

        Args:
            isbn (str): Book ISBN number
        
        Returns:
            None
        """
        if isbn in self.library:
            for k, v in self.library[isbn].items():
                print(f'{k}: {v}')
        else:
            print(f'Book with ISBN: {isbn} does not exist in the library.')


    def search_for_book(self, title:str='', author:str='') -> dict:
        """
        Search for books by title or author

        Args:
            title (str): Book title
            author (str): Book author
        
        Returns:
            dict: dictionary of all books matching the search.
        """
        if title:
            return { key: val for key, val in self.library.items() if title.lower() in val['title'].lower() }
        elif author:
            return { key: val for key, val in self.library.items() if author.lower() in val['author'].lower() }
        else:
            print(f'No book was found for the search: {title or author}')

    def get_all_books(self) -> None:
        """
        List all books currently in the library.

        Args:
            No arguments
        
        Returns:
            None
        """
        for isbn, book_details in self.library.items():
            print(f'ISBN: {isbn}')
            for book_attribute, value in book_details.items():
                print(f'--> {book_attribute}: {value}')
            print()

    def update_book(self, isbn:str, **kwargs) -> None:
        """
        Update the details of an existing book

        Args:
            isbn (str): Book ISBN number
            **kwargs: Arbitrary number of keyword arguments e.g. title, author, publisher

        Returns:
            dict: dictionary of all books matching the search.
        """
        if isbn in self.library:
            book = self.library[isbn]
            for key, value in kwargs.items():
                if key in book:
                    book[key] = value
            print(f'Book with ISBN {isbn} has been updated.')
        else:
            print(f'Book with ISBN {isbn} does not exist.')

    def book_available(self, isbn:str) -> bool:
        """
        Check if a book is available in the library by its ISBN

        Args:
            isbn (str): Book ISBN number
            
        Returns:
            bool: Return true if book is in library.
        """
        if isbn in self.library:
            print(f'Book with ISBN {isbn} is available.')
        else:
            print(f'Book with ISBN {isbn} is not available.')
