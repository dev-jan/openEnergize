import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Consumer } from './models/Consumer';
import { environment } from './../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ConsumerService {

  private consumerUrl = '/consumers/';

  getAllConsumers(): Observable<Consumer[]> {
    return this.http.get<Consumer[]>(environment.apiUrl + this.consumerUrl);
  }

  constructor(private http: HttpClient) { }
}
