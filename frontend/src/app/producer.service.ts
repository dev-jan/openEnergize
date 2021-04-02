import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../environments/environment';
import { Observable } from 'rxjs';
import { Producer } from './models/Producer';

@Injectable({
  providedIn: 'root'
})
export class ProducerService {

  producerUrl = '/producers/';

  getAllProducers(): Observable<Producer[]> {
    return this.http.get<Producer[]>(environment.apiUrl + this.producerUrl);
  }

  constructor(private http: HttpClient) { }
}
