import { Component } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Projets';
  
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
