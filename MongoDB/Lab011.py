import unittest
from mongosetup import *


'''
Description : Complete the below method using MongoDB methods to insert a 'Book' document into
'Library' Database.

'''


def createBookDocument():

    # connect to 'Library' data base in MongoDB

    # connect to 'Books' collection

    # user insertOne() method to create the document in MongoDB

    return


class TestLab11(unittest.TestCase):
    def test_LibraryBooksCollection(self):
        # call create Book document
        createBookDocument()
        # Test the created record
        book_data = getCollectionsFromLibraryDB("Books").find_one()
        print(book_data)
        self.assertIsNotNone(
            book_data, "No Books data found. It is suppose to be found.")


if __name__ == '__main__':
    unittest.main()
