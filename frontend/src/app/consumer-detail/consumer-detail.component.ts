import { Component, Input, OnInit } from '@angular/core';
import { Consumer } from '../models/Consumer';

@Component({
  selector: 'app-consumer-detail',
  templateUrl: './consumer-detail.component.html',
  styleUrls: ['./consumer-detail.component.scss']
})
export class ConsumerDetailComponent implements OnInit {

  @Input() consumer?: Consumer;

  constructor() {
    // intentionally empty
  }

  ngOnInit(): void {
    // intentionally empty
  }

}
