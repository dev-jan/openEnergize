import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { ConsumerService } from './consumer.service';
import { Consumer } from './models/Consumer';

describe('ConsumerService', () => {
  let service: ConsumerService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ ConsumerService ]
    });
    service = TestBed.inject(ConsumerService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should be able to retrieve consumer infos', () => {
    const dummyConsumers: Consumer[] = [
      {
        id: 1,
        name: 'Test 1',
        type: 'constant',
        isControllable: false,
        status: 'UNKNOWN',
        currentConsumptionInWatt: 1000.33
      },
      {
        id: 2,
        name: 'Test 2',
        type: 'constant',
        isControllable: true,
        status: 'READY',
        currentConsumptionInWatt: 10
      },
    ];

    service.getAllConsumers().subscribe(consumers => {
      expect(consumers.length).toBe(2);
      expect(consumers).toEqual(dummyConsumers);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/consumers/');
    expect(req.request.method).toEqual('GET');
    req.flush(dummyConsumers);
  });
});
