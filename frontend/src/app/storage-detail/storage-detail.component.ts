import { Component, Input, OnInit } from '@angular/core';
import { Storage } from '../models/Storage';

@Component({
  selector: 'app-storage-detail',
  templateUrl: './storage-detail.component.html',
  styleUrls: ['./storage-detail.component.scss']
})
export class StorageDetailComponent implements OnInit {
  fallbackImageUrl: string = 'https://images.unsplash.com/photo-1591964006776-90b32e88f5ec?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&h=200&q=80';
  @Input() storage?: Storage;

  constructor() {
    // intentionally empty
  }

  ngOnInit(): void {
    // intentionally empty
  }

}
