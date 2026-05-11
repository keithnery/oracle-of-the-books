genre = {
    'fantasy': [
        'Percy Jackson', 'Throne of Glass', 'Caraval',
        'The Cruel Prince', 'Six of Crows', 'The Hobbit',
        'Eragon', 'A Court of Thorns and Roses', 'Crescent City',
        'Twilight', 'Fourth Wing', 'Lord of the Rings', 'Dracula'

    ],

    'mystery': [
        'Sherlock Holmes', 'The Da Vinci Code', 'Gone Girl',
        'Murder on the Orient Express', 'And Then There Were None',
        'A Good Girl’s Guide to Murder'
    ],

    'romance': [
        'Pride and Prejudice', 'Me Before You', 'The Notebook',
        'Better Than the Movies', 'Beach Read', 'It Ends with Us',
        'Twilight', 'The Selection', 'Fourth Wing'
    ],

    'sci-fi': [
        'Dune', 'The Martian', 'Ender’s Game',
        'Ready Player One', 'Foundation', 'Project Hail Mary'
    ],

    'thriller': [
        'The Silent Patient', 'Gone Girl', 'The Girl on the Train',
        'Behind Closed Doors', 'Verity'
    ],

    'dystopia': [
        'The Hunger Games', 'Divergent', '1984',
        'Brave New World', 'Maze Runner', 'Shatter me',
        'Red Queen'
    ],

    'adventure': [
        'Treasure Island', 'The Hobbit', 'Percy Jackson',
        'Around the World in 80 Days', 'Life of Pi',
        'Lord of the Rings'
    ],

    'horror': [
        'Dracula', 'Frankenstein', 'It',
        'The Shining', 'Coraline'
    ]
}

era = {
    'past': [
        'Pride and Prejudice', 'Sherlock Holmes',
        'Dracula', 'Frankenstein',
        'Treasure Island',
        'Around the World in 80 Days',
        'Murder on the Orient Express',
        'And Then There Were None',
        'The Hobbit', 'Fourth Wing', 'Throne of Glass',
        'Lord of the Rings', 'Eragon', 'Caraval'
    ],

    'modern': [
        'Percy Jackson', 'Gone Girl', 'Twilight',
        'The Silent Patient',
        'Better Than the Movies',
        'Beach Read', 'The Notebook',
        'Verity', 'Behind Closed Doors',
        'The Girl on the Train',
        'A Good Girl’s Guide to Murder',
        'Me Before You', 'Coraline',  'Life of Pi'
    ],

    'future': [
        'Dune', 'The Hunger Games',
        'Divergent', 'Ready Player One',
        'Foundation', 'Ender’s Game',
        'Project Hail Mary',
        '1984', 'Brave New World',
        'Maze Runner', 'Shatter me',
        'Red Queen', 'The Selection', 'Crescent City'
    ]
}

detail = {
    'dragons': [
        'Eragon', 'Fourth Wing', 'Throne of Glass', 'The Hobbit'
    ],

    'faeries': [
        'The Cruel Prince', 'Crescent City',
        'Throne of Glass',
        'A Court of Thorns and Roses',
    ],

    'vampires': [
        'Twilight', 'Dracula',
    ],

    'only humans': [
        'Pride and Prejudice', 'Gone Girl',
        'Sherlock Holmes', 'The Da Vinci Code',
        'Verity', 'The Silent Patient',
        'The Girl on the Train', 'Behind Closed Doors',
        'Me Before You', 'Beach Read', 'Life of Pi',
        'The Notebook', 'Red Queen', 'Shatter me', 'Caraval'
    ],

    'royalty': [
        'The Cruel Prince', 'Red Queen',
        'The Selection', 'Throne of Glass', 'A Court of Thorns and Roses'
    ],

    'pirates': [
        'Treasure Island', 'Six of Crows', 'Throne of Glass'
    ],

    'other races': [
        'The Hobbit', 'Lord of the Rings',
        'Eragon', 'It', 'Throne of Glass',
        'A Court of Thorns and Roses', 'Crescent City'
    ],

    'new races': [
        'Dune', 'Foundation',
        'Ender’s Game', 'Project Hail Mary', 'Frankenstein',
        'Coraline', 'Throne of Glass',
        'A Court of Thorns and Roses', 'Crescent City'
    ]
}

print('WELCOME TO THE ORACLE OF BOOKS 📖✨')
print('Choose from the options and discover the perfect fiction book for you!')

print('GENRES: \nFantasy \nMystery \nRomance \nSci-Fi \nThriller \nDystopia \nAdventure \nHorror')
user_genre = input('Choose genre: ').strip().lower()

print('ERAS: \nPast \nModern \nFuture')
user_era = input('Choose era:').strip().lower()

print('DETAILS: \nDragons \nFaeries \nVampires \nOnly humans \nRoyalty \nPirates \nOther races \nNew races')
user_detail = input('Choose one detail that cannot be missing:').strip().lower()

books1 = set(genre[user_genre])
books2 = set(era[user_era])
books3 = set(detail[user_detail])

result = books1 & books2 & books3

print('\nBest books for you:\n ')

if result:
    for book in result:
        print(book)
else:
    print('Books not found')