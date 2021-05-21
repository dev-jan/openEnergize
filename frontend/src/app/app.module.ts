import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { OverviewComponent } from './overview/overview.component';
import { HeaderComponent } from './header/header.component';
import { ProducerDetailComponent } from './producer-detail/producer-detail.component';
import { ConsumerDetailComponent } from './consumer-detail/consumer-detail.component';
import { NavigationComponent } from './navigation/navigation.component';
import { EventlistComponent } from './eventlist/eventlist.component';
import { AboutComponent } from './about/about.component';
import { StorageDetailComponent } from './storage-detail/storage-detail.component';
import { ConfigurationlistComponent } from './configurationlist/configurationlist.component';
import { NotFoundComponent } from './not-found/not-found.component';

export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}

@NgModule({
  declarations: [
    AppComponent,
    OverviewComponent,
    HeaderComponent,
    ProducerDetailComponent,
    ConsumerDetailComponent,
    NavigationComponent,
    EventlistComponent,
    AboutComponent,
    StorageDetailComponent,
    ConfigurationlistComponent,
    NotFoundComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    TranslateModule.forRoot({
      defaultLanguage: 'en',
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [ HttpClient ]
      }
    }),
    MatToolbarModule,
    MatIconModule,
    MatCardModule,
    MatSidenavModule,
    MatListModule,
    MatTableModule,
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
