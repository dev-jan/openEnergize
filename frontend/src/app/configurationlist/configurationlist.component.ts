import { Component, OnInit } from '@angular/core';
import { ConfigurationService } from '../configuration.service';
import { Configuration } from '../models/Configuration';
import { environment } from '../../environments/environment';
import { PartialObserver } from 'rxjs';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-configurationlist',
  templateUrl: './configurationlist.component.html',
  styleUrls: ['./configurationlist.component.scss']
})
export class ConfigurationlistComponent implements OnInit {

  configuration?: Configuration;
  environmentConfig = environment;
  errorMessage?: string;

  constructor(private configurationService: ConfigurationService,
              public translate: TranslateService) { }

  ngOnInit(): void {
    this.configurationService.getFullConfiguration()
        .subscribe({
          next: data => this.configuration = data,
          error: error => this.errorMessage = error.message
        } as PartialObserver<Configuration>);

    this.translate.addLangs(environment.availableLanguages);
  }

  switchLanguage(language: string): void {
    localStorage.setItem('lang', language);
    this.translate.use(language);
  }

}
