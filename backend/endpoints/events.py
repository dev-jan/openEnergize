from flask_restx import Namespace, Resource, fields

api = Namespace('events', description='Events')

event = api.model('Event', {
    'timestamp': fields.String(
        required=True,
        description='Timestamp of the event'
    ),
    'level': fields.String(
        required=True,
        description='Loglevel. Possible values: \
        (DEBUG, INFO, WARNING, ERROR, CRITICAL, NONE)'
    ),
    'name': fields.String(
        required=True,
        description='Module name of the event'
    ),
    'text': fields.String(
        required=True,
        description='The text of the event'
    )
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
                fields = line.split(' ')
                if len(fields) > 5 and fields[3] != 'werkzeug':
                    singleEvent = {}
                    singleEvent['timestamp'] = fields[0] + " " + fields[1]
                    singleEvent['level'] = fields[2]
                    singleEvent['name'] = fields[3]
                    singleEvent['text'] = ' '.join(fields[4:])
                    events.append(singleEvent)
        events.reverse()
        return events
