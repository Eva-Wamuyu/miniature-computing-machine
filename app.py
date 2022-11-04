from flask import Flask,request
import json
from enum import Enum

app = Flask(__name__)


@app.route('/app',methods=['POST'])
def handler():
    if request.data:
        data = request.get_json()
        print(data)

        return calculate(data)
    return app.response_class(
        status=400,
    )


def calculate(data):
    try:
        x = data['x']
        y = data['y']
        operation_type = data['operation_type']
        operator = Operation[operation_type].value
        op = Operation[operation_type]
        print(type(op))
        if operator is "*":
            result = x * y
        elif operator is "+":
            result = x + y
        else:
            result = x - y
        response_data = json.dumps(
        {"slackUsername": "Wamuyu",
        "result": result,
        "operation_type": op
        }
    )
    except KeyError:
        return app.response_class(
            status=400,
            response={
                "operation_type[multiplication or addition or subtraction], x and y are required"
            }
        )
    else:
        response = app.response_class(
        response = response_data,
        status = 200,
        mimetype='application/json'
        )
        return response

    
class Operation(str,Enum):
    multiplication = '*',
    addition = '+'
    subtraction = '-'

if __name__=='__main__':
    app.run()