import { Component } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css'],
})
export class CardComponent {
  // name: string = 'Mountains Ranges';
  // desc: string = 'Shayadri Mountain Ranges Explore the thrilling experience';
  // price: number = 15000;
  // img: string =
  //   'https://images.unsplash.com/photo-1744649781353-8a1b70c37a77?q=80&w=1217&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D';
  myName = '';
  isDisabled = false;

  newProduct = {
    name: '',
    description: '',
    price: '',
    img: 'https://images.unsplash.com/photo-1591914227599-30b05407ed7b?q=80&w=1167&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
  };

  product1 = {
    name: 'Lakes',
    desc: 'Beautiful Uncrowded lakes',
    price: 10000,
    img: 'https://images.unsplash.com/photo-1720884413532-59289875c3e1?q=80&w=735&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
  };

  products: any = [
    {
      name: 'Mountains Ranges',
      desc: 'Shayadri Mountain Ranges Explore the thrilling experience',
      price: 15000,
      img: 'https://images.unsplash.com/photo-1744649781353-8a1b70c37a77?q=80&w=1217&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    },
    {
      name: 'Lakes',
      desc: 'Beautiful Uncrowded lakes',
      price: 10000,
      img: 'https://images.unsplash.com/photo-1720884413532-59289875c3e1?q=80&w=735&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    },
  ];

  onClickButton() {
    console.log('button clicked');
  }

  onInput(event: any) {
    this.myName += event.data;
    console.log(this.myName);
  }

  onSubmit() {
    // console.log(this.newProduct);
    this.products.push(this.newProduct);
    this.newProduct = {
      name: '',
      description: '',
      price: '',
      img: 'https://images.unsplash.com/photo-1720884413532-59289875c3e1?q=80&w=735&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    };
  }
}
