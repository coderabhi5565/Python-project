from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def display_results(prompt, llama_response, mixtral_response, gemma_response):
    console.print(Panel(prompt, title="Your Prompt"))
    
    table = Table()
    
    table.add_column("Llama", style="cyan")
    table.add_column("Mixtral", style="green")
    table.add_column("Gemma", style="magenta")
    
    table.add_row(llama_response, mixtral_response, gemma_response)
    
    console.print(table)