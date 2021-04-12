import { Component, Input, OnInit } from '@angular/core';
import { Storage } from '../models/Storage';

@Component({
  selector: 'app-storage-detail',
  templateUrl: './storage-detail.component.html',
  styleUrls: ['./storage-detail.component.scss']
})
export class StorageDetailComponent implements OnInit {

  @Input() storage?: Storage;

  constructor() { }

  ngOnInit(): void {
  }

}
