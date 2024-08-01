import Car from './10-car.js';

class EVCar extends Car {
    constructor(brand, motor, color, range) {
        super(brand, motor, color); // Appel du constructeur de Car
        this._range = range; // Stockage de la portée
    }

    cloneCar() {
        // Renvoie une instance de Car au lieu de EVCar
        return new Car(this._brand, this._motor, this._color);
    }
}

export default EVCar;