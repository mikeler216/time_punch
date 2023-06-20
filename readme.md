##
Install 
-------
## poetry
1. Install poetry 
```bash 
brew install poetry
```
2. Install dependencies
```bash
poetry install
```
3. install playwright
```bash
poetry run playwright install
```
## pip
1. Create virtual environment
```bash
python3 -m venv venv
```
2. Activate virtual environment
```bash
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. install playwright
```bash
python -m playwright install
```
-----
## Runing App
1. Set variables in main.py
```python
main(company_number="", employee_id="", password="")
```
2. Run
```bash
python main.py
```



