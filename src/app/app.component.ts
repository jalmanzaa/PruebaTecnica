import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = '2Dimagen';

}
export function estimate_area(image: any): void {
  const reader = new FileReader();
  reader.onload = (event: any) => {
    const img = new Image();
    img.onload = () => {
      const canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.drawImage(img, 0, 0);
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        if (imageData) {
          const data = imageData.data;
          let area = 0;
          for (let i = 0; i < data.length; i += 4) {
            if (data[i] > 0 && data[i + 1] === 0 && data[i + 2] === 0 && data[i + 3] > 0) {
              area++;
            }
          }
          console.log(`El área estimada de la mancha es de ${area} píxeles`);
        }
      }
    };
    img.src = event.target.result;
  };
  reader.readAsDataURL(image);
}


