import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { ConfigurationService } from './configuration.service';
import { Configuration } from './models/Configuration';

describe('ConfigurationService', () => {
  let service: ConfigurationService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ ConfigurationService ]
    });
    service = TestBed.inject(ConfigurationService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should be able to retrieve configuration info', () => {
    const dummyConfig: Configuration = {
      raw: 'some appconfig: true\n anotherconfig: false\n'
    };

    service.getFullConfiguration().subscribe(config => {
      expect(config).toEqual(dummyConfig);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/configuration');
    expect(req.request.method).toEqual('GET');
    req.flush(dummyConfig);
  });
});
