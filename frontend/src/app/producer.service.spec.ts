import { TestBed } from '@angular/core/testing';

import { ProducerService } from './producer.service';

describe('ProducerService', () => {
  let service: ProducerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProducerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
