import { Component, OnInit } from '@angular/core';
import { ProducerService } from '../producer.service';
import { Producer } from '../models/Producer';
import { Consumer } from '../models/Consumer';
import { ConsumerService } from '../consumer.service';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss']
})
export class OverviewComponent implements OnInit {

  constructor(private producerService:ProducerService,
              private consumerService:ConsumerService) { }

  producers: Producer[] = [];
  consumers: Consumer[] = [];

  ngOnInit(): void {
    this.producerService.getAllProducers()
        .subscribe(producers => this.producers = producers);

    this.consumerService.getAllConsumers()
        .subscribe(consumers => this.consumers = consumers);
  }

}
