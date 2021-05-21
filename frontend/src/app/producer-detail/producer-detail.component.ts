import { Component, Input, OnInit } from '@angular/core';
import { Producer } from '../models/Producer';

@Component({
  selector: 'app-producer-detail',
  templateUrl: './producer-detail.component.html',
  styleUrls: ['./producer-detail.component.scss']
})
export class ProducerDetailComponent implements OnInit {
  fallbackImageUrl:string = 'https://images.unsplash.com/photo-1521618755572-156ae0cdd74d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&h=200&q=80';
  @Input() producer?: Producer;

  constructor() {
    // intentionally empty
  }

  ngOnInit(): void {
    // intentionally empty
  }

}
