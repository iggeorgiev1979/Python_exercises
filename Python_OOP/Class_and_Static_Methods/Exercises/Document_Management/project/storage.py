from Class_and_Static_Methods.Exercises.Document_Management.project.category import Category
from Class_and_Static_Methods.Exercises.Document_Management.project.document import Document
from Class_and_Static_Methods.Exercises.Document_Management.project.topic import Topic
# from project.category import Category
# from project.document import Document
# from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        tmp = [topic for topic in self.topics if topic.id == topic_id]
        if tmp:
            topic, = tmp
        else:
            topic = None

        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        tmp = [document for document in self.documents if document.id == document_id]
        if tmp:
            document, = tmp
        else:
            document = None

        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)
                break

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)
                break

    def delete_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)
                break

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return "\n".join([f'{document}' for document in self.documents])


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
