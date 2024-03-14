from .repository import Repository

class TopicRepository(Repository):
    def __init__(self):
        self.topics = {}

    def add(self, topic):
        self.topics[topic.id] = topic

    def get(self, topic_id):
        return self.topics.get(topic_id)

    def update(self, topic):
        if topic.id in self.topics:
            self.topics[topic.id] = topic
        else:
            print(f"Ошибка: Задание с id {topic.id} не существует")

    def remove(self, topic):
        if topic.id in self.topics:
            del self.topics[topic.id]
        else:
            print(f"Ошибка: Задание с id {topic.id} не существует")

    def get_all(self):
        return list(self.topics.values())