import { Component, OnInit } from '@angular/core';
import { ProducerService } from '../producer.service';
import { ConsumerService } from '../consumer.service';
import { StorageService } from '../storage.service';
import { TotalsService } from '../totals.service';
import { Producer } from '../models/Producer';
import { Consumer } from '../models/Consumer';
import { Storage } from '../models/Storage';
import { Totals } from '../models/Totals';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss']
})
export class OverviewComponent implements OnInit {

  constructor(private producerService:ProducerService,
              private consumerService:ConsumerService,
              private storageService:StorageService,
              private totalsService:TotalsService) { }

  producers: Producer[] = [];
  consumers: Consumer[] = [];
  storages: Storage[] = [];
  totals?: Totals;

  ngOnInit(): void {
    this.producerService.getAllProducers()
        .subscribe(producers => this.producers = producers);

    this.consumerService.getAllConsumers()
        .subscribe(consumers => this.consumers = consumers);

    this.storageService.getAllStorages()
        .subscribe(storages => this.storages = storages);

    this.totalsService.getTotals()
        .subscribe(totals => this.totals = totals);
  }

}
