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
  requests_by_niels: Object[];

  constructor(private fb: FormBuilder, public authService: AuthService) {
    // public userService: UserService
    this.createForm();
    this.setActive(1);

    this.availeable_profiles = [
      {
        pic: "https://storage.googleapis.com/neo-zurich/max.png",
        name: "Maxime Vandepoel",
        score: "5",
        price: "100"
      },
      {
        pic: "https://storage.googleapis.com/neo-zurich/niels.jpeg",
        name: "Niels Buekers",
        score: "4",
        price: "200"
      },
      {
        pic: "https://storage.googleapis.com/neo-zurich/serge.jpeg",
        name: "Serge Hendrickx",
        score: "3",
        price: "150"
      }
    ];



    // this.requestForm = this.fb.group({
    //   request: [name, Validators.required ]
    // });

  }

  createForm() {
    this.registerForm = this.fb.group({
      phrase: ['', Validators.required ]
    });
  }

  tryRegister(value, username, map){
    console.log(value)
    console.log(map)
    console.log(username)

    this.authService.saveNewRequest(username+"_vid1", value.phrase, 'Niels@fourcast.io',  map)


    this.authService.postToStatus({'requester':username, 'requestedPhrase': value, 'requestedPerson': username})
    .subscribe(
        (val) => {
          console.log(val);
          this.openPopup(String(JSON.stringify(val)))
        },
        response => {
            this.openPopup(String(JSON.stringify(response)))
            console.log("POST call in error", response);
        },
        () => {
            console.log("The POST observable is now completed.");
        });
  }

  openPopup(content){
    var x=window.open('','','width=600, height=600');
    x.document.open();
    x.document.write(content);
    x.document.close();
  }



  ngOnInit(): void {
  }

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
      this.getRequests();
    }
    if(i==3){
      this.tab1 = false;
      this.tab2 = false;
      this.tab3 = true;
    }
  }



  getRequests(){
    var lines = []
    var baseTable = `
    <table class="table table-hover">
      <thead>
        <tr>
          <th style="width:20%" scope="col">Preview</th>
          <th style="width:20%" scope="col">Name</th>
          <th style="width:30%" scope="col">Phrase</th>
          <th style="width:20%" scope="col">Status</th>
        </tr>
      </thead>
      <tbody>
      `
      var endTable = `    </tbody>
          </table>`

    lines.push(baseTable)
    var requests_by_niels = this.authService.getRequestDoneByUser("Niels@fourcast.io").then(

      (res) => {console.log(res);

        res.forEach(doc => {
          console.log(doc);
            lines.push(`<tr> `)
            lines.push(`<td  style="height:100px"><img src="`+doc.map.pic+`" alt="test" class="img-thumbnail"></td> `)
            lines.push(`<td>`+doc.map.name+`</td> `)
            lines.push(`<td>`+doc.phrase+`</ td> `)
            lines.push(`<td>`+doc.status+`</ td> `)
            lines.push(`</tr> `)
          })

      lines.push(endTable)
      console.log(lines.join(" "))
      document.getElementById("requests").innerHTML = lines.join(" ");
    })

  }


  requestVideo(){
    console.log(document.getElementById("test"));
  }

}
