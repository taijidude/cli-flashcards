from rich.console import Console
from rich.markdown import Markdown

def main():
    console = Console()
    with open("angular.md", encoding="UTF-8") as data:
        content: str = data.read()
        cards: list[str] = content.split('<!-- Card -->')
        numberOfCards: int = len(cards)
        for card in cards:
            console.clear()
            sides = card.split('<!-- Sides -->')
            console.print(Markdown(sides[0])) 
            input("\nshow the answer!")
            console.print(Markdown(sides[1]))
            input("\nnext card!")
            console.clear()
if __name__ == "__main__":
    main()