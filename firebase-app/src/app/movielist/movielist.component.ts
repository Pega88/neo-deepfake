import { Component, OnInit } from '@angular/core';
import { UserService } from '../core/user.service';
import { AuthService } from '../core/auth.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { FirebaseUserModel } from '../core/user.model';
// import * as firebase from 'firebase';

@Component({
  selector: 'page-movielist',
  templateUrl: 'movielist.component.html',
  styleUrls: ['movielist.scss']
})
export class MovielistComponent implements OnInit{

  availeable_profiles: Object[];
  tab1: boolean;
  tab2: boolean;
  tab3: boolean;
  registerForm: FormGroup;
  // requestForm: FormGroup;

  constructor(private fb: FormBuilder) {
    // public userService: UserService
    this.createForm();
    this.setActive(1);

    this.availeable_profiles = [
      {
        pic: "https://storage.googleapis.com/neo-zurich/max.png",
        name: "Maxime Vandepoel",
        score: "5",
        price: "10"
      },
      {
        pic: "https://storage.googleapis.com/neo-zurich/niels.jpeg",
        name: "Niels Buekers",
        score: "4",
        price: "2"
      },
      {
        pic: "https://storage.googleapis.com/neo-zurich/serge.jpeg",
        name: "Serge Hendrickx",
        score: "4",
        price: "5"
      }
    ];

    // this.requestForm = this.fb.group({
    //   request: [name, Validators.required ]
    // });

  }

  createForm() {
    this.registerForm = this.fb.group({
      email: ['', Validators.required ],
      password: ['',Validators.required]
    });
  }

  tryRegister(value){
    console.log(value)
    // this.authService.doRegister(value)
    // .then(res => {
    //   console.log(res);
    //   this.errorMessage = "";
    //   this.successMessage = "Your account has been created";
    // }, err => {
    //   console.log(err);
    //   this.errorMessage = err.message;
    //   this.successMessage = "";
    // })
  }



  //
  // constructor(
  //   public userService: UserService//,
  //   // public authService: AuthService,
  //   // private route: ActivatedRoute,
  //   // private location : Location,
  //   // private fb: FormBuilder
  // ) {
  //   // this.authService.testpost();
  // }

  ngOnInit(): void {
    // this.route.data.subscribe(routeData => {
    //   this.subscribed = false;
    //   let data = routeData['data'];
    //   if (data) {
    //     this.user = data;
    //     this.createForm(this.user.name);
    //   }
    // })
  }

  // createForm(name) {
  //   this.profileForm = this.fb.group({
  //     name: [name, Validators.required ]
  //   });
  // }
  //
  setActive(i){
    if(i==1){
      this.tab1 = true;
      this.tab2 = false;
      this.tab3 = false;
    }
    if(i==2){
      this.tab1 = false;
      this.tab2 = true;
      this.tab3 = false;
    }
    if(i==3){
      this.tab1 = false;
      this.tab2 = false;
      this.tab3 = true;
    }
  }


  requestVideo(){

    // console.log(value)
    console.log(document.getElementById("test"));

    // this.userService.updateCurrentUser(value)
    // .then(res => {
    //   console.log(res);
    // }, err => console.log(err))
  }

  // unsubscribe(){
  //   console.log("unsubscribe")
  //   this.subscribed = false
  // }
  //
  // refreshList(){
  // this.authService.testpost();
  // }
  //
  // save(value){
  //
  //   this.userService.updateCurrentUser(value)
  //   .then(res => {
  //     console.log(res);
  //   }, err => console.log(err))
  // }
  //
  // logout(){
  //   this.authService.doLogout()
  //   .then((res) => {
  //     this.location.back();
  //   }, (error) => {
  //     console.log("Logout error", error);
  //   });
  //
  //
  //
  // }
}
