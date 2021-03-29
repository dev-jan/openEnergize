from flask_restx import Namespace, Api, Resource, fields

ns = Namespace('producers', description='Energy producers')

producer = ns.model('Producer', {
    'id': fields.String(required=True, description='ID of the producer'),
    'name': fields.String(required=True, description='Name of the producer')
})

class Producer(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

@ns.route('/')
class ProducerList(Resource):
    @ns.doc('list_producers')
    @ns.marshal_list_with(producer)
    def get(self):
        producers = []
        producers.append(Producer(0, "Testproducer"))
        producers.append(Producer(1, "Second producer"))
        return producers
