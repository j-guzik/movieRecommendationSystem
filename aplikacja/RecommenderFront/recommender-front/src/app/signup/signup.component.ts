import { Component, OnInit } from '@angular/core';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent implements OnInit {
  email: string;
  password: string;
  error;

  constructor(public authService: AuthService) {}

  ngOnInit(): void {}

  signup(email: any, password: any) {
    this.email = email;
    this.password = password;
    this.error = this.authService.signup(this.email, this.password);
    this.email = this.password = '';
  }
}
