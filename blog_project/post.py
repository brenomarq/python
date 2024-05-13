class Post:
    def __init__(self, post_data: dict) -> None:
        self.id: int = int(post_data['id'])
        self.title: str = post_data['title']
        self.subtitle: str = post_data['subtitle']
        self.body: str = post_data['body']
        self.author: str = post_data['author']
        self.date: str = post_data['date']
