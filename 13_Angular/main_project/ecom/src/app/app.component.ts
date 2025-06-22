import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'ecom';

  sum(): number {
    const n1 = 1;
    const n2 = 2;
    const sum = n1 + n2;
    return sum;
  }

  constructor() {
    // let name: string = 'angular';
    // name = '5';
    // console.log(name);

    // let myNum: number = 5;
    // myNum = 6;
    // console.log(myNum);

    // console.log(this.sum());

    let student: {
      name: string;
      subject: string;
      marks: number;
    } = {
      name: 'Bharat',
      subject: 'Angular',
      marks: 80,
    };

    console.log(student.subject, 'type of subject is:', typeof student.subject);
  }
}
