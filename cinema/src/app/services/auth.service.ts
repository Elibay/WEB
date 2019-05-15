import {EventEmitter, Injectable} from '@angular/core';
import {Main} from './main.service';
import {HttpClient} from '@angular/common/http';
import { patchComponentDefWithScope } from '@angular/core/src/render3/jit/module';
import { IAuthResponse } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class AuthService extends Main {


  constructor(http: HttpClient) {
    super(http);
  }

  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://192.168.1.10:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://192.168.1.10:8000/api/logout/', {});
  }
}