# TODO API

- /todo (POST) create todo
- /todo (GET) get All todo
- /todo/<id> (GET) get todo by ID
- /todo/<id> (PUT/PATCH) update todo
- /todo/<id>/finish finish todo
- /todo/<id> (DELETE) soft delete todo

# How to run
first, make sure the library & package is all installed `pip install -r requirements.txt`
### Run the API server

```ps
cd fastapi && fastapi dev
```

### Run the Demo web

```ps
python -m flask --app main run -p 9000 --debug
```

# Demo

![2024-11-30 17-46-23](https://github.com/user-attachments/assets/f0f26405-06ea-427f-b6d6-03d4164d9e41)

# Todo Model
```py
id: int
title: str = "untitled"
description: str = "......." 
finished_at: Optional[str] = None
created_at: Optional[str] = None
updated_at: Optional[str] = None
deleted_at: Optional[str] = None
```

- id : is unique, the index is based on its array length +1
- title & desc : have default value when object created
- *_at : is optional to include in a request and have null default