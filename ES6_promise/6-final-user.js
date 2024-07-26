import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const results = await Promise.allSettled([
    signUpUser(firstName, lastName), // Call signUpUser with firstName and lastName
    uploadPhoto(fileName) // Call uploadPhoto with fileName
  ]);

  // Map results to the required format
  return results.map(result => ({
    status: result.status,
    value: result.status === 'fulfilled' ? result.value : result.reason
  }));
}

export default handleProfileSignup;
