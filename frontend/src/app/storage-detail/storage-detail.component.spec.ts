import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StorageDetailComponent } from './storage-detail.component';

describe('StorageDetailComponent', () => {
  let component: StorageDetailComponent;
  let fixture: ComponentFixture<StorageDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StorageDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StorageDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
