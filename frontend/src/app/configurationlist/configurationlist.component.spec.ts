import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfigurationlistComponent } from './configurationlist.component';

describe('ConfigurationlistComponent', () => {
  let component: ConfigurationlistComponent;
  let fixture: ComponentFixture<ConfigurationlistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConfigurationlistComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfigurationlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
