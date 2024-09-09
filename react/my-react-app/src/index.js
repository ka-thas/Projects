import React from 'react';
import ReactDOM from 'react-dom/client';

const myFirstElement = <div>Hello React!</div>

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(myFirstElement);

export default App;

class Car {
  constructor(name) {
    this.brand = name;

  }

  present() {
    return 'i have a ' + this.brand
  }
}

class Model extends Car {
  constructor(name, mod) {
    super(name);
    this.model = mod;
  }

  show() {
    return this.present() + ', it is a ' + this.model;
  }
}

const mycar = new Model("Toyota", 'Corola');
mycar.present();
mycar.show();
console.log(mycar.show())