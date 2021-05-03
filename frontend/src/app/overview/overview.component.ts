import { Component, OnInit } from '@angular/core';
import { ProducerService } from '../producer.service';
import { ConsumerService } from '../consumer.service';
import { StorageService } from '../storage.service';
import { TotalsService } from '../totals.service';
import { Producer } from '../models/Producer';
import { Consumer } from '../models/Consumer';
import { Storage } from '../models/Storage';
import { Totals } from '../models/Totals';
import { PartialObserver } from 'rxjs';

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.scss']
})
export class OverviewComponent implements OnInit {

  constructor(private producerService: ProducerService,
              private consumerService: ConsumerService,
              private storageService: StorageService,
              private totalsService: TotalsService) { }

  producers: Producer[] = [];
  consumers: Consumer[] = [];
  storages: Storage[] = [];
  totals?: Totals;
  totalRequestError?: string;

  ngOnInit(): void {
    this.producerService.getAllProducers()
        .subscribe({
          next: producers => this.producers = producers,
          error: error => console.log('Error while getting producers!' + error.message)
        } as PartialObserver<Producer[]>);

    this.consumerService.getAllConsumers()
        .subscribe({
          next: consumers => this.consumers = consumers,
          error: error => console.log('Error while getting consumers!' + error.message)
        } as PartialObserver<Consumer[]>);

    this.storageService.getAllStorages()
        .subscribe({
          next: storages => this.storages = storages,
          error: error => console.log('Error while getting storages!' + error.message)
        } as PartialObserver<Storage[]>);

    this.totalsService.getTotals()
        .subscribe({
          next: totals => this.totals = totals,
          error: error => this.totalRequestError = error.message
        } as PartialObserver<Totals>);
  }

}
