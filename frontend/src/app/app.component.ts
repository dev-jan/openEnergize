import { Component } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';

  constructor(private translate: TranslateService) { }

  ngOnInit(): void {
    var lang = localStorage.getItem('lang');
    if (lang === null) {
      lang = this.translate.getBrowserLang();
    }
    this.translate.use(lang);
  }
}
