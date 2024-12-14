### Windows

Create virtual environment  
```commandline
python -m venv env-python-pgd
```

Activate virtual environment  
```commandline
.\env-python-pgd\Scripts\activate
```

Install dependencies  
```commandline
pip install -r .\requirements.txt
```

Run test  
```commandline
pytest .\src\operators\logical.py
```