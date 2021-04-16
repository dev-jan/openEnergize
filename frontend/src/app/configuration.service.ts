import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Configuration } from './models/Configuration';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ConfigurationService {

  configurationUrl = '/configuration';

  constructor(private http: HttpClient) { }

  getFullConfiguration(): Observable<Configuration> {
    return this.http.get<Configuration>(environment.apiUrl + this.configurationUrl);
  }
}
