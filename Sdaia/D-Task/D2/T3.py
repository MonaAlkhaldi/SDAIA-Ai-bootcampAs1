#Create a function that returns a markdown header block: 

from datetime import datetime

def md_header(source: str) -> list[str]:
    ts = datetime.now().isoformat(timespec="seconds")
    #the source will be givn , and we need to add the vtime to a varible so we can print them using markdown 

    return[
        "# Markdown",
        "", 
        f"-**source** '{source}'" ,
        f"-**ts** '{ts}'" ,
        "",
    ]
