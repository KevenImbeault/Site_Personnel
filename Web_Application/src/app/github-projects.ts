import { Component } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-github-projects',
  templateUrl: './github-projects.html',
  styleUrls: ['./app.component.css']
})
export class AppGithubProjects {
  title = 'Développement logiciel';

  model = {
    left: true,
    middle: false,
    right: false
  };
  
  constructor(private httpService: HttpClient) { }
  array: string [];

  ngOnInit() {
    this.httpService.get('http://localhost:5000/api/github').subscribe(
      data => {
        this.array = data as string [];
      },
      (err: HttpErrorResponse) => {
        console.log(err.message);
      }
    );
  }

}
