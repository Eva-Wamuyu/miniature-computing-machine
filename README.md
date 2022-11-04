## About

This is a post request in python  

## Instructions
### Data
Using an API testing tool,make a POST request with the body having json data in the following format:
```
{
    "operation_type": "" an Enum can be multiplication, substraction or addition,
    "x": number  a number/int, 
    "y": number a number/int
    
}
```
### Response
```
{
    "slackUsername": "Wamuyu",
    "result": number calculated from the operands and operator passed,
    "operation_type": "+"
}
Status: 200

```
### Points
All inputs are required i.operation_type, x and y

### Using the repository
```
git clone https://github.com/Eva-Wamuyu/miniature-computing-machine.git  
cd miniature-computing-machine
python3 -m venv venv
pip install -r requirements.txt
python3 app.py
```
Make POST request http://127.0.0.1:{PORT}/app where {PORT} can be 5000 or any other port number



