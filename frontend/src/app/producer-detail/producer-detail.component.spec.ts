import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProducerDetailComponent } from './producer-detail.component';

describe('ProducerDetailComponent', () => {
  let component: ProducerDetailComponent;
  let fixture: ComponentFixture<ProducerDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProducerDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProducerDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
