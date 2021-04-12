import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Storage } from './models/Storage';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class StorageService {

  storageUrl = '/storages';

  storages: Storage[] = [];

  getAllStorages(): Observable<Storage[]> {
    return this.http.get<Storage[]>(environment.apiUrl + this.storageUrl);
  }

  constructor(private http:HttpClient) { }
}
