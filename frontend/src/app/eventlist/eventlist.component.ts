import { Component, OnInit } from '@angular/core';
import { EventService } from '../event.service';
import { Event } from '../models/Event';

@Component({
  selector: 'app-eventlist',
  templateUrl: './eventlist.component.html',
  styleUrls: ['./eventlist.component.scss']
})
export class EventlistComponent implements OnInit {

  constructor(private eventService: EventService) { }

  events: Event[] = [];
  eventColumns: string[] = ['timestamp', 'level', 'name', 'text'];

  ngOnInit(): void {
    this.reloadEvents();
  }

  reloadEvents(): void {
    this.eventService.getAllEvents()
        .subscribe(events => this.events = events);
  }
}
