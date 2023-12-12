// const axios = require('axios');
import axios from "axios";

// Replace the URL with the appropriate URL where your Flask app is running
const apiUrl = 'http://127.0.0.1:5000';

// Make a GET request
const getdata = async () => {
    try {
      const response = await axios.get(apiUrl+"/get_data");
      console.log("in axios get");
      console.log(response.data);
    } catch (error) {
      console.error('Error:', error.message);
      if (error.response) {
        // The request was made and the server responded with a status code
        console.error('Response status:', error.response.status);
        console.error('Response data:', error.response.data);
      } else if (error.request) {
        // The request was made but no response was received
        console.error('No response received');
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error('Error message:', error.message);
      }
    }
  };

const userService = {
    getdata
}

export default userService