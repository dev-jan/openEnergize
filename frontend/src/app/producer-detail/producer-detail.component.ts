import { Component, Input, OnInit } from '@angular/core';
import { Producer } from '../models/Producer';

@Component({
  selector: 'app-producer-detail',
  templateUrl: './producer-detail.component.html',
  styleUrls: ['./producer-detail.component.scss']
})
export class ProducerDetailComponent implements OnInit {

  @Input() producer?: Producer;

  constructor() {
    // intentionally empty
  }

  ngOnInit(): void {
    // intentionally empty
  }

}
