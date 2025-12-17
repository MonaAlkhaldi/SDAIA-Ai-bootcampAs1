def md_table_header() -> list[str]:
    return[
        "#Table",
        "|c1|ty|mis|un",
        "|---|--:|---:|"
    ]

print("\n".join(md_table_header())) 

#When we want to add a new row in the table we caan build a function that will take all the information of columns \

def New_row(Name:str , typ: str , missing: int, missing_pct: float, unique: int)->str: #this means that the output will be returned as str
      return f"|'{Name}'|'{typ}'|'{missing}'|'{missing_pct}'|'{unique}'"
 