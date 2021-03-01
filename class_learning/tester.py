from flask_restful import Resource, Api, reqparse

parser = reqparse.RequestParser()

parser.add_argument('rate', type=int, help='Rate cannot be converted')
parser.add_argument('name', required=True, help='Name cannot be blank')
args = parser.parse_args()

print(args.rate(args.name))