import { Component, OnInit } from '@angular/core';
import { ProducerService } from '../producer.service';
import { Producer } from '../models/Producer';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss']
})
export class OverviewComponent implements OnInit {

  constructor(private producerService:ProducerService) { }

  producers: Producer[] = [];

  ngOnInit(): void {
    this.producerService.getAllProducers()
        .subscribe(producers => this.producers = producers);
  }

}
