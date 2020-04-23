import sumTwoNumbers
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

# class docker_poc_call(Resource):
#     def get(self,image_name):
        
#         return docker_poc.runAContainer(image_name) 

 
class sumNumbers(Resource):
    def get(self, first_number, second_number):
        return {'data': sumTwoNumbers.sumTwoNumberss(first_number,second_number)}
api.add_resource(sumNumbers, '/sumtwonumbers/<first_number>/<second_number>')

#api.add_resource(docker_poc_call, '/docker_poc/<image_name>')

if __name__ == '__main__':
     app.run()