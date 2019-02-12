import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AppGithubProjects } from './github-projects';
import { AppHome } from './home';

const routes: Routes = [
  { path: 'developpement-logiciel', component: AppGithubProjects},
  { path: '', component: AppHome}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
