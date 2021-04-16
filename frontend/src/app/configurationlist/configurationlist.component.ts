import { Component, OnInit } from '@angular/core';
import { ConfigurationService } from '../configuration.service';
import { Configuration } from '../models/Configuration';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-configurationlist',
  templateUrl: './configurationlist.component.html',
  styleUrls: ['./configurationlist.component.scss']
})
export class ConfigurationlistComponent implements OnInit {

  configuration?: Configuration;
  environmentConfig = environment;

  constructor(private configurationService: ConfigurationService) { }

  ngOnInit(): void {
    this.configurationService.getFullConfiguration()
        .subscribe(data => this.configuration = data);
  }

}
