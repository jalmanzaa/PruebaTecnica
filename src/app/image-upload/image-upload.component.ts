import { Component } from '@angular/core';
import { estimate_area } from '../app.component';

@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.component.html',
  styleUrls: ['./image-upload.component.scss']
})
export class ImageUploadComponent {
  image: any;

  onFileSelected(event: any) {
    this.image = event.target.files[0];
  }

  onSubmit() {
    estimate_area(this.image);
  }
}


