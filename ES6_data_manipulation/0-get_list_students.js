function getListStudents() {
  // Create an array of student objects
  const students = [
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
  
  return students; // Return the array
}

export default getListStudents; // Export the function
