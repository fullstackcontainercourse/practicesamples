import unittest
from mongosetup import *


'''
Description : Complete the below method using MongoDB methods to insert a 'Book' document into
'Library' Database.

Points to note :
Try to use collections.insert(dictionary) method
The document is available only after it is inserted in the DB


'''


def createQueryToReadBooksData(isbnno):
    query = <<TODO >>

    return query


def createBookDocuments():

    # connect to 'Library' data base in MongoDB

    # connect to 'Books' collection

    # user insertOne() method to create the document in MongoDB

    inserted_doc_id = getCollectionsFromLibraryDB("Books").insert_many([
        {"title": "Seven Eleven", "author": "John Peter", "isbn": "67234"},
        {"title": "The Alice in Wonderland",
            "author": "James Wales", "isbn": "134543"},
        {"title": "Seven Stages", "author": "Mike Hary", "isbn": "78564"},
        {"title": "Fairy Tales", "author": "Jim Magats", "isbn": "123"},
        {"title": "The Truth", "author": "Blandina Paul", "isbn": "85234"}])

    return inserted_doc_id


class TestLab14(unittest.TestCase):
    def test_LibraryBooksCollection(self):
        # call create Book document
        createBookDocuments()
        # Test the created record
        books_data = getCollectionsFromLibraryDB(
            "Books").find(createQueryToReadBooksData(78564))

        self.assertIsNotNone(
            books_data, "No Books data found. It is suppose to be found.")
        self.assertTrue(len(list((books_data))) == 1,
                        "Insert Many records failed")


if __name__ == '__main__':
    unittest.main()
