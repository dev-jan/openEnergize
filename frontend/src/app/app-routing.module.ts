import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { ConfigurationlistComponent } from './configurationlist/configurationlist.component';
import { EventlistComponent } from './eventlist/eventlist.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { OverviewComponent } from './overview/overview.component';

const routes: Routes = [
  { path: 'overview', component: OverviewComponent },
  { path: 'eventlist', component: EventlistComponent },
  { path: 'about', component: AboutComponent },
  { path: 'configurations', component: ConfigurationlistComponent },
  { path: '404', component: NotFoundComponent },
  { path: '', redirectTo: '/overview', pathMatch: 'full' },
  { path: '**', redirectTo: '/404' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
