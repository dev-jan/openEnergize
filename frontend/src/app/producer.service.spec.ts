import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { ProducerService } from './producer.service';
import { Producer } from './models/Producer';

describe('ProducerService', () => {
  let service: ProducerService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ ProducerService ]
    });
    service = TestBed.inject(ProducerService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('shoud be able to retrieve producers', () => {
    const dummyProducers: Producer[] = [
      {
        id: 1,
        name: 'Test producer 1',
        type: 'constant',
        currentProductionInWatt: 20000
      },
      {
        id: 2,
        name: 'Test producer 2',
        type: 'constant',
        currentProductionInWatt: 30000.222
      }
    ];

    service.getAllProducers().subscribe(producers => {
      expect(producers.length).toBe(2);
      expect(producers).toEqual(dummyProducers);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/producers/');
    expect(req.request.method).toEqual('GET');
    req.flush(dummyProducers);
  });
});
