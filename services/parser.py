import csv
import io

def parse_csv(file) -> list:
    data = []
    content = file.read().decode("utf-8")
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        data.append({
            "name": row.get("название", ""),
            "price": row.get("цена", ""),
            "description": row.get("описание", "")
        })
    return data
