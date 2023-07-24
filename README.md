### Testing REST API with Pytest 
https://www.youtube.com/watch?v=7dgQRVqF1N0 
preparation 
```bash
$ virtualenv venv
$ source venv/bin/activate 

$ pip install pytest 
$ pip install requests 
``` 
Test URL
https://todo.pixegami.io 

https://todo.pixegami.io/docs 


Run tests
```bash
$ pytest 
$ pytest -v
```

To let print something withng testing
```bash
$ pytest -v -s
```