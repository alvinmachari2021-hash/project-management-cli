from rich.console import Console

console = Console()

def pretty_print(message):
    console.print(message, style="bold green")