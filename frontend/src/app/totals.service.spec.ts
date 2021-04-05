import { TestBed } from '@angular/core/testing';

import { TotalsService } from './totals.service';

describe('TotalsService', () => {
  let service: TotalsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TotalsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
