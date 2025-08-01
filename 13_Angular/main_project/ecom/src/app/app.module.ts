import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { CardComponent } from './card/card.component';
import { FooterComponent } from './footer/footer.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [AppComponent, NavbarComponent, CardComponent, FooterComponent],
  imports: [BrowserModule, FormsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
