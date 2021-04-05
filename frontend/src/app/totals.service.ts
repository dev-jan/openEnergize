import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Totals } from './models/Totals';

@Injectable({
  providedIn: 'root'
})
export class TotalsService {

  totalsUrl = '/totals/';

  getTotals(): Observable<Totals> {
    return this.http.get<Totals>(environment.apiUrl + this.totalsUrl);
  }

  constructor(private http:HttpClient) { }
}
