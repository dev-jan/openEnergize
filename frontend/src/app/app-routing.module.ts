import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { EventlistComponent } from './eventlist/eventlist.component';
import { OverviewComponent } from './overview/overview.component';

const routes: Routes = [
  { path: 'overview', component: OverviewComponent },
  { path: 'eventlist', component: EventlistComponent },
  { path: 'about', component: AboutComponent },
  { path: '', redirectTo: '/overview', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
