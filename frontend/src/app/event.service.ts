import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Event } from './models/Event';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  eventsUrl = '/events';

  getAllEvents(): Observable<Event[]> {
    return this.http.get<Event[]>(environment.apiUrl + this.eventsUrl);
  }

  constructor(private http: HttpClient) { }
}
