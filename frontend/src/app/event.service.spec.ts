import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { EventService } from './event.service';
import { Event } from './models/Event';

describe('EventService', () => {
  let service: EventService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ EventService ]
    });
    service = TestBed.inject(EventService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should be able to retrieve events', () => {
    const dummyEvents: Event[] = [
      {
        level: 'debug',
        name: 'app.py',
        text: 'Some debug message',
        timestamp: '2021-05-09 16:23:19,255'
      },
      {
        level: 'info',
        name: 'backend.ConsumerTrigger',
        text: 'Production capacity (816.33) is greater than the threshold',
        timestamp: '2021-05-09 16:22:58,687'
      }
    ];

    service.getAllEvents().subscribe(events => {
      expect(events.length).toBe(2);
      expect(events).toEqual(dummyEvents);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/events');
    expect(req.request.method).toEqual('GET');
    req.flush(dummyEvents);
  });
});
