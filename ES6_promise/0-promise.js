export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const response = true;
    if (response) {
      resolve('Success');
    } else {
      reject(new Error('Failure'));
    }
  });
}
