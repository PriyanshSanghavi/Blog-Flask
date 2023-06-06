
# Blog-Flask

I created a blogging platform using Flask that allows users to write, read, update, and remove blog articles. I handled these processes effectively by designing routes and functions. SQLAlchemy integration allows me to store and retrieve post data.
 I can quickly create a fully working blog website with rich CRUD features by using Flask's versatility and simplicity of use.
## Installation

For install, open the Blog-Flask folder in Visual Studio Code, then create a new terminal and enter the below code. 

Use the package manager pip to install virtualenv

```bash
  pip install virtualenv
```
After installing virtualenv, run it using below command:

```bash
    virtualenv env
```
```bash
    Set-ExecutionPolicy unrestricted
```
If error occurs while running this command, run below command in PowerShell:
```bash
    Set-ExecutionPolicy unrestricted
```
After that, run the command below to activate a virtual environment:

```bash
    .\env\Scripts\Activate.ps1
```
Install Flask and sqlalchemy in a virtual environment by running the following command:
```bash
    pip install flask
    pip install flask-sqlalchemy
```

Install the ``` jinja2 snippet kit ``` plugin in Visual Studio code.
## Run
Run this command in the terminal:
```bash
    .\env\Scripts\Activate.ps1
    Python app.py
```
After that, click the link below:
```bash
    http://127.0.0.1:8000/
```
## Output
![1](https://github.com/PriyanshSanghavi/Blog-Flask/assets/64824381/4e8d437d-c8df-41ca-acc4-7aff1a0b28de)
![2](https://github.com/PriyanshSanghavi/Blog-Flask/assets/64824381/16fe7681-9ff4-4cb2-84d1-2134461ab9b0)
![4](https://github.com/PriyanshSanghavi/Blog-Flask/assets/64824381/bf593a38-0e03-409f-8bb7-c2810362a93f)
![3](https://github.com/PriyanshSanghavi/Blog-Flask/assets/64824381/cd7f1dd5-75c3-4e8e-bc32-f16c197407a0)
