import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService } from '../auth.service';
import { PageEvent } from '@angular/material/paginator';
import { ChangeDetectorRef, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
@Injectable({ providedIn: 'root' })
export class DashboardComponent implements OnInit {
  // currentRate = 0;
  configUrl = 'http://127.0.0.1:5000/predictions/';
  configGetUrl = 'http://127.0.0.1:5000/getUser/';
  moviesUrl = 'http://127.0.0.1:5000/getMovies';
  popularUrl = 'http://127.0.0.1:5000/getPopularMovies';
  rateUrl = 'http://127.0.0.1:5000/rateItem/';
  currentRateUrl = 'http://127.0.0.1:5000/currentRate/';
  recommUrl = 'http://127.0.0.1:5000/recommendations/';
  fetchedMovies = [];
  fetchedAllMovies = [];
  fetchedPopularMovies = [];
  popularMovies1 = [];
  popularMovies2 = [];
  pageOfItems: Array<any>;
  ratedValue = null;
  currentStars = 0;
  loader = true;

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    setTimeout(() => this.getUser(this.authService.userID), 2100);
    // this.fetchedMovies = Array(1500)
    //   .fill(0)
    //   .map((x, i) => ({ id: i + 1, name: `Movies ${i + 1}` }));
  }

  // getRecommendation(uid) {
  //   this.http.get(this.configUrl + uid).subscribe(
  //     (response: any) => {
  //       this.fetchedMovies = response;
  //     },
  //     (error) => console.log(error)
  //   );
  // }

  // getUser(uid: string) {
  //   this.http.get(this.configGetUrl + uid).subscribe(
  //     (response: any) => this.getRecommendation(response[0]),
  //     (error) => console.log(error)
  //   );
  // }

  getUser(uid: string) {
    this.http.get(this.configGetUrl + uid).subscribe(
      (response: any) => {
        this.getMovies(), this.getPopularMovies(), this.getRecommendation(uid);
        setTimeout(() => {
          // <<<---using ()=> syntax
          this.loader = false;
        }, 500);
      },
      (error) => console.log(error)
    );
  }

  getRecommendation(uid) {
    this.http.get(this.recommUrl + uid).subscribe(
      (response: any) => {
        this.fetchedMovies = response;
      },
      (error) => console.log(error)
    );
  }

  getMovies() {
    this.http.get(this.moviesUrl).subscribe(
      (response: any) => {
        this.fetchedAllMovies = response;
      },
      (error) => console.log(error)
    );
  }

  getPopularMovies() {
    this.http.get(this.popularUrl).subscribe(
      (response: any) => {
        this.fetchedPopularMovies = response;
        this.popularMovies1 = this.fetchedPopularMovies.slice(0, 4);
        this.popularMovies2 = this.fetchedPopularMovies.slice(4);
      },
      (error) => console.log(error)
    );
  }

  rateItem(movie) {
    this.http
      .get(
        this.rateUrl +
          movie +
          '/' +
          this.ratedValue +
          '/' +
          this.authService.userID
      )
      .subscribe(
        (response: any) => {
          console.log(response);
        },
        (error) => console.log(error)
      );
    // console.log(this.ratedValue, movie);
  }

  currentRate(movie) {
    this.http
      .get(this.currentRateUrl + movie + '/' + this.authService.userID)
      .subscribe(
        (response: any) => {
          this.currentStars = response;
          this.cdr.detectChanges();
        },
        (error) => {
          this.currentStars = 0;
          this.cdr.detectChanges();
          console.log(error);
        }
      );
  }

  onChangePage(pageOfItems: Array<any>) {
    this.pageOfItems = pageOfItems;
  }
}
