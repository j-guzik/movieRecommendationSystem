import { Injectable } from '@angular/core';
import * as firebase from 'firebase/app';
import { AngularFireAuth } from '@angular/fire/auth';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private user: Observable<firebase.User | null | undefined>;
  public userID: string;
  configUrl = 'http://127.0.0.1:5000/newUser/';
  fetchedUser = [];
  error;

  constructor(private firebaseAuth: AngularFireAuth, private http: HttpClient) {
    this.user = this.firebaseAuth.authState;
  }

  signup(email: string, password: string) {
    this.firebaseAuth.auth
      .createUserWithEmailAndPassword(email, password)
      .then((x) => {
        this.createInternalUser(x.user.uid);
        console.log('Sign up!', x.user.uid);
      })
      .catch((err) => {
        console.log('Error:', err.message);
        this.error = err;
        return this.error;
      });
  }

  signin(email: string, password: string) {
    this.firebaseAuth.auth
      .signInWithEmailAndPassword(email, password)
      .then((x) => {
        this.userID = x.user.uid;
        console.log('Sign in', x.user.uid);
      })
      .catch((err) => {
        console.log('Error:', err.message);
      });
  }

  signout() {
    this.firebaseAuth.auth.signOut();
  }

  createInternalUser(uid: string) {
    this.http.get(this.configUrl + uid).subscribe(
      (response: any) => console.log(response),
      (error) => console.log(error)
    );
  }
}
