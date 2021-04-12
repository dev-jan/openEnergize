from flask_restx import Namespace, Api, Resource, fields

api = Namespace('events', description='Events')

event = api.model('Event', {
    'text': fields.String(required=True, description='The text of the event')
})

@api.route('/')
class EventList(Resource):
    @api.doc('list_events')
    @api.marshal_list_with(event)
    def get(self):
        events = []
        with open('./app.log') as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip('\n')
                events.append({'text': line})
        events.reverse()
        return events
