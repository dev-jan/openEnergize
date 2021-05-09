import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { Storage } from './models/Storage';
import { StorageService } from './storage.service';

describe('StorageService', () => {
  let service: StorageService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ StorageService ]
    });
    service = TestBed.inject(StorageService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should be able to retrieve storage information', () => {
    const dummyStorageInfos: Storage[] = [
      {
        id: 1,
        name: 'Test 1',
        type: 'constant',
        currentStorageCapacityInPercent: 91
      },
      {
        id: 2,
        name: 'Test 2',
        type: 'constant',
        currentStorageCapacityInPercent: 100
      }
    ];

    service.getAllStorages().subscribe(storages => {
      expect(storages.length).toBe(2);
      expect(storages).toEqual(dummyStorageInfos);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/storages');
    expect(req.request.method).toEqual('GET');
    req.flush(dummyStorageInfos);
  });
});
