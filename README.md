Windows

Create virtual environment  
python -m venv env-python-pgd

Activate virtual environment  
.\env-python-pgd\Scripts\activate

Install dependencies  
pip install -r .\requirements.txt

Run test  
pytest .\src\operators\logical.py