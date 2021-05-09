import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TotalsService } from './totals.service';
import { Totals } from './models/Totals';

describe('TotalsService', () => {
  let service: TotalsService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ TotalsService ]
    });
    service = TestBed.inject(TotalsService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should be able to receive totals info', () => {
    const dummyTotals: Totals = {
      energySum: 100.2,
      totalEnergyConsumption: 200.1,
      totalEnergyProduction: 300.1
    };

    service.getTotals().subscribe(totals => {
      expect(totals).toEqual(dummyTotals);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/totals/');
    expect(req.request.method).toEqual('GET');
    req.flush(dummyTotals);
  });
});
