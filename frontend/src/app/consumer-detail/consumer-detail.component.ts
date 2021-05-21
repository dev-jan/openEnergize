import { Component, Input, OnInit } from '@angular/core';
import { Consumer } from '../models/Consumer';

@Component({
  selector: 'app-consumer-detail',
  templateUrl: './consumer-detail.component.html',
  styleUrls: ['./consumer-detail.component.scss']
})
export class ConsumerDetailComponent implements OnInit {
  fallbackImageUrl: string = 'https://images.unsplash.com/photo-1610056494052-6a4f83a8368c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&h=200&q=80';
  @Input() consumer?: Consumer;

  constructor() {
    // intentionally empty
  }

  ngOnInit(): void {
    // intentionally empty
  }

}
