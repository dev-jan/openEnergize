import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent implements OnInit {

  @Output() sidenavClose = new EventEmitter();

  constructor() {
    // intentionally empty
  }

  ngOnInit(): void {
    // intentionally empty
  }

  public onSidenavClose = () => {
    this.sidenavClose.emit();
  }

}
