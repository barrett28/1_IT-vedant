import { Component } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css'],
})
export class CardComponent {
  name: string = 'Mountains Ranges';
  desc: string = 'Shayadri Mountain Ranges Explore the thrilling experience';
  price: number = 15000;
  img: string =
    'https://images.unsplash.com/photo-1744649781353-8a1b70c37a77?q=80&w=1217&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D';
  myName = '';
  isDisabled = false;

  onClickButton() {
    console.log('button clicked');
  }

  onInput(event: any) {
    this.myName += event.data;
    console.log(this.myName);
  }
}
