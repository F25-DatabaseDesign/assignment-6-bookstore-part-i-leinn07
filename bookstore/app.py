from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]
# 4 categories for the bookstore
categories = [
    {"id": 1, "name": "Mystery"},      
    {"id": 2, "name": "Music"},      
    {"id": 3, "name": "Philosophy"},   
    {"id": 4, "name": "Poetry"}     
]

books = [
    # Mystery (categoryId = 1)
    {
        "id": 1,
        "categoryId": 1,
        "title": "Verity",
        "author": "Colleen Hoover",
        "isbn": "9781538724736",
        "price": 14.99,
        "image": "my-1.jpg",
        "readNow": 1
    },
    {
        "id": 2,
        "categoryId": 1,
        "title": "A Good Girl's Guide to Murder",
        "author": "Holly Jackson",
        "isbn": "9781405293181",
        "price": 11.99,
        "image": "my-2.jpg",
        "readNow": 1
    },
    {
        "id": 3,
        "categoryId": 1,
        "title": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "isbn": "9780007119318",
        "price": 10.99,
        "image": "my-3.jpg",
        "readNow": 0
    },
    {
        "id": 4,
        "categoryId": 1,
        "title": "Ruthless People",
        "author": "J.J. McAvoy",
        "isbn": "9781612133195",
        "price": 9.99,
        "image": "my-4.jpg",
        "readNow": 0
    },

    # Music (categoryId = 2)
    {
        "id": 5,
        "categoryId": 2,
        "title": "Jazz Piano Fundamentals.",
        "author": "Jeremy Siskind",
        "isbn": "9781735169538",
        "price": 19.99,
        "image": "music-1.jpg",
        "readNow": 1
    },
    {
        "id": 6,
        "categoryId": 2,
        "title": "Music Composition For Dummies",
        "author": "Scott Jarrett, Holly Day",
        "isbn": "9780470289938",
        "price": 18.99,
        "image": "music-2.jpg",
        "readNow": 0
    },
    {
        "id": 7,
        "categoryId": 2,
        "title": "Music: A Very Short Introduction",
        "author": "Nicholas Cook",
        "isbn": "9780192853820",
        "price": 12.99,
        "image": "music-3.jpg",
        "readNow": 1
    },
    {
        "id": 8,
        "categoryId": 2,
        "title": "Music Composition 1: Learn how to compose well-written rhythms and melodies (Volume 1)",
        "author": "Jonathan E. Peters",
        "isbn": "9781495397325",
        "price": 16.99,
        "image": "music-4.jpg",
        "readNow": 0
    },

    # Philosophy (categoryId = 3)
    {
        "id": 9,
        "categoryId": 3,
        "title": "Ancient Philosophy: A New History of Western Philosophy, Volume 1",
        "author": "Anthony Kenny",
        "isbn": "9780198752721",
        "price": 24.99,
        "image": "phi-1.jpg",
        "readNow": 1
    },
    {
        "id": 10,
        "categoryId": 3,
        "title": "Encyclopedia of Time: Science, Philosophy, Theology, & Culture",
        "author": "H. James Birx",
        "isbn": "97814129416481",
        "price": 39.99,
        "image": "phi-2.jpg",
        "readNow": 0
    },
    {
        "id": 11,
        "categoryId": 3,
        "title": "Language and Mind",
        "author": "Noam Chomsky",
        "isbn": "9780521674935",
        "price": 19.99,
        "image": "phi-3.jpg",
        "readNow": 1
    },
    {
        "id": 12,
        "categoryId": 3,
        "title": "Set Theory and its Philosophy: A Critical Introduction",
        "author": "Michael Potter",
        "isbn": "9780199270415",
        "price": 29.99,
        "image": "phi-4.jpg",
        "readNow": 0
    },

    # Poetry (categoryId = 4)
    {
        "id": 13,
        "categoryId": 4,
        "title": "The Dark Between Stars: Poems",
        "author": "Atticus",
        "isbn": "9781982104863",
        "price": 14.99,
        "image": "poem-1.jpg",
        "readNow": 1
    },
    {
        "id": 14,
        "categoryId": 4,
        "title": "Pillow Thoughts",
        "author": "Courtney Peppernell",
        "isbn": "9781539170389",
        "price": 12.99,
        "image": "poem-2.jpg",
        "readNow": 1
    },
    {
        "id": 15,
        "categoryId": 4,
        "title": "Black Book Of Poems",
        "author": "Vincent Hunanyan",
        "isbn": "9781521345467",
        "price": 11.99,
        "image": "poem-3.jpg",
        "readNow": 0
    },
    {
        "id": 16,
        "categoryId": 4,
        "title": "The Sun and Her Flowers",
        "author": "Rupi Kaur",
        "isbn": "9781449486792",
        "price": 13.99,
        "image": "poem-4.jpg",
        "readNow": 0
    }
]


# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable

    # Create a new list called selected_books containing a list of books that have the selected category

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    category_id = request.args.get('category', type=int)

    selected_books = [
        book for book in books
        if book["categoryId"] == category_id
    ]
    
    return render_template(
        'category.html',
        categories=categories,
        books=selected_books,
        selectedCategory=category_id
    )

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)

