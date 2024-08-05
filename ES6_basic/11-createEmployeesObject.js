export default function createEmployeesObject(departmentName, employees) {
  return {
    [departmentName]: employees, // Utilisation de la syntaxe des objets pour définir la clé dynamique
  };
}
