# Encrypt Api 

An api endpoint to encrypt messages using the FastApi Platform in Python.

## Installation

Clone the git repo
```bash
git clone https://github.com/ilulale/encryptapi.git
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fastApi and uvicorn.

```bash
pip install fastapi
pip install uvicorn
```

## Usage
Run the tset.py file in uvicorn
```bash
uvicorn tset:app --reload 
```
## ChangeLog
Created a encryption endpoint at 

[http://127.0.0.1:8000/encrypt/{sender_key}/{msg}/{reciever_key}](http://127.0.0.1:8000/encrypt/6/Test/9)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
