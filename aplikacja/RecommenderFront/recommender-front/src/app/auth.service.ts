import { Injectable } from '@angular/core';
import * as firebase from 'firebase/app';
import { AngularFireAuth } from '@angular/fire/auth';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private user: Observable<firebase.User | null | undefined>;
  public userID: string;
  configUrl = 'http://127.0.0.1:5000/newUser/';
  fetchedUser = [];
  firebaseErrors = {
    'auth/user-not-found':
      'Brak użytkownika odpowiadającego podanemu adresowi email.',
    'auth/email-already-in-use':
      'Podany adres e-mail jest już używany przez istniejącego użytkownika.',
    'auth/invalid-email': 'Podany email jest nieprawidłowy.',
    'auth/invalid-password': 'Podane hasło jest nieprawidłowe.',
    'auth/wrong-password': 'Podane hasło jest nieprawidłowe.',
    'auth/weak-password': 'Hasło musi zawierać 6 lub więcej znaków.',
    'auth/network-request-failed': 'Wystąpił błąd sieci.',
  };

  constructor(
    private firebaseAuth: AngularFireAuth,
    private http: HttpClient,
    private router: Router
  ) {
    this.user = this.firebaseAuth.authState;
  }

  signup(email: string, password: string) {
    this.firebaseAuth.auth
      .createUserWithEmailAndPassword(email, password)
      .then((x) => {
        this.createInternalUser(x.user.uid);
        this.router.navigate(['/dashboard']);
        console.log('Sign up!', x.user.uid);
      })
      .catch((err) => {
        console.log('Error:', err.message);
        const message = document.getElementById('error');
        message.textContent = this.firebaseErrors[err.code] || err.message;
      });
  }

  signin(email: string, password: string) {
    this.firebaseAuth.auth
      .signInWithEmailAndPassword(email, password)
      .then((x) => {
        this.userID = x.user.uid;
        this.router.navigate(['/dashboard']);
        console.log('Sign in', x.user.uid);
      })
      .catch((err) => {
        console.log('Error:', err.message);
        const message = document.getElementById('error');
        message.textContent = this.firebaseErrors[err.code] || err.message;
      });
  }

  signout() {
    this.firebaseAuth.auth.signOut();
    this.router.navigate(['/home']);
  }

  createInternalUser(uid: string) {
    this.http.get(this.configUrl + uid).subscribe(
      (response: any) => console.log(response),
      (error) => console.log(error)
    );
  }
}
