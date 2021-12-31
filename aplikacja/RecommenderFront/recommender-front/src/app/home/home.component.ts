import { Component, OnInit } from '@angular/core';
import { EmailValidator } from '@angular/forms';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  constructor(private authService: AuthService) {}

  ngOnInit(): void {}

  signin(email: any, password: any) {
    this.authService.signin(email, password);
  }
}
