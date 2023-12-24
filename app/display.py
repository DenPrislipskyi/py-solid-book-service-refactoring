from app.book import Book
from abc import ABC, abstractmethod


class Displayer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplayer(Displayer):
    def display(self) -> None:
        print(self.book.content)


class ReverseDisplayer(Displayer):
    def display(self) -> None:
        print(self.book.content[::-1])
