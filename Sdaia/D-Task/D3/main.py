import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    
    print(f"Hello {name}")

app = typer.Typer()





if __name__ == "__main__":
    app() 
    
    

    