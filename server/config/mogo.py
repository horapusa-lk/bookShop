class Mongo:

    def connect(self):
        """
        :return: books object.
        """
        import pymongo
        myclient = pymongo.MongoClient(
            "mongodb+srv://horapusa:OY5NDCbVwSTvOO4y@horapusa.ouly8ln.mongodb.net/?retryWrites=true&w=majority")
        mydb = myclient["bookStore"]
        mycol = mydb["books"]
        return mycol


