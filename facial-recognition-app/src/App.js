import { useState } from 'react';
import './App.css';
const uuid = require('uuid');

function App() {
  const [image, setImage]=useState('');
  const [uploadResultMessage, setUploadResultMessage]=useState('Upload your picture to authenticate entry');
  const [visitorName, setVisitorName]=useState('placeholder.jpg');
  const [isAuth, setAuth] = useState(false);

  function sendImage(e){
    e.preventDefault();
    setVisitorName(image.name);
    const visitorImageName = uuid.v4();
    fetch(`https://t15ochfpbk.execute-api.ca-central-1.amazonaws.com/dev/nihal-visitor-image-storage/${visitorImageName}.jpeg`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'image/jpeg'
      },
      body: image
    }).then(async () => {
       const response = await authenticate(visitorImageName);
       if (response.Message === 'Success') {
        setAuth(true);
        setUploadResultMessage(`Hi ${response['firstName']} ${response['lastName']}, welcome to the office!`)
       } else {
        setAuth(false);
        setUploadResultMessage('Employee not recognized')
       }
    }).catch(error => {
      setAuth(false);
      setUploadResultMessage('Error during authentication')
      console.error(error);
    })
  }

  async function authenticate(visitorImageName){
    const requestUrl = 'https://t15ochfpbk.execute-api.ca-central-1.amazonaws.com/dev/employee?' + new URLSearchParams({
      objectKey: `${visitorImageName}.jpeg`
    });
    return await fetch(requestUrl, {
      method: 'GET',
      headers:  {
        'Accept': 'application/json'
      }
    }).then(response=>response.json())
    .then((data)=>{
      return data;
    }).catch(error =>  console.error(error));
  }

  return (
    <div className="App">
      <h2>Office Sign-In (Facial Recognition)</h2>
      <form onSubmit={sendImage}>
        <input type='file' name='image' onChange={e => setImage(e.target.files[0])}/>
        <button type='submit'>Authenticate</button>
      </form>
      <div className={isAuth ? 'success' : 'failure'}>{uploadResultMessage}</div>
      <img src={require(`./visitors/${visitorName}`)} alt="visitor" height={250} width={250}/>
    </div>
  );
}

export default App;
