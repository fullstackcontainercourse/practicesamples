import unittest
from mongosetup import *


'''
Description : Complete the below method using MongoDB methods to insert a 'Books' document into
'Library' Database.

Points to note :
Try to use collections.insert_many([dictionaries]) method
The document is available only after it is inserted in the DB


'''


def createBookDocuments():

    # connect to 'Library' data base in MongoDB

    # connect to 'Books' collection

    # user insert_many() method to create the document in MongoDB

    inserted_doc_id = << Insert_Many call >>

    return inserted_doc_id


class TestLab11(unittest.TestCase):
    def test_LibraryBooksCollection(self):
        # call create Book document
        createBookDocuments()
        # Test the created record
        books_data = getCollectionsFromLibraryDB(
            "Books").find()
        print(books_data)

        self.assertIsNotNone(
            books_data, "No Books data found. It is suppose to be found.")
        self.assertTrue(len(list((books_data))) >= 5,
                        "Insert Many records failed")


if __name__ == '__main__':
    unittest.main()
